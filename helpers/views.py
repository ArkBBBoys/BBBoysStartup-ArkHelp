import math

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from accounts.models import HelperProfile, UserProfile
from helpers.choices import (
    DIVISION_CHOICES, DISTRICT_CHOICES, SERVICE_TYPE_CHOICES,
    PLACE_TYPE_CHOICES, SERVICE_CATEGORIES, SERVICE_TYPE_ICONS,
    get_districts_by_division, get_upazilas_by_district
)
from hirings.models import Review


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(dlon / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def home(request):
    """Home page with hero section and featured helpers"""
    featured_helpers = HelperProfile.objects.filter(
        is_verified_by_admin=True,
        availability_status='available'
    ).select_related('user_profile__user').order_by('-average_rating')[:6]

    # Count stats
    total_helpers = HelperProfile.objects.filter(is_verified_by_admin=True).count()
    total_services = len(SERVICE_TYPE_CHOICES)

    context = {
        'featured_helpers': featured_helpers,
        'divisions': DIVISION_CHOICES,
        'service_categories': SERVICE_CATEGORIES,
        'service_icons': SERVICE_TYPE_ICONS,
        'service_types': SERVICE_TYPE_CHOICES,
        'total_helpers': total_helpers,
        'total_services': total_services,
    }
    return render(request, 'helpers/home.html', context)


def helper_list(request):
    """List all verified helpers with enhanced filters"""
    helpers = HelperProfile.objects.filter(
        is_verified_by_admin=True
    ).select_related('user_profile__user').order_by('-average_rating')

    # Enhanced filters
    division = request.GET.get('division')
    district = request.GET.get('district')
    upazila = request.GET.get('upazila')
    place_type = request.GET.get('place_type')
    service_type = request.GET.get('service_type')
    min_rating = request.GET.get('min_rating')
    max_rate = request.GET.get('max_rate')
    availability = request.GET.get('availability')
    search = request.GET.get('search')
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    radius = request.GET.get('radius')

    if division:
        helpers = helpers.filter(user_profile__division=division)

    if district:
        helpers = helpers.filter(user_profile__district=district)

    if upazila:
        helpers = helpers.filter(user_profile__upazila=upazila)

    if place_type:
        helpers = helpers.filter(user_profile__place_type=place_type)

    if service_type:
        helpers = helpers.filter(service_types__icontains=service_type)

    if min_rating:
        helpers = helpers.filter(average_rating__gte=float(min_rating))

    if max_rate:
        r = float(max_rate)
        helpers = helpers.filter(
            Q(monthly_rate__lte=r) |
            Q(monthly_rate__isnull=True, hourly_rate__lte=r)
        )

    if availability:
        helpers = helpers.filter(availability_status=availability)

    if search:
        helpers = helpers.filter(
            Q(user_profile__user__first_name__icontains=search) |
            Q(user_profile__user__last_name__icontains=search) |
            Q(user_profile__division__icontains=search) |
            Q(user_profile__district__icontains=search) |
            Q(user_profile__upazila__icontains=search) |
            Q(user_profile__village_city_area__icontains=search) |
            Q(bio__icontains=search)
        )

    # Location-based proximity filter (Haversine)
    if lat and lng:
        try:
            lat_f, lng_f = float(lat), float(lng)
            r = float(radius) if radius else 10.0
            # Bounding box pre-filter (rough, ~10% margin)
            lat_deg = r / 111.0
            lng_deg = r / (111.0 * math.cos(math.radians(lat_f)))
            helpers = helpers.filter(
                user_profile__latitude__isnull=False,
                user_profile__longitude__isnull=False,
                user_profile__latitude__gte=lat_f - lat_deg,
                user_profile__latitude__lte=lat_f + lat_deg,
                user_profile__longitude__gte=lng_f - lng_deg,
                user_profile__longitude__lte=lng_f + lng_deg,
            )
            # Exact Haversine filter
            nearby = []
            for h in helpers.select_related('user_profile'):
                dist = haversine_km(
                    lat_f, lng_f,
                    h.user_profile.latitude, h.user_profile.longitude,
                )
                if dist <= r:
                    nearby.append(h.pk)
            helpers = helpers.filter(pk__in=nearby)
        except (ValueError, TypeError):
            pass

    # Cascade districts based on selected division
    if division:
        districts_for_template = get_districts_by_division(division)
    else:
        districts_for_template = DISTRICT_CHOICES

    # Cascade upazilas based on selected district
    if district and division:
        districts_for_division = get_districts_by_division(division)
        district_codes = [d[0] for d in districts_for_division]
        if district in district_codes:
            upazilas_for_template = get_upazilas_by_district(district)
        else:
            upazilas_for_template = []
    elif district:
        upazilas_for_template = get_upazilas_by_district(district)
    else:
        upazilas_for_template = []

    paginator = Paginator(helpers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'helpers': page_obj.object_list,
        'divisions': DIVISION_CHOICES,
        'districts': districts_for_template,
        'upazilas': upazilas_for_template,
        'service_types': SERVICE_TYPE_CHOICES,
        'service_categories': SERVICE_CATEGORIES,
        'service_icons': SERVICE_TYPE_ICONS,
        'place_types': PLACE_TYPE_CHOICES,
        'selected_division': division,
        'selected_district': district,
        'selected_upazila': upazila,
        'selected_place_type': place_type,
        'selected_service': service_type,
        'selected_min_rating': min_rating,
        'selected_max_rate': max_rate,
        'selected_availability': availability,
        'selected_search': search,
        'selected_lat': lat,
        'selected_lng': lng,
        'selected_radius': radius,
    }
    return render(request, 'helpers/helper_list.html', context)


def helper_detail(request, pk):
    """Show helper detail page with reviews"""
    helper = get_object_or_404(
        HelperProfile.objects.select_related('user_profile__user'),
        pk=pk
    )

    reviews = Review.objects.filter(
        hiring__helper=helper
    ).select_related('hiring__user__user').order_by('-created_at')[:10]

    user_can_review = False
    if request.user.is_authenticated:
        try:
            user_profile = request.user.profile
            for hiring in user_profile.hirings.filter(helper=helper, status='completed'):
                from datetime import date
                if (date.today() - hiring.start_date).days >= 1 and not hasattr(hiring, 'review'):
                    user_can_review = True
                    break
        except UserProfile.DoesNotExist:
            pass

    context = {
        'helper': helper,
        'reviews': reviews,
        'user_can_review': user_can_review,
        'service_icons': SERVICE_TYPE_ICONS,
        'service_types': SERVICE_TYPE_CHOICES,
    }
    return render(request, 'helpers/helper_detail.html', context)


def get_districts(request):
    """AJAX endpoint to get districts by division"""
    division = request.GET.get('division', '').lower()
    if division:
        districts = get_districts_by_division(division)
        return JsonResponse({'districts': districts})
    return JsonResponse({'districts': []})


def get_upazilas(request):
    """AJAX endpoint to get upazilas by district"""
    district = request.GET.get('district', '').lower()
    if district:
        upazilas = get_upazilas_by_district(district)
        return JsonResponse({'upazilas': upazilas})
    return JsonResponse({'upazilas': []})


def ajax_districts(request):
    """AJAX endpoint returning JSON of districts by division"""
    division = request.GET.get('division', '').lower()
    districts = get_districts_by_division(division) if division else []
    return JsonResponse({'districts': [{'code': d[0], 'name': d[1]} for d in districts]})


def ajax_upazilas(request):
    """AJAX endpoint returning JSON of upazilas by district"""
    district = request.GET.get('district', '').lower()
    upazilas = get_upazilas_by_district(district) if district else []
    return JsonResponse({'upazilas': [{'code': u[0], 'name': u[1]} for u in upazilas]})


def get_nearby_helpers(request):
    """API endpoint for location-based nearby helpers"""
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    radius = float(request.GET.get('radius', 10))

    if not lat or not lng:
        return JsonResponse({'helpers': []})

    helpers = HelperProfile.objects.filter(
        is_verified_by_admin=True,
        availability_status='available',
        user_profile__latitude__isnull=False,
        user_profile__longitude__isnull=False,
    )

    lat_f, lng_f = float(lat), float(lng)
    lat_deg = radius / 111.0
    lng_deg = radius / (111.0 * math.cos(math.radians(lat_f)))
    helpers = helpers.filter(
        user_profile__latitude__gte=lat_f - lat_deg,
        user_profile__latitude__lte=lat_f + lat_deg,
        user_profile__longitude__gte=lng_f - lng_deg,
        user_profile__longitude__lte=lng_f + lng_deg,
    )

    data = []
    for h in helpers.select_related('user_profile__user')[:20]:
        dist = haversine_km(lat_f, lng_f, h.user_profile.latitude, h.user_profile.longitude)
        if dist > radius:
            continue
        data.append({
            'id': h.pk,
            'name': h.user_profile.user.get_full_name(),
            'district': h.user_profile.get_district_display(),
            'services': h.get_display_services()[:3],
            'rating': float(h.average_rating),
            'photo': h.user_profile.profile_photo.url if h.user_profile.profile_photo else None,
        })

    return JsonResponse({'helpers': data})
