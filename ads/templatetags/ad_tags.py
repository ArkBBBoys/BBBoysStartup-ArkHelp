from django import template
from django.core.cache import cache
from django.utils import timezone

register = template.Library()


@register.simple_tag
def get_ads(page_type, ad_type=None, limit=5):
    """
    Get active ads for a specific page type.
    Usage: {% get_ads 'home' as ads %}
           {% get_ads 'helpers' 'banner' 3 as ads %}
    """
    cache_key = f'ads_{page_type}_{ad_type}_{limit}'
    ads = cache.get(cache_key)

    if ads is None:
        from ads.models import Ad
        from django.db.models import Q

        queryset = Ad.objects.filter(is_active=True)

        # Filter by placement
        if page_type != 'all':
            queryset = queryset.filter(Q(placement='all') | Q(placement=page_type))

        # Filter by ad type if specified
        if ad_type:
            queryset = queryset.filter(ad_type=ad_type)

        # Filter by date range and impressions in Python
        now = timezone.now()
        filtered_ads = []
        for ad in queryset.order_by('-priority', '-created_at')[:limit * 2]:  # Get more to filter
            if not ad.can_show:
                continue
            filtered_ads.append(ad)
            if len(filtered_ads) >= limit:
                break

        ads = filtered_ads
        cache.set(cache_key, ads, 300)  # Cache for 5 minutes

    return ads


@register.simple_tag
def get_popup_ads():
    """Get active popup ads"""
    return get_ads('all', 'popup', 1)


@register.simple_tag
def get_banner_ads(placement='home_bottom', limit=1):
    """Get active banner ads for a specific placement"""
    return get_ads(placement, 'banner', limit)