from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.db import models
from .models import Ad, AdClick, AdImpression
from django.views.decorators.cache import cache_page


def get_ads_for_page(page_type):
    """Get active ads for a specific page type with caching"""
    from django.core.cache import cache

    cache_key = f'ads_{page_type}'
    ads = cache.get(cache_key)

    if ads is None:
        queryset = Ad.objects.filter(
            is_active=True,
        ).filter(
            # Either show on all pages or specific page
            models.Q(placement='all') | models.Q(placement=page_type)
        )

        # Filter by date range
        now = timezone.now()
        queryset = queryset.filter(
            models.Q(start_date__isnull=True) | models.Q(start_date__lte=now),
            models.Q(end_date__isnull=True) | models.Q(end_date__gte=now),
            models.Q(impressions_limit__isnull=True) | models.Q(impressions_count__lt=models.F('impressions_limit'))
        ).order_by('-priority', '-created_at')

        ads = list(queryset.select_related()[:5])
        cache.set(cache_key, ads, 300)  # Cache for 5 minutes

    return ads


def track_impression(request, ad_id):
    """Track ad impression - called via AJAX"""
    ad = get_object_or_404(Ad, pk=ad_id)

    # Update impression count
    Ad.objects.filter(pk=ad_id).update(impressions_count=models.F('impressions_count') + 1)

    # Record impression
    AdImpression.objects.create(
        ad=ad,
        ip_address=get_client_ip(request),
        session_key=request.session.session_key if hasattr(request, 'session') else ''
    )

    return JsonResponse({'status': 'ok'})


def track_click(request, ad_id):
    """Track ad click - called via AJAX"""
    ad = get_object_or_404(Ad, pk=ad_id)

    # Record click
    AdClick.objects.create(
        ad=ad,
        ip_address=get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500]
    )

    # Redirect if URL exists
    if ad.redirect_url:
        return JsonResponse({'status': 'ok', 'redirect': ad.redirect_url})

    return JsonResponse({'status': 'ok'})


def get_client_ip(request):
    """Get client IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    return ip