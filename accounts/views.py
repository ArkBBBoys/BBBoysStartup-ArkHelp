from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from accounts.models import UserProfile, HelperProfile
from helpers.choices import (
    DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES, SERVICE_TYPE_CHOICES,
    PLACE_TYPE_CHOICES, get_districts_by_division, get_upazilas_by_district,
    SERVICE_CATEGORIES, SERVICE_TYPE_ICONS
)


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        account_type = request.POST.get('account_type', 'user')
        phone_number = request.POST.get('phone_number')
        terms_accepted = request.POST.get('terms_accepted')

        if not terms_accepted:
            messages.error(request, 'শর্তাবলী গ্রহণ করা প্রয়োজন।')
            return render(request, 'accounts/signup.html', {
                'divisions': DIVISION_CHOICES,
                'service_categories': SERVICE_CATEGORIES,
                'service_icons': SERVICE_TYPE_ICONS,
            })

        if password1 != password2:
            messages.error(request, 'পাসওয়ার্ড মিলেনি।')
            return render(request, 'accounts/signup.html', {
                'divisions': DIVISION_CHOICES,
                'service_categories': SERVICE_CATEGORIES,
                'service_icons': SERVICE_TYPE_ICONS,
            })

        if len(password1) < 8:
            messages.error(request, 'পাসওয়ারড কমপক্ষে ৮ অক্ষরের হতে হবে।')
            return render(request, 'accounts/signup.html', {
                'divisions': DIVISION_CHOICES,
                'service_categories': SERVICE_CATEGORIES,
                'service_icons': SERVICE_TYPE_ICONS,
            })

        from django.contrib.auth import get_user_model
        User = get_user_model()

        if User.objects.filter(email=email).exists():
            messages.error(request, 'এই ইমেইল ইতিমধ্যে ব্যবহৃত হয়েছে।')
            return render(request, 'accounts/signup.html', {
                'divisions': DIVISION_CHOICES,
                'service_categories': SERVICE_CATEGORIES,
                'service_icons': SERVICE_TYPE_ICONS,
            })

        base_username = email.split('@')[0]
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f'{base_username}{counter}'
            counter += 1

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
        except IntegrityError:
            messages.error(request, 'এই তথ্য দিয়ে নিবন্ধন সম্ভব হচ্ছে না। অনুগ্রহ করে আবার চেষ্টা করুন।')
            return render(request, 'accounts/signup.html', {
                'divisions': DIVISION_CHOICES,
                'service_categories': SERVICE_CATEGORIES,
                'service_icons': SERVICE_TYPE_ICONS,
            })

        profile = UserProfile.objects.get(user=user)
        profile.account_type = account_type
        profile.phone_number = phone_number
        profile.terms_accepted = True
        profile.save()

        if account_type == 'helper':
            HelperProfile.objects.create(
                user_profile=profile,
                service_types='',
                availability_status='available'
            )

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        verify_url = request.build_absolute_uri(f'/accounts/verify-email/{uid}/{token}/')

        try:
            from django.core.mail import EmailMultiAlternatives
            html_content = render_to_string('emails/verification.html', {
                'user': user,
                'verify_url': verify_url,
                'site_name': 'HelpHands',
            })
            msg = EmailMultiAlternatives(
                'HelpHands - ইমেইল যাচাই',
                f'স্বাগতম! আপনার HelpHands অ্যাকাউন্ট যাচাই করতে এই লিঙ্কে ক্লিক করুন: {verify_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'রেজিস্ট্রেশন সফল হয়েছে! অনুগ্রহ করে আপনার ইমেইল যাচাই করুন।')
        except Exception:
            messages.warning(request, 'রেজিস্ট্রেশন সফল হয়েছে কিন্তু যাচাই ইমেইল পাঠানো যায়নি।')

        return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {
        'divisions': DIVISION_CHOICES,
        'service_categories': SERVICE_CATEGORIES,
        'service_icons': SERVICE_TYPE_ICONS,
    })


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'এই ইমেইল দিয়ে কোনো অ্যাকাউন্ট নেই।')
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            messages.success(request, 'সফলভাবে লগইন হয়েছেন!')
            next_url = request.GET.get('next', 'accounts:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'ভুল পাসওয়ার্ড।')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'আপনি লগআউট হয়েছেন।')
    return redirect('helpers:home')


def verify_email(request, uidb64, token):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        profile = user.profile
        profile.is_email_verified = True
        profile.save()
        messages.success(request, 'আপনার ইমেইল সফলভাবে যাচাই হয়েছে!')
        return redirect('accounts:login')

    messages.error(request, 'যাচাই লিঙ্ক অবৈধ বা মেয়াদ উত্তীর্ণ।')
    return redirect('helpers:home')


@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if profile.account_type == 'helper':
        helper_profile = profile.helper_profile
        completeness = 0
        if profile.phone_number: completeness += 10
        if profile.division: completeness += 10
        if profile.district: completeness += 10
        if profile.address: completeness += 10
        if helper_profile.service_types: completeness += 15
        if helper_profile.bio: completeness += 10
        if helper_profile.hourly_rate or helper_profile.monthly_rate: completeness += 10
        if helper_profile.national_id_number: completeness += 10
        if helper_profile.nid_card_image: completeness += 10
        if helper_profile.is_verified_by_admin: completeness += 5

        from hirings.models import Hiring
        recent_hirings = helper_profile.hirings.all()[:5]
        pending_count = helper_profile.hirings.filter(status='pending').count()
        active_count = helper_profile.hirings.filter(status='active').count()
        completed_count = helper_profile.hirings.filter(status='completed').count()

        context = {
            'profile': profile,
            'helper_profile': helper_profile,
            'completeness': completeness,
            'recent_hirings': recent_hirings,
            'pending_count': pending_count,
            'active_count': active_count,
            'completed_count': completed_count,
        }
        return render(request, 'accounts/helper_dashboard.html', context)
    else:
        from hirings.models import Hiring
        my_hirings = profile.hirings.all()[:5]
        reviewable_hirings = []
        for hiring in profile.hirings.filter(status='completed'):
            if hiring.can_review() and not hasattr(hiring, 'review'):
                reviewable_hirings.append(hiring)

        context = {
            'profile': profile,
            'my_hirings': my_hirings,
            'reviewable_hirings': reviewable_hirings,
        }
        return render(request, 'accounts/user_dashboard.html', context)


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if request.method == 'POST':
        profile.phone_number = request.POST.get('phone_number', '')
        profile.division = request.POST.get('division', '')
        profile.district = request.POST.get('district', '')
        profile.upazila = request.POST.get('upazila', '')
        profile.place_type = request.POST.get('place_type', '')
        profile.village_city_area = request.POST.get('village_city_area', '')
        profile.house_address = request.POST.get('house_address', '')
        profile.landmark = request.POST.get('landmark', '')
        profile.latitude = request.POST.get('latitude') or None
        profile.longitude = request.POST.get('longitude') or None
        profile.address = profile.get_full_address()

        if 'profile_photo' in request.FILES:
            profile.profile_photo = request.FILES['profile_photo']

        profile.save()
        messages.success(request, 'প্রোফাইল আপডেট হয়েছে।')
        return redirect('accounts:edit_profile')

    selected_division = profile.division
    selected_district = profile.district
    districts = get_districts_by_division(selected_division) if selected_division else []
    upazilas = get_upazilas_by_district(selected_district) if selected_district else []

    context = {
        'profile': profile,
        'divisions': DIVISION_CHOICES,
        'districts': districts,
        'upazilas': upazilas,
        'place_types': PLACE_TYPE_CHOICES,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required
def edit_helper_profile(request):
    try:
        profile = request.user.profile
        if profile.account_type != 'helper':
            return redirect('accounts:dashboard')
        helper_profile = profile.helper_profile
    except (UserProfile.DoesNotExist, HelperProfile.DoesNotExist):
        return redirect('accounts:signup')

    if request.method == 'POST':
        helper_profile.service_types = ','.join(request.POST.getlist('service_types'))
        helper_profile.experience_years = int(request.POST.get('experience_years', 0))
        helper_profile.hourly_rate = request.POST.get('hourly_rate') or None
        helper_profile.monthly_rate = request.POST.get('monthly_rate') or None
        helper_profile.availability_status = request.POST.get('availability_status', 'unavailable')
        helper_profile.bio = request.POST.get('bio', '')
        helper_profile.national_id_number = request.POST.get('national_id_number', '')

        if 'nid_card_image' in request.FILES:
            helper_profile.nid_card_image = request.FILES['nid_card_image']

        helper_profile.save()
        messages.success(request, 'হেল্পার প্রোফাইল আপডেট হয়েছে।')
        return redirect('accounts:edit_helper_profile')

    current_services = helper_profile.get_services_list()

    context = {
        'profile': profile,
        'helper_profile': helper_profile,
        'service_types': SERVICE_TYPE_CHOICES,
        'service_categories': SERVICE_CATEGORIES,
        'service_icons': SERVICE_TYPE_ICONS,
        'current_services': current_services,
    }
    return render(request, 'accounts/edit_helper_profile.html', context)
