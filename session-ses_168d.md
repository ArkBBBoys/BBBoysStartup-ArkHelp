# New session - 2026-06-05T09:42:13.760Z

**Session ID:** ses_168d697ffffehUq0MZzyzjdGOd
**Created:** 6/5/2026, 3:42:13 PM
**Updated:** 6/5/2026, 3:53:10 PM

---

## User

sumarize the project that is on this directry

---

## Assistant (Build · DeepSeek V4 Flash Free · 3.9s)

_Thinking:_

The user wants me to summarize the project in the current directory. Let me explore the project structure first.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\ASUS\\ArkHelps"
}
```

**Output:**
```
<path>C:\Users\ASUS\ArkHelps</path>
<type>directory</type>
<entries>
.env
.env.example
.git/
.gitignore
.python-version
.venv/
accounts/
ads/
AGENTS.md
CLAUDE.md
cookies.txt
db.sqlite3
helpers/
helphands/
hirings/
manage.py
media/
pyproject.toml
README.md
requirements.txt
SEO_REFERENCE.md
SEO_REPORT.md
static/
staticfiles/
sw.js
templates/
uv.lock

(27 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\ASUS\\ArkHelps\\README.md"
}
```

**Output:**
```
<path>C:\Users\ASUS\ArkHelps\README.md</path>
<type>file</type>
<content>
1: # HelpHands (হেল্পহ্যান্ডস)
2: 
3: A Bangladesh-based platform where people can find, hire, and review trusted domestic helpers.
4: 
5: ## Features
6: 
7: - বিশ্বস্ত কাজের লোক খুঁজুন (Find trusted helping hands)
8: - হেল্পার প্রোফাইল দেখুন (View helper profiles)
9: - হায়ার করুন (Hire helpers)
10: - রিভিউ লিখুন (Write reviews)
11: - অ্যাডমিন ভেরিফিকেশন (Admin verification)
12: 
13: ## Setup Instructions
14: 
15: ### Prerequisites
16: - Python 3.10+
17: - PostgreSQL (optional, SQLite works for development)
18: 
19: ### Installation
20: 
21: 1. Create a virtual environment:
22: ```bash
23: python -m venv venv
24: source venv/bin/activate  # On Windows: venv\Scripts\activate
25: ```
26: 
27: 2. Install dependencies:
28: ```bash
29: pip install -r requirements.txt
30: ```
31: 
32: 3. Create the `.env` file (copy from `.env.example` or create new):
33: ```bash
34: cp .env.example .env
35: # Edit .env with your values
36: ```
37: 
38: 4. Run migrations:
39: ```bash
40: python manage.py makemigrations
41: python manage.py migrate
42: ```
43: 
44: 5. Create superuser:
45: ```bash
46: python manage.py createsuperuser
47: ```
48: 
49: 6. Run development server:
50: ```bash
51: python manage.py runserver
52: ```
53: 
54: ## Environment Variables
55: 
56: See `.env.example` for all required variables:
57: 
58: - `SECRET_KEY` - Django secret key
59: - `DEBUG` - True/False
60: - `ALLOWED_HOSTS` - Comma-separated hosts
61: - `DATABASE_URL` - PostgreSQL connection (optional, SQLite used if empty)
62: - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME` - Backblaze B2 storage
63: - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - Gmail SMTP
64: 
65: ## Account Types
66: 
67: 1. **সাধারণ ব্যবহারকারী** (Regular User) - Anyone looking to hire helpers
68: 2. **হেল্পার** (Helper) - Domestic helpers offering services
69: 
70: ## Tech Stack
71: 
72: - Django 6+
73: - Django Jazzmin (Admin)
74: - Django PWA
75: - Django Allauth (Social Login)
76: - Backblaze B2 / S3 Storage
77: - Whitenoise (Static files)
78: - Pure CSS (No frameworks)
79: 
80: ## License
81: 
82: MIT

(End of file - total 82 lines)
</content>
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.6s)

_Thinking:_

The user wants a summary of the project. I have the AGENTS.md file which has very detailed project info. Let me provide a concise summary based on what I've read.

**HelpHands (হেল্পহ্যান্ডস)** — A Bangladesh domestic helper marketplace built with **Django 6.0.5 + SQLite/PostgreSQL + Whitenoise + PWA**.

**4 Django apps:**
- `accounts/` — User auth, profiles (User/HelperProfile), signup/login/dashboard
- `helpers/` — Browse/search helpers with BD location data (8 divisions, 64 districts)
- `hirings/` — Hiring workflow + reviews (OneToOne per hiring)
- `ads/` — Ad management with impressions/clicks tracking

**Stack:** Django Jazzmin admin, no DRF (all AJAX via JsonResponse), pure CSS (58KB), no jQuery. Bangla-language UI targeting users finding & hiring domestic helpers in Bangladesh.

---

## User

read every comprehensive file and make the readme.md

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.3s)

_Thinking:_

The user wants me to read all comprehensive files and create/update the README.md. Let me first read the key files across the project to understand the full codebase structure, then create a comprehensive README.

Let me read the main files systematically.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Read all core project files (settings, urls, models, views, forms)",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Read app files (accounts, helpers, hirings, ads)",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Read templates and static files structure",
      "status": "pending",
      "priority": "medium"
    },
    {
      "content": "Write comprehensive README.md",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Read all core project files (settings, urls, models, views, forms)",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Read app files (accounts, helpers, hirings, ads)",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Read templates and static files structure",
    "status": "pending",
    "priority": "medium"
  },
  {
    "content": "Write comprehensive README.md",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 94.1s)

_Thinking:_

Let me read all the core project files and app files in parallel.

**Tool: task**

**Input:**
```json
{
  "description": "Read accounts app files",
  "prompt": "Read the following files completely and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\accounts\\models.py\n2. C:\\Users\\ASUS\\ArkHelps\\accounts\\views.py\n3. C:\\Users\\ASUS\\ArkHelps\\accounts\\forms.py\n4. C:\\Users\\ASUS\\ArkHelps\\accounts\\urls.py\n5. C:\\Users\\ASUS\\ArkHelps\\accounts\\admin.py\n\nReturn all file contents with their paths clearly marked.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_168d5a855ffeWRNHMfGgP3E2Ie" state="completed">
<task_result>
## 1. `C:\Users\ASUS\ArkHelps\accounts\models.py` (136 lines)

```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from helpers.choices import (
    ACCOUNT_TYPE_CHOICES, DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES,
    AVAILABILITY_CHOICES, SERVICE_TYPE_CHOICES, PLACE_TYPE_CHOICES
)


class User(AbstractUser):
    def get_initials(self):
        first = (self.first_name or self.username or 'হ')[0]
        last = (self.last_name or '')[0] if self.last_name else ''
        return (first + last).upper()[:2]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='user')
    phone_number = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    division = models.CharField(max_length=20, choices=DIVISION_CHOICES, blank=True)
    district = models.CharField(max_length=30, choices=DISTRICT_CHOICES, blank=True)
    upazila = models.CharField(max_length=50, choices=UPAZILA_CHOICES, blank=True)
    place_type = models.CharField(max_length=20, choices=PLACE_TYPE_CHOICES, blank=True)
    village_city_area = models.CharField(max_length=100, blank=True, help_text="গ্রাম/শহর/এলাকার নাম")
    house_address = models.CharField(max_length=200, blank=True, help_text="বাড়ি/রোড/ব্লক নম্বর")
    landmark = models.CharField(max_length=200, blank=True, help_text="ল্যান্ডমার্ক (ঐচ্ছিক)")
    address = models.TextField(blank=True)

    latitude = models.FloatField(blank=True, null=True, help_text="অক্ষাংশ (GPS)")
    longitude = models.FloatField(blank=True, null=True, help_text="দ্রাঘিমাংশ (GPS)")

    is_email_verified = models.BooleanField(default=False)
    terms_accepted = models.BooleanField(default=False, help_text="শর্তাবলী গ্রহণ করেছেন")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_account_type_display()})"

    def get_full_address(self):
        parts = []
        if self.house_address:
            parts.append(self.house_address)
        if self.village_city_area:
            place_type_name = self.get_place_type_display() if self.place_type else ''
            if place_type_name:
                parts.append(f"{self.village_city_area} ({place_type_name})")
            else:
                parts.append(self.village_city_area)
        if self.upazila:
            parts.append(self.get_upazila_display())
        if self.district:
            parts.append(self.get_district_display())
        if self.division:
            parts.append(self.get_division_display())
        return ', '.join(parts) if parts else ''


class HelperProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='helper_profile')
    service_types = models.CharField(max_length=500, help_text="Comma-separated service types")
    experience_years = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='unavailable')
    bio = models.TextField(blank=True, help_text="Short description in Bangla")
    national_id_number = models.CharField(max_length=20, blank=True)
    nid_card_image = models.ImageField(upload_to='nid_cards/', blank=True, null=True, help_text="এনআইডি কার্ডের ছবি")
    nid_verified = models.BooleanField(default=False, help_text="এনআইডি যাচাই করা হয়েছে")
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    is_verified_by_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile.user.get_full_name()} - হেল্পার"

    def get_services_list(self):
        return [s.strip() for s in self.service_types.split(',') if s.strip()]

    def get_display_services(self):
        services = self.get_services_list()
        service_display = []
        for svc in services:
            for code, name in SERVICE_TYPE_CHOICES:
                if code == svc:
                    service_display.append(name)
                    break
        return service_display


class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default='HelpHands')
    site_description = models.TextField(blank=True)
    debug_mode = models.BooleanField(
        default=True,
        help_text="True = প্রোডাকশন মোড, False = ডেভেলপমেন্ট মোড",
        verbose_name="ডিবাগ মোড"
    )
    domain_url = models.URLField(
        default='http://localhost:8000',
        help_text="সাইটের মূল URL (প্রোডাকশনে পরিবর্তন করুন)",
        verbose_name="ডোমেইন URL"
    )
    site_logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    about_page_content = models.TextField(blank=True)
    terms_page_content = models.TextField(blank=True)
    privacy_page_content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'সাইট কনফিগারেশন'
        verbose_name_plural = 'সাইট কনফিগারেশন'

    def __str__(self):
        return self.site_name

    @classmethod
    def get_settings(cls):
        config, _ = cls.objects.get_or_create(pk=1)
        return config

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
```

## 2. `C:\Users\ASUS\ArkHelps\accounts\views.py` (306 lines)

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

        user = User.objects.create_user(
            username=email.split('@')[0],
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )

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
```

## 3. `C:\Users\ASUS\ArkHelps\accounts\forms.py` (92 lines)

```python
from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile, HelperProfile
from helpers.choices import DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES, SERVICE_TYPE_CHOICES, PLACE_TYPE_CHOICES, AVAILABILITY_CHOICES

User = get_user_model()


class SignupForm(forms.Form):
    account_type = forms.ChoiceField(choices=[('user', 'ব্যবহারকারী'), ('helper', 'হেল্পার')], initial='user')
    first_name = forms.CharField(max_length=150, label='নাম')
    last_name = forms.CharField(max_length=150, required=False, label='পদবি')
    email = forms.EmailField(label='ইমেইল')
    phone_number = forms.CharField(max_length=20, label='ফোন নম্বর')
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='পাসওয়ার্ড')
    password2 = forms.CharField(widget=forms.PasswordInput, label='পাসওয়ার্ড নিশ্চিত করুন')
    terms_accepted = forms.BooleanField(label='শর্তাবলী গ্রহণ')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('এই ইমেইল ইতিমধ্যে ব্যবহৃত হয়েছে।')
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('পাসওয়ার্ড মিলেনি।')
        return cleaned


class LoginForm(forms.Form):
    email = forms.EmailField(label='ইমেইল')
    password = forms.CharField(widget=forms.PasswordInput, label='পাসওয়ার্ড')
    remember = forms.BooleanField(required=False, label='মনে রাখুন')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'division', 'district', 'upazila', 'place_type',
                  'village_city_area', 'house_address', 'landmark', 'latitude', 'longitude',
                  'profile_photo']
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.address = instance.get_full_address()
        if commit:
            instance.save()
        return instance


class HelperProfileForm(forms.ModelForm):
    service_types = forms.MultipleChoiceField(
        choices=SERVICE_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='সেবার ধরন'
    )

    class Meta:
        model = HelperProfile
        fields = ['service_types', 'experience_years', 'hourly_rate', 'monthly_rate',
                  'availability_status', 'bio', 'national_id_number', 'nid_card_image']

    def clean_service_types(self):
        return ','.join(self.cleaned_data.get('service_types', []))

    def save(self, commit=True):
        instance = super().save(commit=False)
        if isinstance(self.cleaned_data.get('service_types'), list):
            instance.service_types = ','.join(self.cleaned_data['service_types'])
        if commit:
            instance.save()
        return instance


class HiringForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='শুরুর তারিখ')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='শেষ তারিখ')
    notes = forms.CharField(widget=forms.Textarea, required=False, label='নোট')


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=[(i, f'{i} ★') for i in range(1, 6)], widget=forms.RadioSelect, label='রেটিং')
    comment = forms.CharField(widget=forms.Textarea, label='মন্তব্য')
```

## 4. `C:\Users\ASUS\ArkHelps\accounts\urls.py` (14 lines)

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit-profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/edit-helper-profile/', views.edit_helper_profile, name='edit_helper_profile'),
]
```

## 5. `C:\Users\ASUS\ArkHelps\accounts\admin.py` (67 lines)

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserProfile, HelperProfile, SiteConfiguration


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'phone_number', 'division', 'district', 'is_email_verified', 'terms_accepted', 'created_at')
    list_filter = ('account_type', 'division', 'district', 'is_email_verified', 'terms_accepted')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone_number')
    raw_id_fields = ('user',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HelperProfile)
class HelperProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'availability_status', 'experience_years', 'hourly_rate', 'monthly_rate', 'average_rating', 'total_reviews', 'is_verified_by_admin', 'nid_verified')
    list_filter = ('availability_status', 'is_verified_by_admin', 'nid_verified', 'service_types')
    search_fields = ('user_profile__user__username', 'user_profile__user__first_name', 'user_profile__user__last_name', 'national_id_number')
    raw_id_fields = ('user_profile',)
    list_editable = ('is_verified_by_admin', 'availability_status', 'nid_verified')

    actions = ['verify_helpers', 'verify_nid', 'mark_available', 'mark_unavailable']

    fieldsets = (
        ('সাধারণ তথ্য', {'fields': ('user_profile', 'service_types', 'bio', 'experience_years')}),
        ('রেটিং ও ফি', {'fields': ('hourly_rate', 'monthly_rate', 'average_rating', 'total_reviews')}),
        ('যাচাইকরণ', {'fields': ('availability_status', 'is_verified_by_admin', 'national_id_number', 'nid_card_image', 'nid_verified')}),
        ('তথ্য', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

    def verify_helpers(self, request, queryset):
        queryset.update(is_verified_by_admin=True)
    verify_helpers.short_description = 'হেল্পার ভেরিফাই করুন'

    def verify_nid(self, request, queryset):
        queryset.update(nid_verified=True)
    verify_nid.short_description = 'এনআইডি যাচাই করুন'

    def mark_available(self, request, queryset):
        queryset.update(availability_status='available')
    mark_available.short_description = 'উপলব্ধ হিসেবে চিহ্নিত করুন'

    def mark_unavailable(self, request, queryset):
        queryset.update(availability_status='unavailable')
    mark_unavailable.short_description = 'অনুপলব্ধ হিসেবে চিহ্নিত করুন'


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'debug_mode', 'domain_url', 'contact_email', 'updated_at')
    fieldsets = (
        ('সাধারণ সেটিংস', {'fields': ('site_name', 'site_description', 'debug_mode', 'domain_url')}),
        ('লোগো ও ফেভিকন', {'fields': ('site_logo', 'favicon')}),
        ('যোগাযোগ তথ্য', {'fields': ('contact_email', 'contact_phone', 'address')}),
        ('সোশ্যাল লিংক', {'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')}),
        ('পেজ কন্টেন্ট', {'fields': ('about_page_content', 'terms_page_content', 'privacy_page_content')}),
    )

    def has_add_permission(self, request):
        if SiteConfiguration.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
```

All 5 files returned in full.
</task_result>
</task>
```

**Tool: task**

**Input:**
```json
{
  "description": "Read helpers app files",
  "prompt": "Read the following files completely and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\helpers\\models.py\n2. C:\\Users\\ASUS\\ArkHelps\\helpers\\views.py\n3. C:\\Users\\ASUS\\ArkHelps\\helpers\\urls.py\n4. C:\\Users\\ASUS\\ArkHelps\\helpers\\choices.py\n5. C:\\Users\\ASUS\\ArkHelps\\helpers\\admin.py\n\nReturn all file contents with their paths clearly marked.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_168d5a4beffeNiKp35HKfmA9F4" state="completed">
<task_result>
Here are the full contents of all 5 files:

---

### 1. `helpers/models.py` (3 lines)

```python
from django.db import models

# Create your models here.
```

---

### 2. `helpers/views.py` (291 lines)

```python
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
```

---

### 3. `helpers/urls.py` (15 lines)

```python
from django.urls import path
from . import views

app_name = 'helpers'

urlpatterns = [
    path('', views.home, name='home'),
    path('helpers/', views.helper_list, name='helper_list'),
    path('helpers/<int:pk>/', views.helper_detail, name='helper_detail'),
    path('get-districts/', views.get_districts, name='get_districts'),
    path('get-upazilas/', views.get_upazilas, name='get_upazilas'),
    path('ajax/districts/', views.ajax_districts, name='ajax_districts'),
    path('ajax/upazilas/', views.ajax_upazilas, name='ajax_upazilas'),
    path('api/nearby-helpers/', views.get_nearby_helpers, name='nearby_helpers'),
]
```

---

### 4. `helpers/choices.py` (254 lines)

```python
DIVISION_CHOICES = [
    ('dhaka', 'ঢাকা'),
    ('chittagong', 'চট্টগ্রাম'),
    ('rajshahi', 'রাজশাহী'),
    ('khulna', 'খুলনা'),
    ('barisal', 'বরিশাল'),
    ('sylhet', 'সিলেট'),
    ('rangpur', 'রংপুর'),
    ('mymensingh', 'ময়মনসিংহ'),
]

DHAKA_DIVISION_DISTRICTS = [
    ('dhaka', 'ঢাকা'), ('faridpur', 'ফরিদপুর'), ('gazipur', 'গাজীপুর'),
    ('gopalganj', 'গোপালগঞ্জ'), ('jamalpur', 'জামালপুর'), ('kishoreganj', 'কিশোরগঞ্জ'),
    ('madaripur', 'মাদারীপুর'), ('manikganj', 'মানিকগঞ্জ'), ('munshiganj', 'মুন্সিগঞ্জ'),
    ('narayanganj', 'নারায়ণগঞ্জ'), ('narsingdi', 'নরসিংদী'), ('netrokona', 'নেত্রকোণা'),
    ('rajbari', 'রাজবাড়ী'), ('shariatpur', 'শরীয়তপুর'), ('sherpur', 'শেরপুর'), ('tangail', 'টাঙ্গাইল'),
]

DHAKA_UPAZILAS = {
    'dhaka': [('dhaka_sadar', 'ঢাকা সদর'), ('savar', 'সাভার'), ('dohar', 'দোহার'), ('keraniganj', 'কেরানীগঞ্জ'), ('nawabganj', 'নবাবগঞ্জ')],
    'faridpur': [('faridpur_sadar', 'ফরিদপুর সদর'), ('bhanga', 'ভাঙ্গা'), ('boalmari', 'বোয়ালমারী'), ('saltha', 'সালথা'), ('charbhadrasan', 'চরভদ্রাসন'), ('madarchar', 'মাদারচর'), ('nagaranda', 'নগরকান্দা'), ('sadarpur', 'সদরপুর'), ('alkhali', 'আলফাডাঙ্গা')],
    'gazipur': [('gazipur_sadar', 'গাজীপুর সদর'), ('tongi', 'টঙ্গী'), ('sreepur', 'শ্রীপুর'), ('kaliganj', 'কালীগঞ্জ'), ('kapasia', 'কাপাসিয়া'), ('kaliakair', 'কালিয়াকৈর')],
    'gopalganj': [('gopalganj_sadar', 'গোপালগঞ্জ সদর'), ('kashiani', 'কাশীয়ানী'), ('tungipara', 'তুংগীপারা'), ('kotalipara', 'কোটালীপাড়া'), ('muksudpur', 'মুকসুদপুর')],
    'jamalpur': [('jamalpur_sadar', 'জামালপুর সদর'), ('melandaha', 'মেলান্দহ'), ('dewanganj', 'দেওয়ানগঞ্জ'), ('bakshiganj', 'বকশীগঞ্জ'), ('islampur', 'ইসলামপুর'), ('madarganj', 'মাদারগঞ্জ'), ('sarishabari', 'সরিষাবাড়ী')],
    'kishoreganj': [('kishoreganj_sadar', 'কিশোরগঞ্জ সদর'), ('hossainpur', 'হোসেনপুর'), ('pakundia', 'পাকুন্দিয়া'), ('katiadi', 'কাটিয়াদী'), ('bhairab', 'ভৈরব'), ('tarail', 'টারাইল'), ('bajitpur', 'বাজিতপুর'), ('mithamain', 'মিঠামইন'), ('nikli', 'নিকলী'), ('kuliarchar', 'কুলিয়ারচর'), ('itna', 'ইটনা'), ('ashtagram', 'অষ্টগ্রাম')],
    'madaripur': [('madaripur_sadar', 'মাদারীপুর সদর'), ('rajoir', 'রাজৈর'), ('kalkini', 'কালকিনি'), ('sibchar', 'শিবচর'), ('dasar', 'ডাসার')],
    'manikganj': [('manikganj_sadar', 'মানিকগঞ্জ সদর'), ('saturia', 'সাটুরিয়া'), ('harirampur', 'হরিরামপুর'), ('ghior', 'ঘিওর'), ('daulatpur', 'দৌলতপুর'), ('singair', 'সিংগাইর'), ('shibalaya', 'শিবালয়')],
    'munshiganj': [('munshiganj_sadar', 'মুন্সিগঞ্জ সদর'), ('sreenagar', 'শ্রীনগর'), ('serajdikhan', 'সিরাজদিখান'), ('lauhajang', 'লৌহজং'), ('gazaria', 'গজারিয়া'), ('tongibari', 'টংগিবাড়ী')],
    'narayanganj': [('narayanganj_sadar', 'নারায়ণগঞ্জ সদর'), ('siddirganj', 'সিদ্ধিরগঞ্জ'), ('araihazar', 'আড়াইহাজার'), ('bandar', 'বন্দর'), ('sonargaon', 'সোনারগাঁও'), ('rupganj', 'রূপগঞ্জ')],
    'narsingdi': [('narsingdi_sadar', 'নরসিংদী সদর'), ('belabo', 'বেলাবো'), ('monohardi', 'মনোহরদী'), ('shibpur', 'শিবপুর'), ('palash', 'পলাশ'), ('raipura', 'রায়পুরা')],
    'netrokona': [('netrokona_sadar', 'নেত্রকোণা সদর'), ('dhobaura', 'ধোবাউড়া'), ('kalmakanda', 'কলমাকান্দা'), ('purbadhala', 'পূর্বধলা'), ('durgapur', 'দুর্গাপুর'), ('kendua', 'কেন্দুয়া'), ('madan', 'মদন'), ('mohanganj', 'মোহনগঞ্জ'), ('atpara', 'আটপাড়া'), ('barhatta', 'বরহাট্টা')],
    'rajbari': [('rajbari_sadar', 'রাজবাড়ী সদর'), ('baliakandi', 'বালিয়াকান্দি'), ('kalukhali', 'কালুখালী'), ('pangsha', 'পাংশা'), ('goalanda', 'গোয়ালন্দ'), ('doulatdia', 'দৌলতদিয়া')],
    'shariatpur': [('shariatpur_sadar', 'শরীয়তপুর সদর'), ('naria', 'নড়িয়া'), ('jajira', 'জাজিরা'), ('bhedarganj', 'ভেদরগঞ্জ'), ('damudhya', 'ডামুড্যা'), ('gosairhat', 'গোসাইরহাট')],
    'sherpur': [('sherpur_sadar', 'শেরপুর সদর'), ('nokla', 'নকলা'), ('sribordi', 'শ্রীবরদী'), ('jhenigati', 'ঝিনাইগাতী')],
    'tangail': [('tangail_sadar', 'টাঙ্গাইল সদর'), ('sakhipur', 'সখিপুর'), ('basail', 'বাসাইল'), ('dhanbari', 'ধানবাড়ী'), ('gopalpur', 'গোপালপুর'), ('madhupur', 'মধুপুর'), ('mirzapur', 'মির্জাপুর'), ('nagarpur', 'নাগরপুর'), ('bhuyapur', 'ভুয়াপুর'), ('kalihati', 'কালিহাতী'), ('delduar', 'দেলদুয়ার')],
}

CHITTAGONG_DIVISION_DISTRICTS = [
    ('bandarban', 'বান্দরবন'), ('brahmanbaria', 'ব্রাহ্মণবাড়ীয়া'), ('chandpur', 'চাঁদপুর'),
    ('chittagong', 'চট্টগ্রাম'), ('comilla', 'কুমিল্লা'), ('cox_bazar', 'কক্সবাজার'),
    ('feni', 'ফেনী'), ('khagrachari', 'খাগড়াছড়ি'), ('lakshmipur', 'লক্ষ্মীপুর'),
    ('noakhali', 'নোয়াখালী'), ('rangamati', 'রাঙ্গামাটি'),
]

CHITTAGONG_UPAZILAS = {
    'chittagong': [('chittagong_sadar', 'চট্টগ্রাম সদর'), ('pahartali', 'পাহাড়তলী'), ('banskali', 'বাঁশখালী'), ('sitakunda', 'সীতাকুণ্ড'), ('rangunia', 'রাঙ্গুনিয়া'), ('hathazari', 'হাটহাজারী'), ('patiya', 'পটিয়া'), ('mirsharai', 'মীরসরাই'), ('anwara', 'আনোয়ারা'), ('sandwip', 'সন্দ্বীপ'), ('boalkhali', 'বোয়ালখালী'), ('fatickchhari', 'ফটিকছড়ি'), ('lohagara', 'লোহাগাড়া'), ('satkania', 'সাতকানিয়া'), ('chandanish', 'চন্দনাইশ')],
    'comilla': [('comilla_sadar', 'কুমিল্লা সদর'), ('chandina', 'চন্দিনা'), ('daudkandi', 'দাউদকান্দি'), ('laksam', 'লাকসাম'), ('nangalkot', 'নাঙ্গলকোট'), ('chaddagram', 'চৌদ্দগ্রাম'), ('burichang', 'বুড়িচং'), ('barura', 'বরুড়া'), ('debidwar', 'দেবীদ্বার'), ('homna', 'হোমনা'), ('mudhafargonj', 'মুরাদনগর'), ('meghna', 'মেঘনা'), ('titas', 'তিতাস'), ('monohargonj', 'মনোহরগঞ্জ')],
    'cox_bazar': [('cox_bazar_sadar', 'কক্সবাজার সদর'), ('ramu', 'রামু'), ('moheshkhali', 'মহেশখালী'), ('chakaria', 'চকরিয়া'), ('ukhiya', 'উখিয়া'), ('teknaf', 'টেকনাফ'), ('kutubdia', 'কুতুবদিয়া'), ('pekarua', 'পেকুয়া')],
    'noakhali': [('noakhali_sadar', 'নোয়াখালী সদর'), ('companiganj', 'কোম্পানীগঞ্জ'), ('begumganj', 'বেগমগঞ্জ'), ('hatiya', 'হাতিয়া'), ('subarnachar', 'সুবর্ণচর'), ('senbagh', 'সেনবাগ'), ('sonaimuri', 'সোনাইমুড়ী'), ('kabirhat', 'কবিরহাট')],
    'feni': [('feni_sadar', 'ফেনী সদর'), ('parshuram', 'পরশুরাম'), ('daganbhuiyan', 'দাগনভূঁইয়া'), ('sonagazi', 'সোনাগাজী'), ('fulgazi', 'ফুলগাজী'), ('chhagalnaiya', 'ছাগলনাইয়া')],
    'brahmanbaria': [('brahmanbaria_sadar', 'ব্রাহ্মণবাড়ীয়া সদর'), ('ashuganj', 'আশুগঞ্জ'), ('nabinagar', 'নবীনগর'), ('sarail', 'সরাইল'), ('bancharampur', 'বাঞ্ছারামপুর'), ('bijoynagar', 'বিজয়নগর'), ('akkhaura', 'আখাউড়া'), ('kasba', 'কসবা'), ('nasirnagar', 'নাসিরনগর')],
    'chandpur': [('chandpur_sadar', 'চাঁদপুর সদর'), ('hajiganj', 'হাজীগঞ্জ'), ('shahrasti', 'শাহরাস্তি'), ('kacharipara', 'কচুয়া'), ('matlab_dakshin', 'মতলব দক্ষিণ'), ('matlab_uttar', 'মতলব উত্তর'), ('faridganj', 'ফরিদগঞ্জ')],
    'bandarban': [('bandarban_sadar', 'বান্দরবন সদর'), ('naikhongchhari', 'নাইক্ষ্যংছড়ি'), ('rowangchhari', 'রোয়াংছড়ি'), ('ruma', 'রুমা'), ('lama', 'লামা'), ('thanchi', 'থানচি'), ('alikadam', 'আলীকদম')],
    'khagrachari': [('khagrachari_sadar', 'খাগড়াছড়ি সদর'), ('dighinala', 'দিঘিনালা'), ('panchhari', 'পানছড়ি'), ('manikchhari', 'মানিকছড়ি'), ('matiranga', 'মাটিরাঙ্গা'), ('ramgarh', 'রামগড়'), ('lakshmichhari', 'লক্ষ্মীছড়ি'), ('mohalchari', 'মহালছড়ি')],
    'lakshmipur': [('lakshmipur_sadar', 'লক্ষ্মীপুর সদর'), ('ramganj', 'রামগঞ্জ'), ('ramgati', 'রামগতি'), ('raipur', 'রায়পুর'), ('kamalnagar', 'কমলনগর')],
    'rangamati': [('rangamati_sadar', 'রাঙ্গামাটি সদর'), ('kaptai', 'কাপ্তাই'), ('kawkhali', 'কাউখালী'), ('baghaichhari', 'বাঘাইছড়ি'), ('barkal', 'বারকাল'), ('langadu', 'লঙ্গাদু'), ('belaichhari', 'বেলাইছড়ি'), ('juraichhari', 'জুরাইছড়ি'), ('naniachar', 'নানিয়ারচর')],
}

RAJSHAHI_DIVISION_DISTRICTS = [
    ('bogra', 'বগুড়া'), ('chapainawabganj', 'চাঁপাইনবাবগঞ্জ'), ('jaipurhat', 'জয়পুরহাট'),
    ('naogaon', 'নওগাঁ'), ('natore', 'নাটোর'), ('pabna', 'পাবনা'),
    ('rajshahi', 'রাজশাহী'), ('sirajganj', 'সিরাজগঞ্জ'),
]

RAJSHAHI_UPAZILAS = {
    'rajshahi': [('rajshahi_sadar', 'রাজশাহী সদর'), ('paba', 'পবা'), ('durgapur', 'দুর্গাপুর'), ('bagmara', 'বাগমারা'), ('mohanpur', 'মোহনপুর'), ('tanore', 'তানোর'), ('godagari', 'গোদাগাড়ী'), ('boalia', 'বোয়ালিয়া'), ('charget', 'চারঘাট'), ('puthia', 'পুঠিয়া'), ('bagha', 'বাঘা')],
    'bogra': [('bogra_sadar', 'বগুড়া সদর'), ('sariakandi', 'সারিয়াকান্দি'), ('shajahanpur', 'শাজাহানপুর'), ('gabtali', 'গাবতলী'), ('sonatala', 'সোনাতলা'), ('dhunat', 'ধুনট'), ('nandigram', 'নন্দীগ্রাম'), ('shibganj', 'শিবগঞ্জ'), ('adamdighi', 'আদমদীঘি'), ('dupunchaniya', 'দুপচাঁচিয়া'), ('kahaloo', 'কাহালু')],
    'pabna': [('pabna_sadar', 'পাবনা সদর'), ('ishwardi', 'ঈশ্বরদী'), ('sujanagar', 'সুজানগর'), ('santhiya', 'সাঁথিয়া'), ('bera', 'বেড়া'), ('bhangura', 'ভাঙ্গুড়া'), ('atgharia', 'আটঘরিয়া'), ('faridpur_pabna', 'ফরিদপুর'), ('chatmohar', 'চাটমোহর')],
    'naogaon': [('naogaon_sadar', 'নওগাঁ সদর'), ('manda', 'মান্দা'), ('niamatpur', 'নিয়ামতপুর'), ('badalgachi', 'বদলগাছী'), ('patnitala', 'পত্নীতলা'), ('dhamoirhat', 'ধামইরহাট'), ('sapahar', 'সাপাহার'), ('porsha', 'পোরশা'), ('raninagar', 'রাণীনগর'), ('mahadevpur', 'মহাদেবপুর'), ('atrakhi', 'আত্রাই')],
    'natore': [('natore_sadar', 'নাটোর সদর'), ('bagatipara', 'বাগাতিপাড়া'), ('baraigram', 'বড়াইগ্রাম'), ('gurudaspur', 'গুরুদাসপুর'), ('lalpur', 'লালপুর'), ('singra', 'সিংড়া'), ('naldu', 'নলডাঙ্গা')],
    'sirajganj': [('sirajganj_sadar', 'সিরাজগঞ্জ সদর'), ('shahjadpur', 'শাহজাদপুর'), ('ullapara', 'উল্লাপাড়া'), ('belkuchi', 'বেলকুচি'), ('kamarkhanda', 'কামারখন্দ'), ('tarash', 'তারাশ'), ('raiganj', 'রায়গঞ্জ'), ('chauhali', 'চৌহালি'), ('kaziipur', 'কাজীপুর')],
    'chapainawabganj': [('chapainawabganj_sadar', 'চাঁপাইনবাবগঞ্জ সদর'), ('gomastapur', 'গোমস্তাপুর'), ('nawabganj_cha', 'নবাবগঞ্জ'), ('shibganj_cha', 'শিবগঞ্জ'), ('bholahat', 'ভোলাহাট')],
    'jaipurhat': [('jaipurhat_sadar', 'জয়পুরহাট সদর'), ('akkela', 'আক্কেলপুর'), ('kalai', 'কালাই'), ('khetlal', 'ক্ষেতলাল'), ('panchbibi', 'পাঁচবিবি')],
}

KHULNA_DIVISION_DISTRICTS = [
    ('bagerhat', 'বাগেরহাট'), ('chuadanga', 'চুয়াডাঙ্গা'), ('jessore', 'যশোর'),
    ('jhenaidah', 'ঝিনাইদহ'), ('khulna', 'খুলনা'), ('kustia', 'কুষ্টিয়া'),
    ('magura', 'মাগুরা'), ('meherpur', 'মেহেরপুর'), ('narail', 'নড়াইল'), ('satkhira', 'সাতক্ষীরা'),
]

KHULNA_UPAZILAS = {
    'khulna': [('khulna_sadar', 'খুলনা সদর'), ('dighalia', 'দিঘলিয়া'), ('phultala', 'ফুলতলা'), ('rupsha', 'রূপসা'), ('terokhada', 'তেরোখাদা'), ('dacope', 'ডাকোপ'), ('paikgacha', 'পাইকগাছা'), ('koyra', 'কয়রা'), ('batiaghata', 'বটিয়াঘাটা'), ('dumuria', 'ডুমুরিয়া')],
    'jessore': [('jessore_sadar', 'যশোর সদর'), ('bagherpara', 'বাঘেরপাড়া'), ('chowgacha', 'চৌগাছা'), ('jhikargacha', 'ঝিকরগাছা'), ('keshabpur', 'কেশবপুর'), ('manirampur', 'মণিরামপুর'), ('sarsha', 'সরশা'), ('abahaynanagar', 'অভয়নগর'), ('shyamnagar', 'শ্যামনগর'), ('kaliganj_jes', 'কালীগঞ্জ')],
    'satkhira': [('satkhira_sadar', 'সাতক্ষীরা সদর'), ('kalaroa', 'কালারোয়া'), ('tala', 'তালা'), ('assassuni', 'আশাশুনি'), ('debhata', 'দেবহাটা'), ('patkelghata', 'পাটকেলঘাটা'), ('shyamnagar_sat', 'শ্যামনগর')],
    'bagerhat': [('bagerhat_sadar', 'বাগেরহাট সদর'), ('fakirhat', 'ফকিরহাট'), ('mollahat', 'মোল্লাহাট'), ('chitalmari', 'চিতলমারী'), ('rampal', 'রামপাল'), ('khuakhali', 'কচুয়া'), ('morrelganj', 'মোড়েলগঞ্জ'), ('sarankhola', 'শরণখোলা'), ('mathbaria', 'মঠবাড়িয়া')],
    'chuadanga': [('chuadanga_sadar', 'চুয়াডাঙ্গা সদর'), ('alamdanga', 'আলমডাঙ্গা'), ('damurhuda', 'দামুড়হুদা'), ('jibannagar', 'জীবননগর')],
    'jhenaidah': [('jhenaidah_sadar', 'ঝিনাইদহ সদর'), ('maheshpur', 'মহেশপুর'), ('kaliganj_jhe', 'কালীগঞ্জ'), ('kotchandpur', 'কোটচাঁদপুর'), ('shailkupa', 'শৈলকুপা'), ('harinakunda', 'হরিণাকুন্ডু')],
    'kustia': [('kustia_sadar', 'কুষ্টিয়া সদর'), ('kumarkhali', 'কুমারখালী'), ('khoksa', 'খোকসা'), ('mirpur', 'মিরপুর'), ('daulatpur_kus', 'দৌলতপুর'), ('vheramara', 'ভেড়ামারা')],
    'magura': [('magura_sadar', 'মাগুরা সদর'), ('shalikha', 'শালিখা'), ('sreepur_mag', 'শ্রীপুর'), ('mohammadpur_mag', 'মহম্মদপুর')],
    'meherpur': [('meherpur_sadar', 'মেহেরপুর সদর'), ('mujibnagar', 'মুজিবনগর'), ('gangni', 'গাংনী')],
    'narail': [('narail_sadar', 'নড়াইল সদর'), ('lohagara_nar', 'লোহাগড়া'), ('kalia_nar', 'কালিয়া')],
}

BARISAL_DIVISION_DISTRICTS = [
    ('barguna', 'বরগুনা'), ('barisal', 'বরিশাল'), ('bhola', 'ভোলা'),
    ('jhalokati', 'ঝালকাঠী'), ('patuakhali', 'পটুয়াখালী'), ('pirojpur', 'পিরোজপুর'),
]

BARISAL_UPAZILAS = {
    'barisal': [('barisal_sadar', 'বরিশাল সদর'), ('bakerganj', 'বাকেরগঞ্জ'), ('gournadi', 'গৌরনদী'), ('babuganj', 'বাবুগঞ্জ'), ('wazirpur', 'ওয়াজিরপুর'), ('muladi', 'মুলাদী'), ('hizla', 'হিজলা'), ('barisal_mehendiganj', 'মেহেন্দিগঞ্জ'), ('banaripara', 'বানারীপাড়া'), ('agaijhara', 'আগৈলঝারা')],
    'bhola': [('bhola_sadar', 'ভোলা সদর'), ('char_fassion', 'চরফ্যাশন'), ('monpura', 'মনপুরা'), ('lalmohan', 'লালমোহন'), ('tazumuddin', 'তজুমুদ্দিন'), ('borhanuddin', 'বোরহানউদ্দিন'), ('daulatkhan', 'দৌলতখান')],
    'barguna': [('barguna_sadar', 'বরগুনা সদর'), ('amtali', 'আমতলী'), ('bamna', 'বামনা'), ('betagi', 'বেতাগী'), ('patharghata', 'পাথরঘাটা')],
    'jhalokati': [('jhalokati_sadar', 'ঝালকাঠী সদর'), ('natchole', 'নাচোল'), ('kathalia', 'কাঠালিয়া'), ('rajapur_jha', 'রাজাপুর')],
    'patuakhali': [('patuakhali_sadar', 'পটুয়াখালী সদর'), ('bauphal', 'বাউফল'), ('dashmina', 'দশমিনা'), ('galachipa', 'গলাচিপা'), ('kalapara', 'কলাপাড়া'), ('mirzaganj', 'মির্জাগঞ্জ'), ('dumki', 'ডুমকি'), ('rangabali', 'রাঙ্গাবালী')],
    'pirojpur': [('pirojpur_sadar', 'পিরোজপুর সদর'), ('mothbaria', 'মঠবাড়িয়া'), ('nazirpur', 'নাজিরপুর'), ('bhandaria', 'ভাণ্ডারিয়া'), ('zianagar', 'জিয়ানগর'), ('nazirpur_pir', 'নেছারাবাদ'), ('kawkhali_pir', 'কাউখালী')],
}

SYLHET_DIVISION_DISTRICTS = [
    ('habiganj', 'হবিগঞ্জ'), ('moulvibazar', 'মৌলভীবাজার'), ('sunamganj', 'সুনামগঞ্জ'), ('sylhet', 'সিলেট'),
]

SYLHET_UPAZILAS = {
    'sylhet': [('sylhet_sadar', 'সিলেট সদর'), ('balaganj', 'বালাগঞ্জ'), ('beanibazar', 'বিয়ানীবাজার'), ('golapganj', 'গোলাপগঞ্জ'), ('jaintiapur', 'জৈন্তাপুর'), ('kanajghat', 'কানাইঘাট'), ('southern_surma', 'দক্ষিণ সুরমা'), ('fenchuganj', 'ফেঞ্চুগঞ্জ'), ('bishwanath', 'বিশ্বনাথ'), ('zakiganj', 'জকিগঞ্জ'), ('companyganj_syl', 'কোম্পানীগঞ্জ'), ('gowainghat', 'গোয়াইনঘাট')],
    'moulvibazar': [('moulvibazar_sadar', 'মৌলভীবাজার সদর'), ('sreemangal', 'শ্রীমঙ্গল'), ('kamalganj', 'কমলগঞ্জ'), ('rajnagar', 'রাজনগর'), ('kulaora', 'কুলাউড়া'), ('baralekha', 'বড়লেখা'), ('juri', 'জুড়ী')],
    'habiganj': [('habiganj_sadar', 'হবিগঞ্জ সদর'), ('nabiganj', 'নবীগঞ্জ'), ('bahubal', 'বাহুবল'), ('ajmiriganj', 'আজমিরীগঞ্জ'), ('baniachang', 'বানিয়াচং'), ('lakhai', 'লাখাই'), ('chunarughat', 'চুনারুঘাট'), ('madhabpur', 'মাধবপুর')],
    'sunamganj': [('sunamganj_sadar', 'সুনামগঞ্জ সদর'), ('dharamapasha', 'ধর্মপাশা'), ('jamalganj', 'জামালগঞ্জ'), ('sullah', 'শাল্লা'), ('derai', 'দিরাই'), ('chhatak', 'ছাতক'), ('dowarabazar', 'দোয়ারাবাজার'), ('tahirpur', 'তাহিরপুর'), ('bishambharpur', 'বিশম্ভরপুর')],
}

RANGPUR_DIVISION_DISTRICTS = [
    ('dinajpur', 'দিনাজপুর'), ('gaibandha', 'গাইবান্ধা'), ('kurigram', 'কুড়িগ্রাম'),
    ('lalmonirhat', 'লালমনিরহাট'), ('nilphamari', 'নীলফামারী'), ('panchagarh', 'পঞ্চগড়'),
    ('rangpur', 'রংপুর'), ('thakurgaon', 'ঠাকুরগাঁও'),
]

RANGPUR_UPAZILAS = {
    'rangpur': [('rangpur_sadar', 'রংপুর সদর'), ('badarganj', 'বদরগঞ্জ'), ('gangachara', 'গঙ্গাচরা'), ('taraganj', 'তারাগঞ্জ'), ('kaunia', 'কাউনিয়া'), ('porsha_rang', 'পোরশা'), ('mithapukur', 'মিঠাপুকুর'), ('pirgacha', 'পীরগাছা'), ('pirsadar', 'পীরগঞ্জ')],
    'dinajpur': [('dinajpur_sadar', 'দিনাজপুর সদর'), ('birganj', 'বীরগঞ্জ'), ('parbatipur', 'পার্বতীপুর'), ('biral', 'বিরল'), ('bochaganj', 'বোচাগঞ্জ'), ('kaharole', 'কাহারোল'), ('phulbari', 'ফুলবাড়ী'), ('nawabganj_din', 'নবাবগঞ্জ'), ('ghoraghat', 'ঘোড়াঘাট'), ('hili', 'হিলি'), ('birampur', 'বিরামপুর'), ('hoksa_din', 'খানসামা'), ('chirirbandar', 'চিরিরবন্দর')],
    'gaibandha': [('gaibandha_sadar', 'গাইবান্ধা সদর'), ('sadullahpur', 'সাদুল্লাপুর'), ('saghata', 'সাঘাটা'), ('gobindaganj', 'গোবিন্দগঞ্জ'), ('sunatganj', 'সুন্দরগঞ্জ'), ('pulbari_gai', 'পলাশবাড়ী')],
    'kurigram': [('kurigram_sadar', 'কুড়িগ্রাম সদর'), ('nageshwari', 'নাগেশ্বরী'), ('bhurungamari', 'ভুরুঙ্গামারী'), ('phulbari_kur', 'ফুলবাড়ী'), ('rajarhat', 'রাজারহাট'), ('ulipur', 'উলিপুর'), ('chilmari', 'চিলমারী'), ('rowmari', 'রৌমারী'), ('maynaguri', 'ময়নাগুড়ি')],
    'lalmonirhat': [('lalmonirhat_sadar', 'লালমনিরহাট সদর'), ('patgram', 'পাটগ্রাম'), ('hatibandha', 'হাতীবান্ধা'), ('kaliganj_lal', 'কালীগঞ্জ'), ('aditmari', 'আদিতমারী')],
    'nilphamari': [('nilphamari_sadar', 'নীলফামারী সদর'), ('saidpur', 'সৈয়দপুর'), ('dimla', 'ডিমলা'), ('domar', 'ডোমার'), ('kishoreganj_nil', 'কিশোরগঞ্জ'), ('jaldhaka', 'জলঢাকা')],
    'panchagarh': [('panchagarh_sadar', 'পঞ্চগড় সদর'), ('debiganj', 'দেবীগঞ্জ'), ('tetulia', 'তেতুলিয়া'), ('bochaganj_pan', 'বোদা'), ('atwari', 'আটোয়ারী')],
    'thakurgaon': [('thakurgaon_sadar', 'ঠাকুরগাঁও সদর'), ('baliadangi', 'বালিয়াডাঙ্গি'), ('haripur', 'হরিপুর'), ('ranisankail', 'রাণীশংকৈল'), ('pirganj', 'পীরগঞ্জ')],
}

MYMENSINGH_DIVISION_DISTRICTS = [
    ('jamalpur', 'জামালপুর'), ('mymensingh', 'ময়মনসিংহ'), ('netrokona', 'নেত্রকোণা'), ('sherpur', 'শেরপুর'),
]

MYMENSINGH_UPAZILAS = {
    'mymensingh': [('mymensingh_sadar', 'ময়মনসিংহ সদর'), ('fulpur', 'ফুলপুর'), ('muktagacha', 'মুক্তাগাছা'), ('trishal', 'ত্রিশাল'), ('gouripur', 'গৌরীপুর'), ('ishwarganj', 'ঈশ্বরগঞ্জ'), ('halueaghat', 'হালুয়াঘাট'), ('nandail', 'নান্দাইল'), ('phulbaria_mym', 'ফুলবাড়িয়া'), ('bhaluka', 'ভালুকা'), ('tarakanda', 'তারাকান্দা'), ('dhobaura_mym', 'ধোবাউড়া')],
}

DISTRICT_CHOICES = (
    DHAKA_DIVISION_DISTRICTS +
    CHITTAGONG_DIVISION_DISTRICTS +
    RAJSHAHI_DIVISION_DISTRICTS +
    KHULNA_DIVISION_DISTRICTS +
    BARISAL_DIVISION_DISTRICTS +
    SYLHET_DIVISION_DISTRICTS +
    RANGPUR_DIVISION_DISTRICTS +
    MYMENSINGH_DIVISION_DISTRICTS
)

UPAZILA_CHOICES = []
for upazila_dict in [DHAKA_UPAZILAS, CHITTAGONG_UPAZILAS, RAJSHAHI_UPAZILAS, KHULNA_UPAZILAS, BARISAL_UPAZILAS, SYLHET_UPAZILAS, RANGPUR_UPAZILAS, MYMENSINGH_UPAZILAS]:
    for district_upazilas in upazila_dict.values():
        UPAZILA_CHOICES.extend(district_upazilas)

PLACE_TYPE_CHOICES = [
    ('village', 'গ্রাম'), ('city', 'শহর'), ('area', 'এলাকা'),
    ('mohalla', 'মহল্লা'), ('para', 'পাড়া'), ('ward', 'ওয়ার্ড'), ('union', 'ইউনিয়ন'),
]

SERVICE_TYPE_CHOICES = [
    ('cooking', 'রান্না করা'),
    ('cleaning', 'ঘর পরিষ্কার'),
    ('childcare', 'শিশু পরিচর্যা'),
    ('elderly_care', 'বৃদ্ধ সেবা'),
    ('gardening', 'বাগান করা'),
    ('car_washing', 'গাড়ি ধোয়া'),
    ('laundry', 'কাপড় ধোয়া'),
    ('shopping', 'বাজার করা'),
    ('babysitting', 'বেবিসিটিং'),
    ('caregiver', 'কেয়ারগিভার'),
    ('plumber', 'প্লাম্বার'),
    ('electrician', 'ইলেকট্রিশিয়ান'),
    ('carpenter', 'ছুতার'),
    ('painter', 'পেন্টার'),
    ('welder', 'ওয়েল্ডার'),
    ('mason', 'রাজমিস্ত্রি'),
    ('driver', 'ড্রাইভার'),
    ('security_guard', 'সিকিউরিটি গার্ড'),
    ('office_assistant', 'অফিস সহায়ক'),
    ('delivery_man', 'ডেলিভারি ম্যান'),
    ('tailor', 'দর্জি'),
    ('beautician', 'বিউটিশিয়ান'),
    ('masseur', 'ম্যাসিউর'),
    ('nurse', 'নার্স'),
    ('physiotherapist', 'ফিজিওথেরাপিস্ট'),
    ('tutor', 'টিউটর'),
    ('event_worker', 'ইভেন্ট ওয়ার্কার'),
    ('pest_control', 'পেস্ট কন্ট্রোল'),
    ('moving_help', 'মুভিং হেল্প'),
    ('pet_care', 'পোষ্য পরিচর্যা'),
    ('home_repair', 'বাড়ি মেরামত'),
    ('ac_technician', 'এসি টেকনিশিয়ান'),
    ('generator_tech', 'জেনারেটর টেকনিশিয়ান'),
    ('computer_repair', 'কম্পিউটার মেরামত'),
    ('mobile_repair', 'মোবাইল মেরামত'),
]

AVAILABILITY_CHOICES = [
    ('available', 'উপলব্ধ'), ('busy', 'ব্যস্ত'), ('unavailable', 'অনুপলব্ধ'),
]

HIRING_STATUS_CHOICES = [
    ('pending', 'অপেক্ষমাণ'), ('active', 'সক্রিয়'),
    ('completed', 'সম্পন্ন'), ('cancelled', 'বাতিল'),
]

ACCOUNT_TYPE_CHOICES = [
    ('user', 'সাধারণ ব্যবহারকারী'), ('helper', 'হেল্পার'),
]

SERVICE_TYPE_ICONS = {
    'cooking': '🍳', 'cleaning': '🧹', 'childcare': '👶', 'elderly_care': '👴',
    'gardening': '🌱', 'car_washing': '🚗', 'laundry': '👕', 'shopping': '🛒',
    'babysitting': '🍼', 'caregiver': '🤝', 'plumber': '🔧', 'electrician': '⚡',
    'carpenter': '🪚', 'painter': '🎨', 'welder': '🔥', 'mason': '🧱',
    'driver': '🚙', 'security_guard': '🛡️', 'office_assistant': '📋', 'delivery_man': '📦',
    'tailor': '✂️', 'beautician': '💄', 'masseur': '💆', 'nurse': '🏥',
    'physiotherapist': '🦴', 'tutor': '📚', 'event_worker': '🎪', 'pest_control': '🐜',
    'moving_help': '📦', 'pet_care': '🐾', 'home_repair': '🔨', 'ac_technician': '❄️',
    'generator_tech': '⚙️', 'computer_repair': '💻', 'mobile_repair': '📱',
}

SERVICE_CATEGORIES = [
    ('domestic', 'গৃহস্থালি সেবা', ['cooking', 'cleaning', 'laundry', 'shopping', 'gardening', 'car_washing']),
    ('care', 'যত্ন সেবা', ['childcare', 'elderly_care', 'babysitting', 'caregiver', 'pet_care']),
    ('repair', 'মেরামত সেবা', ['plumber', 'electrician', 'carpenter', 'painter', 'welder', 'mason', 'home_repair', 'ac_technician', 'generator_tech', 'computer_repair', 'mobile_repair']),
    ('professional', 'পেশাদার সেবা', ['driver', 'security_guard', 'office_assistant', 'delivery_man', 'tailor', 'beautician', 'masseur', 'nurse', 'physiotherapist', 'tutor', 'event_worker', 'pest_control', 'moving_help']),
]


def get_districts_by_division(division_code):
    district_map = {
        'dhaka': DHAKA_DIVISION_DISTRICTS,
        'chittagong': CHITTAGONG_DIVISION_DISTRICTS,
        'rajshahi': RAJSHAHI_DIVISION_DISTRICTS,
        'khulna': KHULNA_DIVISION_DISTRICTS,
        'barisal': BARISAL_DIVISION_DISTRICTS,
        'sylhet': SYLHET_DIVISION_DISTRICTS,
        'rangpur': RANGPUR_DIVISION_DISTRICTS,
        'mymensingh': MYMENSINGH_DIVISION_DISTRICTS,
    }
    return district_map.get(division_code, [])


def get_upazilas_by_district(district_code):
    all_upazilas = {**DHAKA_UPAZILAS, **CHITTAGONG_UPAZILAS, **RAJSHAHI_UPAZILAS, **KHULNA_UPAZILAS, **BARISAL_UPAZILAS, **SYLHET_UPAZILAS, **RANGPUR_UPAZILAS, **MYMENSINGH_UPAZILAS}
    return all_upazilas.get(district_code, [])
```

---

### 5. `helpers/admin.py` (3 lines)

```python
from django.contrib import admin

# Helper profiles are managed in accounts app admin
```
</task_result>
</task>
```

**Tool: task**

**Input:**
```json
{
  "description": "Read hirings app files",
  "prompt": "Read the following files completely and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\hirings\\models.py\n2. C:\\Users\\ASUS\\ArkHelps\\hirings\\views.py\n3. C:\\Users\\ASUS\\ArkHelps\\hirings\\urls.py\n4. C:\\Users\\ASUS\\ArkHelps\\hirings\\forms.py\n5. C:\\Users\\ASUS\\ArkHelps\\hirings\\admin.py\n\nReturn all file contents with their paths clearly marked.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_168d5a0caffeqVtmtTKMWzbh2m" state="completed">
<task_result>
Here are the full contents of all requested files:

---

### `hirings/models.py` (40 lines)
```python
from django.db import models
from django.conf import settings
from accounts.models import UserProfile, HelperProfile
from helpers.choices import HIRING_STATUS_CHOICES


class Hiring(models.Model):
    """User-helper hiring relationship"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hirings')
    helper = models.ForeignKey(HelperProfile, on_delete=models.CASCADE, related_name='hirings')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=HIRING_STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, help_text="Additional notes for the hiring")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.user.get_full_name()} - {self.helper.user_profile.user.get_full_name()} ({self.get_status_display()})"

    def can_review(self):
        """Check if the user can submit a review for this hiring"""
        return self.status == 'completed'


class Review(models.Model):
    """User reviews for helpers"""
    hiring = models.OneToOneField(Hiring, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.hiring.user.user.get_full_name()} for {self.hiring.helper.user_profile.user.get_full_name()}"
```

---

### `hirings/views.py` (197 lines)
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from accounts.models import UserProfile, HelperProfile
from hirings.models import Hiring, Review


@login_required
def create_hiring(request, helper_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    helper = get_object_or_404(HelperProfile, pk=helper_id)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        notes = request.POST.get('notes', '')

        hiring = Hiring.objects.create(
            user=user_profile,
            helper=helper,
            start_date=start_date,
            notes=notes,
            status='pending'
        )

        helper.availability_status = 'busy'
        helper.save()

        messages.success(request, 'হায়ার রিকোয়েস্ট পাঠানো হয়েছে!')
        return redirect('hirings:my_hirings')

    context = {
        'helper': helper,
    }
    return render(request, 'hirings/create_hiring.html', context)


@login_required
def my_hirings(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    status_filter = request.GET.get('status', '')

    if profile.account_type == 'helper':
        helper_profile = profile.helper_profile
        hirings = helper_profile.hirings.all()
    else:
        hirings = profile.hirings.all()

    if status_filter:
        hirings = hirings.filter(status=status_filter)

    context = {
        'hirings': hirings,
        'current_status': status_filter,
    }
    return render(request, 'hirings/my_hirings.html', context)


@login_required
def submit_review(request, hiring_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    hiring = get_object_or_404(Hiring, pk=hiring_id, user=user_profile)

    if hiring.status != 'completed':
        messages.error(request, 'শুধুমাত্র সম্পন্ন হায়ারিং এর জন্য রিভিউ দেওয়া যায়।')
        return redirect('hirings:my_hirings')

    if hasattr(hiring, 'review'):
        messages.error(request, 'আপনি ইতিমধ্যে এই হায়ারিং এর জন্য রিভিউ দিয়েছেন।')
        return redirect('hirings:my_hirings')

    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        comment = request.POST.get('comment', '')

        if rating < 1 or rating > 5:
            messages.error(request, 'রেটিং ১-৫ এর মধ্যে হতে হবে।')
            return render(request, 'hirings/submit_review.html', {'hiring': hiring})

        Review.objects.create(
            hiring=hiring,
            rating=rating,
            comment=comment
        )

        helper = hiring.helper
        reviews = Review.objects.filter(hiring__helper=helper)
        from django.db.models import Avg
        avg = reviews.aggregate(Avg('rating'))['rating__avg']
        helper.average_rating = round(avg, 2) if avg else 0
        helper.total_reviews = reviews.count()
        helper.save()

        messages.success(request, 'আপনার রিভিউ সফলভাবে জমা দেওয়া হয়েছে!')
        return redirect('hirings:my_hirings')

    return render(request, 'hirings/submit_review.html', {'hiring': hiring})


@login_required
def cancel_hiring(request, hiring_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    hiring = get_object_or_404(Hiring, pk=hiring_id)

    is_helper = (user_profile.account_type == 'helper'
                 and hasattr(user_profile, 'helper_profile')
                 and hiring.helper == user_profile.helper_profile)

    if hiring.user != user_profile and not is_helper:
        messages.error(request, 'আপনি এই হায়ারিং বাতিল করতে পারবেন না।')
        return redirect('hirings:my_hirings')

    if hiring.status != 'pending':
        messages.error(request, 'শুধুমাত্র অপেক্ষমাণ হায়ারিং বাতিল করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'cancelled'
    hiring.save()

    helper = hiring.helper
    if not helper.hirings.filter(status='active').exists():
        helper.availability_status = 'available'
        helper.save()

    messages.success(request, 'হায়ারিং বাতিল করা হয়েছে।')
    return redirect('hirings:my_hirings')


@login_required
def accept_hiring(request, hiring_id):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if profile.account_type != 'helper' or not hasattr(profile, 'helper_profile'):
        messages.error(request, 'শুধুমাত্র হেল্পাররা হায়ারিং গ্রহণ করতে পারেন।')
        return redirect('hirings:my_hirings')

    hiring = get_object_or_404(Hiring, pk=hiring_id, helper=profile.helper_profile)

    if hiring.status != 'pending':
        messages.error(request, 'শুধুমাত্র অপেক্ষমাণ হায়ারিং গ্রহণ করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'active'
    hiring.save()

    messages.success(request, 'হায়ারিং রিকোয়েস্ট গ্রহণ করা হয়েছে!')
    return redirect('hirings:my_hirings')


@login_required
def complete_hiring(request, hiring_id):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if profile.account_type != 'helper' or not hasattr(profile, 'helper_profile'):
        messages.error(request, 'শুধুমাত্র হেল্পাররা হায়ারিং সম্পন্ন করতে পারেন।')
        return redirect('hirings:my_hirings')

    hiring = get_object_or_404(Hiring, pk=hiring_id, helper=profile.helper_profile)

    if hiring.status != 'active':
        messages.error(request, 'শুধুমাত্র সক্রিয় হায়ারিং সম্পন্ন করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'completed'
    from datetime import date
    hiring.end_date = date.today()
    hiring.save()

    helper = hiring.helper
    if not helper.hirings.filter(status='active').exists():
        helper.availability_status = 'available'
        helper.save()

    messages.success(request, 'হায়ারিং সম্পন্ন হিসাবে চিহ্নিত করা হয়েছে!')
    return redirect('hirings:my_hirings')
```

---

### `hirings/urls.py` (13 lines)
```python
from django.urls import path
from . import views

app_name = 'hirings'

urlpatterns = [
    path('hire/<int:helper_id>/', views.create_hiring, name='create_hiring'),
    path('my-hirings/', views.my_hirings, name='my_hirings'),
    path('hirings/<int:hiring_id>/review/', views.submit_review, name='submit_review'),
    path('hirings/<int:hiring_id>/cancel/', views.cancel_hiring, name='cancel_hiring'),
    path('hirings/<int:hiring_id>/accept/', views.accept_hiring, name='accept_hiring'),
    path('hirings/<int:hiring_id>/complete/', views.complete_hiring, name='complete_hiring'),
]
```

---

### `hirings/admin.py` (31 lines)
```python
from django.contrib import admin
from hirings.models import Hiring, Review


@admin.register(Hiring)
class HiringAdmin(admin.ModelAdmin):
    list_display = ('user', 'helper', 'start_date', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__user__username', 'helper__user_profile__user__username', 'notes')
    list_editable = ('status',)
    actions = ['mark_completed', 'mark_active', 'mark_cancelled']

    def mark_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_completed.short_description = 'সম্পন্ন হিসেবে চিহ্নিত করুন'

    def mark_active(self, request, queryset):
        queryset.update(status='active')
    mark_active.short_description = 'সক্রিয় হিসেবে চিহ্নিত করুন'

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
    mark_cancelled.short_description = 'বাতিল হিসেবে চিহ্নিত করুন'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hiring', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('hiring__user__user__username', 'hiring__helper__user_profile__user__username', 'comment')
    readonly_fields = ('created_at',)
```

---

### `hirings/forms.py`
**File does not exist** — `C:\Users\ASUS\ArkHelps\hirings\forms.py` was not found. This app doesn't use Django forms; all form handling is done via raw `request.POST` in the views.
</task_result>
</task>
```

**Tool: task**

**Input:**
```json
{
  "description": "Read ads + core project files",
  "prompt": "Read the following files completely and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\ads\\models.py\n2. C:\\Users\\ASUS\\ArkHelps\\ads\\views.py\n3. C:\\Users\\ASUS\\ArkHelps\\ads\\urls.py\n4. C:\\Users\\ASUS\\ArkHelps\\ads\\admin.py\n5. C:\\Users\\ASUS\\ArkHelps\\helphands\\settings.py\n6. C:\\Users\\ASUS\\ArkHelps\\helphands\\urls.py\n7. C:\\Users\\ASUS\\ArkHelps\\requirements.txt\n\nReturn all file contents with their paths clearly marked.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_168d59be5ffevBeQhYiYKUSDZn" state="completed">
<task_result>
Here are the full contents of all requested files:

---

### `C:\Users\ASUS\ArkHelps\ads\models.py` (126 lines)

```python
from django.db import models


class Ad(models.Model):
    """Advertisement model for managing ads across the site"""

    AD_TYPES = [
        ('popup', 'পপআপ'),
        ('banner', 'ব্যানার'),
        ('sidebar', 'সাইডবার'),
        ('inline', 'ইনলাইন'),
    ]

    AD_POSITIONS = [
        ('home_hero', 'হোম হিরো (শীর্ষে)'),
        ('home_bottom', 'হোম নিচে'),
        ('helpers_top', 'হেল্পার তালিকা শীর্ষে'),
        ('helpers_bottom', 'হেল্পার তালিকা নিচে'),
        ('detail_top', 'হেল্পার বিবরণ শীর্ষে'),
        ('detail_bottom', 'হেল্পার বিবরণ নিচে'),
        ('footer', 'ফুটারে'),
    ]

    AD_PLACEMENT = [
        ('all', 'সব জায়গায়'),
        ('home', 'শুধু হোম পেজ'),
        ('helpers', 'হেল্পার পেজ'),
        ('detail', 'হেল্পার বিবরণ পেজ'),
    ]

    name = models.CharField(max_length=100, verbose_name='এড নাম')
    ad_type = models.CharField(max_length=20, choices=AD_TYPES, default='banner')
    placement = models.CharField(max_length=20, choices=AD_PLACEMENT, default='all')
    position = models.CharField(max_length=30, choices=AD_POSITIONS, default='home_bottom')

    # Ad content
    title = models.CharField(max_length=200, blank=True, verbose_name='শিরোনাম')
    description = models.TextField(blank=True, verbose_name='বিবরণ')
    image = models.ImageField(upload_to='ads/images/', blank=True, null=True, verbose_name='ছবি')
    video = models.FileField(upload_to='ads/videos/', blank=True, null=True, verbose_name='ভিডিও (mp4/webm)')
    video_url = models.URLField(blank=True, verbose_name='ভিডিও URL (YouTube/Vimeo)')
    redirect_url = models.URLField(blank=True, verbose_name='রিডিরেক্ট লিংক')

    # Ad settings
    is_active = models.BooleanField(default=True, verbose_name='সক্রিয়')
    show_close_button = models.BooleanField(default=True, verbose_name='ক্লোজ বাটন দেখাবে')
    auto_close_seconds = models.PositiveIntegerField(default=10, verbose_name='অটো ক্লোজ (সেকেন্ড)', help_text='0 = ক্লোজ হবে না')

    # Scheduling
    start_date = models.DateTimeField(null=True, blank=True, verbose_name='শুরু তারিখ')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='শেষ তারিখ')
    impressions_limit = models.PositiveIntegerField(null=True, blank=True, verbose_name='ইম্প্রেশন লিমিট', help_text='কতবার দেখানো হবে')
    impressions_count = models.PositiveIntegerField(default=0, verbose_name='বর্তমান ইম্প্রেশন')

    # Display settings
    priority = models.PositiveIntegerField(default=1, verbose_name='প্রায়োরিটি (উচ্চ = আগে দেখাবে)')
    display_duration = models.PositiveIntegerField(default=0, verbose_name='প্রদর্শন সময় (সেকেন্ড)', help_text='0 = সবসময় দেখাবে')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', '-created_at']
        verbose_name = 'বিজ্ঞাপন'
        verbose_name_plural = 'বিজ্ঞাপন'

    def __str__(self):
        return self.name

    @property
    def has_video(self):
        return bool(self.video or self.video_url)

    @property
    def can_show(self):
        """Check if ad can be displayed"""
        if not self.is_active:
            return False

        # Check impressions limit
        if self.impressions_limit and self.impressions_count >= self.impressions_limit:
            return False

        # Check date range
        from django.utils import timezone
        now = timezone.now()

        if self.start_date and now < self.start_date:
            return False

        if self.end_date and now > self.end_date:
            return False

        return True


class AdClick(models.Model):
    """Track ad clicks"""
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=500, blank=True)
    clicked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-clicked_at']
        verbose_name = 'এড ক্লিক'
        verbose_name_plural = 'এড ক্লিক'

    def __str__(self):
        return f"{self.ad.name} - {self.clicked_at}"


class AdImpression(models.Model):
    """Track ad impressions"""
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='impressions')
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=40, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewed_at']
        verbose_name = 'এড ইম্প্রেশন'
        verbose_name_plural = 'এড ইম্প্রেশন'

    def __str__(self):
        return f"{self.ad.name} - {self.viewed_at}"
```

---

### `C:\Users\ASUS\ArkHelps\ads\views.py` (80 lines)

```python
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
```

---

### `C:\Users\ASUS\ArkHelps\ads\urls.py` (9 lines)

```python
from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('track/impression/<int:ad_id>/', views.track_impression, name='track_impression'),
    path('track/click/<int:ad_id>/', views.track_click, name='track_click'),
]
```

---

### `C:\Users\ASUS\ArkHelps\ads\admin.py` (44 lines)

```python
from django.contrib import admin
from ads.models import Ad, AdClick, AdImpression


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'ad_type', 'placement', 'position', 'is_active', 'priority', 'impressions_count', 'created_at')
    list_filter = ('ad_type', 'placement', 'is_active', 'position', 'created_at')
    search_fields = ('name', 'title', 'description')
    list_editable = ('is_active', 'priority')
    readonly_fields = ('impressions_count', 'created_at', 'updated_at')

    fieldsets = (
        ('সাধারণ তথ্য', {'fields': ('name', 'ad_type', 'placement', 'position', 'is_active', 'priority')}),
        ('বিজ্ঞাপন বিষয়বস্তু', {'fields': ('title', 'description', 'image', 'video', 'video_url', 'redirect_url')}),
        ('সেটিংস', {'fields': ('show_close_button', 'auto_close_seconds', 'display_duration')}),
        ('সময়সূচী ও সীমা', {'fields': ('start_date', 'end_date', 'impressions_limit', 'impressions_count')}),
    )

    actions = ['activate_ads', 'deactivate_ads']

    def activate_ads(self, request, queryset):
        queryset.update(is_active=True)
    activate_ads.short_description = 'সক্রিয় করুন'

    def deactivate_ads(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_ads.short_description = 'নিষ্ক্রিয় করুন'


@admin.register(AdClick)
class AdClickAdmin(admin.ModelAdmin):
    list_display = ('ad', 'ip_address', 'clicked_at')
    list_filter = ('clicked_at', 'ad')
    search_fields = ('ad__name', 'ip_address')
    readonly_fields = ('clicked_at',)


@admin.register(AdImpression)
class AdImpressionAdmin(admin.ModelAdmin):
    list_display = ('ad', 'ip_address', 'viewed_at')
    list_filter = ('viewed_at', 'ad')
    search_fields = ('ad__name', 'ip_address')
    readonly_fields = ('viewed_at',)
```

---

### `C:\Users\ASUS\ArkHelps\helphands\settings.py` (215 lines)

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key-change-in-production')

DEBUG_RAW = os.getenv('DEBUG', 'True')
DEBUG = DEBUG_RAW.lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

SITE_URL = os.getenv('SITE_URL', 'http://localhost:8000')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'anymail',
    'pwa',
    'storages',

    'accounts',
    'helpers',
    'hirings',
    'ads',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helphands.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'helphands.context_processors.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'helphands.wsgi.application'

DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL:
    import dj_database_url
    DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'bn'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0
WHITENOISE_MIMETYPES = {'.svg': 'image/svg+xml'}

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_REGION_NAME = 'us-east-005'
AWS_S3_ENDPOINT_URL = f'https://s3.{AWS_S3_REGION_NAME}.backblazeb2.com'
AWS_QUERYSTRING_AUTH = True

if AWS_STORAGE_BUCKET_NAME:
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.backblazeb2.com/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage" if AWS_STORAGE_BUCKET_NAME else "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}

ANYMAIL = {
    "RESEND_API_KEY": os.getenv('RESEND_API_KEY', ''),
}

EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'HelpHands <onboarding@resend.dev>')

SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/dashboard/'
LOGOUT_REDIRECT_URL = '/'

JAZZMIN_SETTINGS = {
    'site_title': 'HelpHands Admin',
    'site_header': 'HelpHands Admin',
    'site_brand': 'HelpHands',
    'welcome_sign': 'হেল্পহ্যান্ডস অ্যাডমিন প্যানেলে স্বাগতম',
    "show_sidebar": True,
    "order_with_respect_to": ["auth"],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "navbar_variant": "navbar-dark",
    "theme": "cosmo",
    "dark_mode_theme": "darkly",
}

PWA_APP_NAME = 'HelpHands'
PWA_APP_DESCRIPTION = "বিশ্বস্ত কাজের লোক খুঁজুন সহজেই"
PWA_APP_THEME_COLOR = '#1a6b3c'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [{'src': '/static/img/logo.png', 'sizes': '160x160'}]
PWA_APP_ICONS_APPLE = [{'src': '/static/img/logo.png', 'sizes': '160x160'}]
PWA_APP_SPLASH_SCREEN = [
    {'src': '/static/img/logo.png', 'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'bn-BD'
PWA_APP_SHORTCUTS = []
PWA_APP_SCREENSHOTS = [{'src': '/static/img/logo.png', 'sizes': '750x1334', 'type': 'image/png'}]
PWA_SERVICE_WORKER_PATH = BASE_DIR / 'sw.js'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

ENABLE_ADMIN_SITEMAP = True

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

AUTH_USER_MODEL = 'accounts.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

### `C:\Users\ASUS\ArkHelps\helphands\urls.py` (28 lines)

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView, TemplateView
from pwa.views import manifest, service_worker

from helphands.sitemap import section_sitemaps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helpers.urls')),
    path('accounts/', include('accounts.urls')),
    path('hirings/', include('hirings.urls')),
    path('ads/', include('ads.urls')),
    path('manifest.json', manifest, name='pwa-manifest'),
    path('sw.js', service_worker, name='pwa-service-worker'),
    path('sitemap.xml', sitemap, {'sitemap_urls': section_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('llms.txt', RedirectView.as_view(url='/static/llms.txt', permanent=False), name='llms_txt'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('terms/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
    path('privacy/', TemplateView.as_view(template_name='pages/privacy.html'), name='privacy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

### `C:\Users\ASUS\ArkHelps\requirements.txt` (12 lines)

```
django
django-jazzmin
django-pwa
django-storages[s3]
django-anymail
boto3
whitenoise
dj-database-url
pillow
psycopg2-binary
python-dotenv
django-allauth
```

All 7 files returned in full.
</task_result>
</task>
```

**Tool: task**

**Input:**
```json
{
  "description": "Read templates and static structure",
  "prompt": "Explore the following files/directories and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\templates\\ - list the full directory tree\n2. Read the base template: C:\\Users\\ASUS\\ArkHelps\\templates\\base.html (full content)\n3. C:\\Users\\ASUS\\ArkHelps\\static\\ - list the full directory tree\n4. Read the home page template: C:\\Users\\ASUS\\ArkHelps\\templates\\home.html (full content)\n5. Read the helper_list template: C:\\Users\\ASUS\\ArkHelps\\templates\\helper_list.html\n6. C:\\Users\\ASUS\\ArkHelps\\manage.py\n7. C:\\Users\\ASUS\\ArkHelps\\.env.example\n\nReturn all file contents with their paths clearly marked.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_168d59531ffe2BCo250vehRZY4" state="completed">
<task_result>
Here are the full contents of all requested files:

---

## 1. Templates Directory Tree

```
templates/
├── accounts/
│   ├── edit_helper_profile.html
│   ├── edit_profile.html
│   ├── helper_dashboard.html
│   ├── login.html
│   ├── signup.html
│   └── user_dashboard.html
├── ads/
│   └── ad_display.html
├── emails/
│   └── verification.html
├── helpers/
│   ├── helper_detail.html
│   ├── helper_list.html
│   └── home.html
├── hirings/
│   ├── create_hiring.html
│   ├── my_hirings.html
│   └── submit_review.html
├── pages/
│   ├── about.html
│   ├── privacy.html
│   └── terms.html
├── base.html
```

---

## 2. Static Directory Tree

```
static/
├── css/
│   └── style.css
├── img/
│   └── logo.svg
├── js/
│   └── main.js
└── llms.txt
```

---

## 3. `templates/base.html` (245 lines)

```html
<!DOCTYPE html>
{% load static %}
{% load ad_tags %}
<html lang="bn" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="description" content="{% block meta_description %}HelpHands (হেল্পহ্যান্ডস) - বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার খুঁজে পাওয়ার প্ল্যাটফর্ম। রান্না, পরিষ্কার, শিশু পরিচর্যা, বৃদ্ধ সেবা, প্লাম্বার, ইলেকট্রিশিয়ান সহ সকল ধরনের সেবা।{% endblock %}">
    <meta name="keywords" content="হেল্পার, কাজের লোক, ডোমেস্টিক হেল্পার, বাংলাদেশ, রান্নাকারী, ঘর পরিষ্কার, শিশু পরিচর্যা, বৃদ্ধ সেবা, প্লাম্বার, ইলেকট্রিশিয়ান, বেবিসিটার, কেয়ারগিভার">
    <meta name="author" content="HelpHands">
    <meta name="geo.region" content="BD">
    <meta name="geo.placename" content="Bangladesh">
    <link rel="canonical" href="{% block canonical_url %}{{ request.build_absolute_uri }}{% endblock %}">

    <meta property="og:type" content="{% block og_type %}website{% endblock %}">
    <meta property="og:url" content="{{ request.build_absolute_uri }}">
    <meta property="og:title" content="{% block og_title %}HelpHands (হেল্পহ্যান্ডস) - বিশ্বস্ত হেল্পার খুঁজুন সহজেই{% endblock %}">
    <meta property="og:description" content="{% block og_description %}বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম। রিভিউ ও রেটিং দেখে সঠিক হেল্পার খুঁজে পান।{% endblock %}">
    <meta property="og:image" content="{% block og_image %}{% static 'img/logo.svg' %}{% endblock %}">
    <meta property="og:locale" content="bn_BD">
    <meta property="og:site_name" content="HelpHands হেল্পহ্যান্ডস">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{% block twitter_title %}HelpHands - বিশ্বস্ত হেল্পার খুঁজুন সহজেই{% endblock %}">
    <meta name="twitter:description" content="{% block twitter_description %}বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম।{% endblock %}">
    <meta name="twitter:image" content="{% block twitter_image %}{% static 'img/logo.svg' %}{% endblock %}">

    <title>{% block title %}HelpHands (হেল্পহ্যান্ডস){% endblock %}</title>

    <link rel="manifest" href="{% url 'pwa-manifest' %}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Bengali:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@300;400;500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">

    <link rel="icon" type="image/svg+xml" href="{% static 'img/logo.svg' %}">
    <link rel="apple-touch-icon" href="{% static 'img/logo.svg' %}">
    <link rel="preload" href="{% static 'css/style.css' %}" as="style">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    {% block extra_css %}{% endblock %}

    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "HelpHands হেল্পহ্যান্ডস",
        "alternateName": "HelpHands",
        "url": "{{ site_url|default:'https://www.helphands.com' }}",
        "logo": "{{ site_url|default:'https://www.helphands.com' }}{% static 'img/logo.svg' %}",
        "description": "বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম",
        "areaServed": {"@type": "Country", "name": "Bangladesh"},
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "customer service",
            "email": "{{ contact_email|default:'info@helphands.com' }}",
            "areaServed": "BD",
            "availableLanguage": ["Bengali", "English"]
        }
    }
    </script>
    {% block faq_schema %}{% endblock %}
    {% block breadcrumb_schema %}{% endblock %}
    {% block service_schema %}{% endblock %}
</head>
<body>
    {% get_popup_ads as popup_ads %}
    {% if popup_ads %}
    {% for ad in popup_ads %}
    <div class="ad-popup" id="adPopup{{ ad.id }}" style="display:none;">
        <div class="ad-popup-overlay" onclick="closeAd({{ ad.id }})"></div>
        <div class="ad-popup-content">
            {% if ad.show_close_button %}
            <button class="ad-popup-close" onclick="closeAd({{ ad.id }})">&times;</button>
            {% endif %}
            <a href="#" onclick="trackAdClick({{ ad.id }}); return false;">
                {% if ad.has_video %}
                    {% if ad.video %}
                    <video autoplay muted loop playsinline class="ad-video">
                        <source src="{{ ad.video.url }}" type="video/mp4">
                    </video>
                    {% elif ad.video_url %}
                    <iframe src="{{ ad.video_url }}" frameborder="0" allowfullscreen></iframe>
                    {% endif %}
                {% elif ad.image %}
                <img src="{{ ad.image.url }}" alt="{{ ad.title }}" class="ad-image">
                {% endif %}
                {% if ad.title %}<h3 class="ad-title">{{ ad.title }}</h3>{% endif %}
                {% if ad.description %}<p class="ad-description">{{ ad.description }}</p>{% endif %}
            </a>
        </div>
    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            var p = document.getElementById('adPopup{{ ad.id }}');
            if (p) { p.style.display = 'flex'; p.style.animation = 'adFadeIn 0.4s ease'; }
        }, 1500);
    });
    </script>
    {% endfor %}
    {% endif %}

    <nav class="navbar" id="navbar">
        <div class="container navbar-container">
            <a href="{% url 'helpers:home' %}" class="navbar-brand">
                <img src="{% static 'img/logo.svg' %}" alt="HelpHands" class="navbar-logo">
                <span class="navbar-brand-text">হেল্পহ্যান্ডস</span>
            </a>

            <button class="navbar-toggle" id="navbarToggle" aria-label="মেনু">
                <span></span><span></span><span></span>
            </button>

            <div class="navbar-menu" id="navbarMenu">
                <a href="{% url 'helpers:helper_list' %}" class="nav-link">হেল্পার খুঁজুন</a>
                <a href="{% url 'about' %}" class="nav-link">আমাদের সম্পর্কে</a>
                {% if user.is_authenticated %}
                    <a href="{% url 'accounts:dashboard' %}" class="nav-link">ড্যাশবোর্ড</a>
                    {% if user.profile.account_type == 'helper' %}
                    <a href="{% url 'hirings:my_hirings' %}" class="nav-link">আমার হায়ারিং</a>
                    {% endif %}
                    <div class="navbar-left-actions">
                        <a href="{% url 'accounts:edit_profile' %}" class="notification-badge" aria-label="নোটিফিকেশন" title="নোটিফিকেশন">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
                        </a>
                        <form method="post" action="{% url 'accounts:logout' %}" class="nav-form" style="display:inline;">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-outline btn-sm">লগআউট</button>
                        </form>
                    </div>
                {% else %}
                    <a href="{% url 'accounts:login' %}" class="nav-link">লগইন</a>
                    <a href="{% url 'accounts:signup' %}" class="btn btn-primary btn-sm">নিবন্ধন</a>
                {% endif %}
                <button class="theme-toggle" id="themeToggle" aria-label="থিম">🌙</button>
            </div>
        </div>
    </nav>

    {% if messages %}
    <div class="messages-container">
        {% for message in messages %}
        <div class="message message-{{ message.tags }}">
            <span>{{ message }}</span>
            <button class="message-close" onclick="this.parentElement.remove()">&times;</button>
        </div>
        {% endfor %}
    </div>
    {% endif %}

    {% block sos_banner %}{% endblock %}

    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <a href="#" class="back-to-top" id="backToTop" aria-label="উপরে যান">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>
    </a>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-section">
                    <h3 class="footer-title">হেল্পহ্যান্ডস</h3>
                    <p class="footer-text">বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম। আমরা দেশের মানুষের জন্য তৈরি করেছি একটি নির্ভরযোগ্য সেবা।</p>
                </div>
                <div class="footer-section">
                    <h4 class="footer-subtitle">দ্রুত লিংক</h4>
                    <ul class="footer-links">
                        <li><a href="{% url 'helpers:helper_list' %}">হেল্পার খুঁজুন</a></li>
                        <li><a href="{% url 'about' %}">আমাদের সম্পর্কে</a></li>
                        <li><a href="{% url 'accounts:signup' %}">নিবন্ধন করুন</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 class="footer-subtitle">আইনি</h4>
                    <ul class="footer-links">
                        <li><a href="{% url 'terms' %}">শর্তাবলী</a></li>
                        <li><a href="{% url 'privacy' %}">গোপনীয়তা নীতি</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 class="footer-subtitle">যোগাযোগ</h4>
                    <ul class="footer-links">
                        <li>ইমেইল: {{ contact_email|default:'info@helphands.com' }}</li>
                        <li>ফোন: {{ contact_phone|default:'+৮৮০ ১XXX-XXXXXX' }}</li>
                        <li>ঢাকা, বাংলাদেশ</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; ২০২৬ হেল্পহ্যান্ডস। সর্বস্বত্ব সংরক্ষিত। দেশের জন্য আমাদের এই ছোট প্রয়াস।</p>
            </div>
        </div>
    </footer>

    <script src="{% static 'js/main.js' %}"></script>

    <style>
    .ad-popup{position:fixed;top:0;left:0;right:0;bottom:0;z-index:9999;display:none;align-items:center;justify-content:center}
    .ad-popup-overlay{position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.7);backdrop-filter:blur(4px)}
    .ad-popup-content{position:relative;max-width:90%;max-height:90vh;background:white;border-radius:20px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.3)}
    @keyframes adFadeIn{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
    .ad-popup-close{position:absolute;top:12px;right:12px;background:rgba(0,0,0,.5);color:white;border:none;width:36px;height:36px;border-radius:50%;font-size:22px;cursor:pointer;z-index:10;display:flex;align-items:center;justify-content:center;transition:all .2s}
    .ad-popup-close:hover{background:rgba(0,0,0,.8);transform:rotate(90deg)}
    .ad-popup-content img,.ad-popup-content video{display:block;max-width:100%;max-height:60vh;width:auto;height:auto;margin:0 auto}
    .ad-title{padding:16px 20px 0;margin:0;font-size:1.2rem;text-align:center;color:#2c2416}
    .ad-description{padding:8px 20px 20px;text-align:center;color:#7a6f5d}
    .back-to-top{position:fixed;bottom:24px;left:24px;z-index:5000;width:44px;height:44px;border-radius:50%;background:var(--primary);color:white;border:none;display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow-lg);cursor:pointer;opacity:0;visibility:hidden;transform:scale(.8);transition:all .3s ease}
    .back-to-top.visible{opacity:1;visibility:visible;transform:scale(1)}
    .back-to-top:hover{transform:scale(1.1) translateY(-3px);background:var(--primary-dark)}
    @keyframes adFadeOut{from{opacity:1;transform:scale(1)}to{opacity:0;transform:scale(.9)}}
    </style>

    <script>
    function closeAd(id){var p=document.getElementById('adPopup'+id);if(p){p.style.animation='adFadeOut 0.3s ease forwards';p.addEventListener('animationend',function(){p.style.display='none'},{once:true})}}
    function trackAdClick(id){
        fetch('/ads/track/click/'+id+'/',{method:'POST',headers:{'X-CSRFToken':'{{ csrf_token }}'}})
        .then(function(r){return r.json()}).then(function(d){if(d.redirect)window.location.href=d.redirect})
    }

    document.addEventListener('DOMContentLoaded', function() {
        var toggle = document.getElementById('themeToggle');
        if (toggle) {
            toggle.addEventListener('click', function() {
                var html = document.documentElement;
                var isDark = html.getAttribute('data-theme') === 'dark';
                html.setAttribute('data-theme', isDark ? 'light' : 'dark');
                try { localStorage.setItem('theme', isDark ? 'light' : 'dark'); } catch(e) {}
            });
        }
        var stored = null;
        try { stored = localStorage.getItem('theme'); } catch(e) {}
        if (stored === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        }
    });
    </script>

    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 4. `templates/helpers/home.html` (299 lines)

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}হেল্পহ্যান্ডস - বিশ্বস্ত হেল্পার খুঁজুন সহজেই | HelpHands{% endblock %}

{% block meta_description %}হেল্পহ্যান্ডস - বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম। রান্না, ঘর পরিষ্কার, শিশু পরিচর্যা, বৃদ্ধ সেবা, প্লাম্বার, ইলেকট্রিশিয়ান, বেবিসিটার, কেয়ারগিভার সহ সকল ধরনের সেবা। রিভিউ ও রেটিং দেখে সঠিক হেল্পার খুঁজে পান।{% endblock %}

{% block canonical_url %}{% url 'helpers:home' %}{% endblock %}

{% block og_title %}হেল্পহ্যান্ডস - বিশ্বস্ত হেল্পার খুঁজুন{% endblock %}
{% block og_description %}বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম। ৩৫+ সেবা, ৮ বিভাগ, রিভিউ ও রেটিং।{% endblock %}

{% block faq_schema %}
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type":"Question","name":"হেল্পহ্যান্ডস কী?","acceptedAnswer":{"@type":"Answer","text":"হেল্পহ্যান্ডস বাংলাদেশের সবচেয়ে বিশ্বস্ত হেল্পার প্ল্যাটফর্ম। আমরা পরিবার, অফিস ও প্রতিষ্ঠানের জন্য যাচাইকৃত হেল্পার, প্লাম্বার, ইলেকট্রিশিয়ান, বেবিসিটার, কেয়ারগিভার সহ সকল ধরনের সেবা প্রদানকারীদের সাথে সংযুক্ত করি।"}},
        {"@type":"Question","name":"কী ধরনের হেল্পার পাওয়া যায়?","acceptedAnswer":{"@type":"Answer","text":"আমাদের প্ল্যাটফর্মে রান্নাকারী, ঘর পরিষ্কারকারী, শিশু পরিচর্যাকারী, বৃদ্ধ সেবাকারী, বেবিসিটার, কেয়ারগিভার, প্লাম্বার, ইলেকট্রিশিয়ান, ছুতার, পেন্টার, ড্রাইভার, সিকিউরিটি গার্ড, টিউটর, নার্স সহ ৩৫+ ধরনের সেবা প্রদানকারী পাওয়া যায়।"}},
        {"@type":"Question","name":"হেল্পার কীভাবে নিয়োগ করব?","acceptedAnswer":{"@type":"Answer","text":"প্রথমে নিবন্ধন করুন, তারপর আপনার প্রয়োজন অনুযায়ী ফিল্টার করে হেল্পার বেছে নিন, রিভিউ পড়ুন এবং হায়ার রিকোয়েস্ট পাঠান।"}},
        {"@type":"Question","name":"হেল্পার ভেরিফাইড কিনা কীভাবে বুঝব?","acceptedAnswer":{"@type":"Answer","text":"ভেরিফাইড হেল্পারদের প্রোফাইলে 'অ্যাডমিন ভেরিফাইড' ব্যাজ থাকে। তাদের এনআইডি ও পরিচয় যাচাই করা হয়েছে।"}}
    ]
}
</script>
{% endblock %}

{% block content %}
<section class="hero">
    <div class="container">
        <div class="hero-content">
            <span class="hero-badge">🇧🇩 বাংলাদেশের বিশ্বস্ত প্ল্যাটফর্ম</span>
            <h1 class="hero-title">আপনার প্রয়োজনীয় <span class="text-accent">হেল্পার</span> খুঁজুন</h1>
            <p class="hero-subtitle">রান্না, পরিষ্কার, শিশু পরিচর্যা, বৃদ্ধ সেবা, প্লাম্বার, ইলেকট্রিশিয়ান, বেবিসিটার, ড্রাইভার সহ ৩৫+ ধরনের সেবা। রিভিউ ও রেটিং দেখে সঠিক পছন্দ করুন।</p>

            <div class="hero-search-alt">
                <button class="use-location-btn" id="useLocationBtn" onclick="detectLocation()">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="3"/><path d="M12 2v4m0 12v4m10-10h-4M6 12H2m17.07-7.07l-2.83 2.83M7.76 16.24l-2.83 2.83M19.07 19.07l-2.83-2.83M7.76 7.76L4.93 4.93"/></svg>
                    আমার অবস্থান ব্যবহার করুন
                </button>
                <form action="{% url 'helpers:helper_list' %}" method="get" class="hero-search-form">
                    <div class="search-row">
                        <div class="search-field">
                            <label>বিভাগ</label>
                            <select name="division">
                                <option value="">সব বিভাগ</option>
                                {% for code, name in divisions %}
                                <option value="{{ code }}">{{ name }}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="search-field">
                            <label>সেবার ধরন</label>
                            <select name="service_type">
                                <option value="">সব সেবা</option>
                                {% for code, name in service_types %}
                                <option value="{{ code }}">{{ name }}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <button type="submit" class="btn btn-accent btn-lg search-btn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                            খুঁজুন
                        </button>
                    </div>
                </form>
            </div>

            <div class="hero-stats">
                <div class="hero-stat">
                    <span class="hero-stat-value">{{ total_helpers|default:"০" }}+</span>
                    <span class="hero-stat-label">নিবন্ধিত হেল্পার</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-value">{{ total_services|default:"৩৫" }}+</span>
                    <span class="hero-stat-label">সেবার ধরন</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-value">৮</span>
                    <span class="hero-stat-label">বিভাগ জুড়ে</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-value">৪.৫+</span>
                    <span class="hero-stat-label">গড় রেটিং</span>
                </div>
            </div>
        </div>
    </div>
</section>

<div class="container" style="margin-top:24px">
    <div class="sos-banner reveal">
        <div class="sos-banner-content">
            <div class="sos-icon">🆘</div>
            <div class="sos-text">
                <strong>জরুরি হেল্পার দরকার?</strong>
                <span>এখনই খুঁজুন আপনার কাছের হেল্পার</span>
            </div>
        </div>
        <a href="{% url 'helpers:helper_list' %}?availability=available" class="sos-btn">খুঁজুন</a>
    </div>
</div>

{% if featured_helpers %}
<section class="section reveal">
    <div class="container">
        <div class="section-title">
            <h2>জনপ্রিয় হেল্পার</h2>
            <p>সবচেয়ে বেশি রেটিং প্রাপ্ত হেল্পারগণ</p>
        </div>
        <div class="helper-grid">
            {% for helper in featured_helpers %}
            <a href="{% url 'helpers:helper_detail' helper.pk %}" class="helper-card-link">
                <article class="helper-card-modern gradient-border-card">
                    <div class="helper-card-img">
                        {% if helper.user_profile.profile_photo %}
                        <img src="{{ helper.user_profile.profile_photo.url }}" alt="{{ helper.user_profile.user.get_full_name }}" loading="lazy">
                        {% else %}
                        <div class="helper-card-avatar-modern">
                            <span>{{ helper.user_profile.user.get_initials|default:"হ" }}</span>
                        </div>
                        {% endif %}
                        {% if helper.is_verified_by_admin %}
                        <span class="verified-badge" title="ভেরিফাইড">✓</span>
                        {% endif %}
                        <span class="helper-status {{ helper.availability_status }}">{{ helper.get_availability_status_display }}</span>
                        <button class="favorite-btn fav-btn" data-helper-id="{{ helper.pk }}" onclick="event.stopPropagation();event.preventDefault();" aria-label="ফেভারিট">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                        </button>
                    </div>
                    <div class="helper-card-body">
                        <h3>{{ helper.user_profile.user.get_full_name }}</h3>
                        <p class="helper-location">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            {{ helper.user_profile.get_district_display|default:helper.user_profile.get_division_display }}
                        </p>
                        <div class="helper-tags">
                            {% for service in helper.get_display_services|slice:":3" %}
                            <span class="tag">{{ service }}</span>
                            {% endfor %}
                        </div>
                        <div class="helper-footer-info">
                            <div class="helper-rating">
                                <span class="stars">{% for i in "12345" %}{% if forloop.counter <= helper.average_rating|default:0|floatformat:0|add:0 %}★{% else %}☆{% endif %}{% endfor %}</span>
                                <span class="rating-num">{{ helper.average_rating|default:"0.0" }}</span>
                                <span class="review-count">({{ helper.total_reviews }})</span>
                            </div>
                            <div class="helper-price">
                                {% if helper.monthly_rate %}{{ helper.monthly_rate }}৳<small>/মাস</small>
                                {% elif helper.hourly_rate %}{{ helper.hourly_rate }}৳<small>/ঘণ্টা</small>{% endif %}
                            </div>
                        </div>
                    </div>
                </article>
            </a>
            {% endfor %}
        </div>
        <div class="section-cta">
            <a href="{% url 'helpers:helper_list' %}" class="btn btn-outline btn-lg">
                সব হেল্পার দেখুন
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
        </div>
    </div>
</section>
{% endif %}

<section class="section section-alt services-premium-section reveal">
    <div class="container">
        <div class="section-title">
            <span class="section-badge">আমাদের সেবাসমূহ</span>
            <h2>সকল <span class="text-accent">সেবা</span></h2>
            <p>গৃহস্থালি থেকে শুরু করে পেশাদার সেবা — ৩৫+ ধরনের সেবা এক প্ল্যাটফর্মে</p>
        </div>

        {% for category, cat_name, services in service_categories %}
        <div class="service-premium-category reveal">
            <div class="category-premium-header">
                <h3 class="category-premium-title">{{ cat_name }}</h3>
                <span class="category-premium-count">{{ services|length }} টি সেবা</span>
            </div>
            <div class="services-premium-grid">
                {% for code, name in service_types %}
                    {% if code in services %}
                    <a href="{% url 'helpers:helper_list' %}?service_type={{ code }}" class="service-premium-card">
                        <div class="service-premium-icon-wrap">
                            <span class="service-premium-icon">
                                {% if code == 'cooking' %}🍳
                                {% elif code == 'cleaning' %}🧹
                                {% elif code == 'childcare' %}👶
                                {% elif code == 'elderly_care' %}👴
                                {% elif code == 'gardening' %}🌱
                                {% elif code == 'car_washing' %}🚗
                                {% elif code == 'laundry' %}👕
                                {% elif code == 'shopping' %}🛒
                                {% elif code == 'babysitting' %}🍼
                                {% elif code == 'caregiver' %}🤝
                                {% elif code == 'plumber' %}🔧
                                {% elif code == 'electrician' %}⚡
                                {% elif code == 'carpenter' %}🪚
                                {% elif code == 'painter' %}🎨
                                {% elif code == 'welder' %}🔥
                                {% elif code == 'mason' %}🧱
                                {% elif code == 'driver' %}🚙
                                {% elif code == 'security_guard' %}🛡️
                                {% elif code == 'office_assistant' %}📋
                                {% elif code == 'delivery_man' %}📦
                                {% elif code == 'tailor' %}✂️
                                {% elif code == 'beautician' %}💄
                                {% elif code == 'masseur' %}💆
                                {% elif code == 'nurse' %}🏥
                                {% elif code == 'physiotherapist' %}🦴
                                {% elif code == 'tutor' %}📚
                                {% elif code == 'event_worker' %}🎪
                                {% elif code == 'pest_control' %}🐜
                                {% elif code == 'moving_help' %}📦
                                {% elif code == 'pet_care' %}🐾
                                {% elif code == 'home_repair' %}🔨
                                {% elif code == 'ac_technician' %}❄️
                                {% elif code == 'generator_tech' %}⚙️
                                {% elif code == 'computer_repair' %}💻
                                {% elif code == 'mobile_repair' %}📱
                                {% else %}🔧
                                {% endif %}
                            </span>
                        </div>
                        <span class="service-premium-name">{{ name }}</span>
                        <span class="service-premium-arrow">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                        </span>
                    </a>
                    {% endif %}
                {% endfor %}
            </div>
        </div>
        {% endfor %}
    </div>
</section>

<section class="section reveal">
    <div class="container">
        <div class="info-cards">
            <div class="info-card">
                <div class="info-icon">🛡️</div>
                <h3>যাচাইকৃত প্রোফাইল</h3>
                <p>প্রত্যেক হেল্পারের পরিচয় ও এনআইডি যাচাই করা হয়</p>
            </div>
            <div class="info-card">
                <div class="info-icon">⭐</div>
                <h3>রিভিউ ও রেটিং</h3>
                <p>আসল ব্যবহারকারীদের রিভিউ দেখে সঠিক পছন্দ করুন</p>
            </div>
            <div class="info-card">
                <div class="info-icon">💬</div>
                <h3>সহজ যোগাযোগ</h3>
                <p>সরাসরি হেল্পারের সাথে যোগাযোগ করে নিয়োগ দিন</p>
            </div>
            <div class="info-card">
                <div class="info-icon">🔒</div>
                <h3>নিরাপদ ও ব্যক্তিগত</h3>
                <p>আপনার তথ্য সুরক্ষিত, প্রযোজন ছাড়া ফোন নম্বর দেখানো হয় না</p>
            </div>
        </div>
    </div>
</section>

<section class="cta-section reveal">
    <div class="container">
        <h2>আপনি কি হেল্পার?</h2>
        <p>আমাদের প্ল্যাটফর্মে নিবন্ধন করুন এবং কাজ খুঁজুন। সম্পূর্ণ বিনামূল্যে।</p>
        <a href="{% url 'accounts:signup' %}?account_type=helper" class="btn btn-accent btn-lg">হেল্পার হিসেবে নিবন্ধন করুন</a>
    </div>
</section>

<script>
function detectLocation() {
    var btn = document.getElementById('useLocationBtn');
    btn.innerHTML = 'অবস্থান খোঁজা হচ্ছে...';
    btn.disabled = true;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(pos) {
                window.location.href = '{% url "helpers:helper_list" %}?lat=' + pos.coords.latitude + '&lng=' + pos.coords.longitude;
            },
            function(err) {
                btn.innerHTML = 'অবস্থান পাওয়া যায়নি';
                btn.disabled = false;
                setTimeout(function() {
                    btn.innerHTML = 'আমার অবস্থান ব্যবহার করুন';
                }, 2000);
            }
        );
    } else {
        btn.innerHTML = 'জিওলোকেশন সমর্থিত নয়';
        btn.disabled = false;
    }
}
</script>
{% endblock %}
```

---

## 5. `templates/helpers/helper_list.html` (215 lines)

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}হেল্পার তালিকা - বাংলাদেশের হেল্পার খুঁজুন | HelpHands{% endblock %}

{% block meta_description %}বাংলাদেশের সকল বিভাগে হেল্পার খুঁজুন। রান্নাকারী, ঘর পরিষ্কারকারী, শিশু পরিচর্যাকারী, প্লাম্বার, ইলেকট্রিশিয়ান, বেবিসিটার, কেয়ারগিভার সহ সকল ধরনের সেবা প্রদানকারী। রিভিউ ও রেটিং দেখে সঠিক পছন্দ করুন।{% endblock %}

{% block canonical_url %}{% url 'helpers:helper_list' %}{% endblock %}

{% block og_title %}হেল্পার তালিকা - হেল্পহ্যান্ডস{% endblock %}
{% block og_description %}বাংলাদেশের সকল বিভাগে হেল্পার খুঁজুন।{% endblock %}

{% block content %}
<div class="list-page">
    <div class="container">
        <div class="list-header">
            <div>
                <h1>হেল্পার খুঁজুন</h1>
                {% if helpers %}<p class="results-count">{{ page_obj.paginator.count }} জন হেল্পার পাওয়া গেছে</p>{% endif %}
            </div>
            <button class="filter-toggle-btn" id="filterToggle" onclick="toggleFilters()">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="6" x2="20" y2="6"/><line x1="8" y1="12" x2="20" y2="12"/><line x1="12" y1="18" x2="20" y2="18"/></svg>
                ফিল্টার
            </button>
        </div>

        <div class="layout-with-sidebar">
            <aside class="filter-sidebar" id="filterPanel">
                <div class="filter-header">
                    <h3>ফিল্টার</h3>
                    <button class="filter-close" onclick="toggleFilters()">&times;</button>
                </div>
                <form method="get" class="filter-form" id="filterForm">
                    <input type="hidden" name="lat" id="filterLat" value="{{ selected_lat|default:'' }}">
                    <input type="hidden" name="lng" id="filterLng" value="{{ selected_lng|default:'' }}">

                    {% if selected_lat and selected_lng %}
                    <div class="filter-notice">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v4m0 12v4m10-10h-4M6 12H2"/></svg>
                        আপনার অবস্থানের কাছাকাছি হেল্পার দেখানো হচ্ছে
                        <a href="{% url 'helpers:helper_list' %}" class="clear-location">সরান</a>
                    </div>
                    {% endif %}

                    <div class="filter-group">
                        <label>বিভাগ</label>
                        <select name="division" class="filter-select">
                            <option value="">সব বিভাগ</option>
                            {% for code, name in divisions %}
                            <option value="{{ code }}" {% if selected_division == code %}selected{% endif %}>{{ name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>জেলা</label>
                        <select name="district" class="filter-select">
                            <option value="">সব জেলা</option>
                            {% for code, name in districts %}
                            <option value="{{ code }}" {% if selected_district == code %}selected{% endif %}>{{ name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>উপজেলা/থানা</label>
                        <select name="upazila" id="upazilaSelect" class="filter-select">
                            <option value="">সব উপজেলা</option>
                            {% for code, name in upazilas %}
                            <option value="{{ code }}" {% if selected_upazila == code %}selected{% endif %}>{{ name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>স্থানের ধরন</label>
                        <select name="place_type" class="filter-select">
                            <option value="">সব ধরন</option>
                            {% for code, name in place_types %}
                            <option value="{{ code }}" {% if selected_place_type == code %}selected{% endif %}>{{ name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>সেবার ধরন</label>
                        <select name="service_type" class="filter-select">
                            <option value="">সব সেবা</option>
                            {% for code, name in service_types %}
                            <option value="{{ code }}" {% if selected_service == code %}selected{% endif %}>{{ name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>ন্যূনতম রেটিং</label>
                        <select name="min_rating" class="filter-select">
                            <option value="">সব রেটিং</option>
                            <option value="4" {% if selected_min_rating == "4" %}selected{% endif %}>৪+ ⭐</option>
                            <option value="3" {% if selected_min_rating == "3" %}selected{% endif %}>৩+ ⭐</option>
                            <option value="2" {% if selected_min_rating == "2" %}selected{% endif %}>২+ ⭐</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>সর্বোচ্চ মজুরি</label>
                        <select name="max_rate" class="filter-select">
                            <option value="">যে কোনো মূল্য</option>
                            <option value="5000" {% if selected_max_rate == "5000" %}selected{% endif %}>৫,০০০৳ এর নিচে</option>
                            <option value="10000" {% if selected_max_rate == "10000" %}selected{% endif %}>১০,০০০৳ এর নিচে</option>
                            <option value="20000" {% if selected_max_rate == "20000" %}selected{% endif %}>২০,০০০৳ এর নিচে</option>
                            <option value="50000" {% if selected_max_rate == "50000" %}selected{% endif %}>৫০,০০০৳ এর নিচে</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>উপলব্ধতা</label>
                        <select name="availability" class="filter-select">
                            <option value="">সব</option>
                            <option value="available" {% if selected_availability == "available" %}selected{% endif %}>Available</option>
                            <option value="busy" {% if selected_availability == "busy" %}selected{% endif %}>Busy</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <label>খুঁজুন</label>
                        <input type="text" name="search" class="filter-input" placeholder="নাম বা অবস্থান..." value="{{ selected_search|default:'' }}">
                    </div>

                    <button type="submit" class="btn btn-primary" style="width:100%">ফিল্টার করুন</button>
                    <a href="{% url 'helpers:helper_list' %}" class="btn btn-outline btn-sm" style="width:100%;margin-top:8px;text-align:center">রিসেট</a>
                </form>
            </aside>

            <div class="results-area">
                {% if helpers %}
                <div class="helper-grid-results">
                    {% for helper in helpers %}
                    <a href="{% url 'helpers:helper_detail' helper.pk %}" class="helper-card-link">
                        <article class="helper-card-modern gradient-border-card">
                            <div class="helper-card-img">
                                {% if helper.user_profile.profile_photo %}
                                <img src="{{ helper.user_profile.profile_photo.url }}" alt="{{ helper.user_profile.user.get_full_name }}" loading="lazy">
                                {% else %}
                                <div class="helper-card-avatar-modern">
                                    <span>{{ helper.user_profile.user.get_initials|default:"হ" }}</span>
                                </div>
                                {% endif %}
                                {% if helper.is_verified_by_admin %}
                                <span class="verified-badge" title="ভেরিফাইড">✓</span>
                                {% endif %}
                                <span class="helper-status {{ helper.availability_status }}">{{ helper.get_availability_status_display }}</span>
                                <button class="favorite-btn fav-btn" data-helper-id="{{ helper.pk }}" onclick="event.stopPropagation();event.preventDefault();" aria-label="ফেভারিট">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                                </button>
                            </div>
                            <div class="helper-card-body">
                                <h3>{{ helper.user_profile.user.get_full_name }}</h3>
                                <p class="helper-location">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                                    {{ helper.user_profile.get_district_display|default:helper.user_profile.get_division_display }}
                                    {% if helper.user_profile.get_upazila_display %} - {{ helper.user_profile.get_upazila_display }}{% endif %}
                                </p>
                                <div class="helper-tags">
                                    {% for service in helper.get_display_services|slice:":3" %}
                                    <span class="tag">{{ service }}</span>
                                    {% endfor %}
                                </div>
                                <div class="helper-footer-info">
                                    <div class="helper-rating">
                                        <span class="stars">{% for i in "12345" %}{% if forloop.counter <= helper.average_rating|default:0|floatformat:0|add:0 %}★{% else %}☆{% endif %}{% endfor %}</span>
                                        <span class="rating-num">{{ helper.average_rating|default:"0.0" }}</span>
                                    </div>
                                    <div class="helper-price">
                                        {% if helper.monthly_rate %}{{ helper.monthly_rate }}৳<small>/মাস</small>
                                        {% elif helper.hourly_rate %}{{ helper.hourly_rate }}৳<small>/ঘণ্টা</small>{% endif %}
                                    </div>
                                </div>
                            </div>
                        </article>
                    </a>
                    {% endfor %}
                </div>

                {% if page_obj.has_other_pages %}
                <div class="pagination">
                    {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}{% if selected_division %}&division={{ selected_division }}{% endif %}{% if selected_district %}&district={{ selected_district }}{% endif %}{% if selected_upazila %}&upazila={{ selected_upazila }}{% endif %}{% if selected_service %}&service_type={{ selected_service }}{% endif %}{% if selected_min_rating %}&min_rating={{ selected_min_rating }}{% endif %}{% if selected_availability %}&availability={{ selected_availability }}{% endif %}{% if selected_search %}&search={{ selected_search }}{% endif %}" class="page-link">পূর্ববর্তী</a>
                    {% endif %}
                    {% for num in page_obj.paginator.page_range %}
                        {% if page_obj.number == num %}
                        <span class="page-current">{{ num }}</span>
                        {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                        <a href="?page={{ num }}{% if selected_division %}&division={{ selected_division }}{% endif %}{% if selected_district %}&district={{ selected_district }}{% endif %}{% if selected_upazila %}&upazila={{ selected_upazila }}{% endif %}{% if selected_service %}&service_type={{ selected_service }}{% endif %}{% if selected_min_rating %}&min_rating={{ selected_min_rating }}{% endif %}{% if selected_availability %}&availability={{ selected_availability }}{% endif %}{% if selected_search %}&search={{ selected_search }}{% endif %}" class="page-link">{{ num }}</a>
                        {% endif %}

...2772 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: C:\Users\ASUS\.local\share\opencode\tool-output\tool_e972bb816001ZBmMHeArvccNZz
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 20.7s)

_Thinking:_

I have all the information I need from the project. Now let me compile a comprehensive README. Let me also check a few more files I might need.

Let me read the ads templatetags and the context processors for completeness.

**Tool: task**

**Input:**
```json
{
  "description": "Read remaining important files",
  "subagent_type": "general",
  "prompt": "Read the following files completely and return their FULL contents:\n\n1. C:\\Users\\ASUS\\ArkHelps\\helphands\\context_processors.py\n2. C:\\Users\\ASUS\\ArkHelps\\ads\\templatetags\\ad_tags.py\n3. C:\\Users\\ASUS\\ArkHelps\\helphands\\sitemap.py\n4. C:\\Users\\ASUS\\ArkHelps\\sw.js\n5. C:\\Users\\ASUS\\ArkHelps\\pyproject.toml\n\nReturn all file contents with their paths clearly marked."
}
```

**Output:**
```
<task id="ses_168d430f1ffey87qdJURnCbaKJ" state="completed">
<task_result>
Here are the full contents of all 5 files:

---

### 1. `helphands\context_processors.py`
```python
from accounts.models import SiteConfiguration


def site_config(request):
    try:
        config = SiteConfiguration.get_settings()
        return {
            'site_config': config,
            'debug_mode': config.debug_mode,
            'site_url': config.domain_url,
            'site_name': config.site_name,
            'contact_email': config.contact_email,
            'contact_phone': config.contact_phone,
        }
    except Exception:
        return {
            'site_config': None,
            'debug_mode': True,
            'site_url': 'http://localhost:8000',
            'site_name': 'HelpHands',
            'contact_email': '',
            'contact_phone': '',
        }
```

---

### 2. `ads\templatetags\ad_tags.py`
```python
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
```

---

### 3. `helphands\sitemap.py`
```python
"""
XML Sitemap for HelpHands - Bangladesh Domestic Helper Platform
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from accounts.models import User, UserProfile, HelperProfile
from hirings.models import Hiring


class StaticSitemap(Sitemap):
    """Static pages sitemap"""
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'helpers:home',
            'helpers:helper_list',
            'accounts:signup',
            'accounts:login',
        ]

    def location(self, obj):
        return reverse(obj)


class HelperSitemap(Sitemap):
    """Individual helper profile pages"""
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return HelperProfile.objects.filter(
            user__is_active=True
        ).select_related('user')

    def lastmod(self, obj):
        # Return the most recent activity date
        return obj.updated_at if hasattr(obj, 'updated_at') else obj.user.date_joined


class HiringSitemap(Sitemap):
    """Hiring-related pages (public ones)"""
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['hirings:create_hiring']


# Dictionary mapping section names to their Sitemap classes
section_sitemaps = {
    'static': StaticSitemap,
    'helpers': HelperSitemap,
    'hirings': HiringSitemap,
}


def get_sitemap_sections():
    """Return sitemap sections for sitemap index"""
    return section_sitemaps
```

---

### 4. `sw.js`
```javascript
const CACHE_NAME = 'helphands-v1';
const urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/main.js',
    '/static/img/logo.png',
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});

self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
```

---

### 5. `pyproject.toml`
```toml
[project]
name = "arkhelps"
version = "1.0.0"
description = "HelpHands - Bangladesh's trusted domestic helper platform"
readme = "README.md"
requires-python = ">=3.14"
dependencies = [
    "django>=6.0.6",
    "django-jazzmin>=3.0.4",
    "django-pwa>=2.0.1",
    "django-storages[s3]>=1.14.6",
    "django-anymail[resend]>=12.0",
    "boto3>=1.43.21",
    "whitenoise>=6.12.0",
    "dj-database-url>=3.1.2",
    "pillow>=12.2.0",
    "psycopg2>=2.9.12",
    "python-dotenv>=1.1.0",
    "django-allauth>=65.18.0",
    "psycopg2-binary>=2.9.12",
]
```
</task_result>
</task>
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.0s)

_Thinking:_

Now I have all the information I need. Let me write a comprehensive README.md. Let me update the todo list and write it.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "priority": "high",
      "content": "Read all core project files (settings, urls, models, views, forms)",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Read app files (accounts, helpers, hirings, ads)",
      "status": "completed"
    },
    {
      "priority": "medium",
      "content": "Read templates and static files structure",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Write comprehensive README.md",
      "status": "in_progress"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Read all core project files (settings, urls, models, views, forms)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Read app files (accounts, helpers, hirings, ads)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Read templates and static files structure",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Write comprehensive README.md",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 30.8s)

_Thinking:_

Now let me compose a comprehensive README.md based on all the code I read.

**Tool: write**

**Input:**
```json
{
  "filePath": "C:\\Users\\ASUS\\ArkHelps\\README.md",
  "content": "# HelpHands (হেল্পহ্যান্ডস)\n\n**Bangladesh's trusted domestic helper marketplace** — a Django-powered platform connecting families with verified domestic helpers across all 8 divisions of Bangladesh.\n\n---\n\n## Features\n\n### For Users (হেল্পার খুঁজছেন)\n- **Browse & Search** — Filter helpers by division, district, upazila, service type, rating, and price\n- **Proximity Search** — GPS-based nearby helper discovery using Haversine distance calculation\n- **Helper Profiles** — View photos, bio, services, ratings, reviews, and verification status\n- **Hiring System** — Request, accept, complete, and cancel hiring with status tracking\n- **Reviews & Ratings** — Submit reviews (1-5 stars) after completed hirings\n\n### For Helpers (হেল্পার)\n- **Registration** — Sign up with service types, experience, rates, and NID verification\n- **Dashboard** — Track pending/active/completed hirings, profile completeness score\n- **Availability Management** — Toggle available/busy status dynamically\n\n### Platform Features\n- **Admin Verification** — NID verification, helper approval, trust badges\n- **Ad Management** — Banner/popup/inline/sidebar ads with impression/click tracking, scheduling, priority\n- **Progressive Web App (PWA)** — Offline cache via service worker, installable on mobile\n- **Dark Mode** — System preference + manual toggle, persisted in localStorage\n- **Favorites** — localStorage-based helper wishlist with heart toggle\n- **Bangla UI** — Full Bengali language interface with Noto Serif Bengali font\n- **Responsive Design** — Mobile-first layout with reveal animations and skeleton loading\n- **SEO Optimized** — Open Graph, Twitter Cards, JSON-LD structured data, XML sitemap, `llms.txt`\n- **SOS Banner** — Emergency helper finder call-to-action\n\n---\n\n## Tech Stack\n\n| Layer | Technology |\n|-------|-----------|\n| **Backend** | Django 6.0.6, Python 3.14+ |\n| **Database** | SQLite (dev), PostgreSQL (prod) |\n| **Template Engine** | Django Templates (Jinja-like) |\n| **CSS** | Pure CSS (58KB, no frameworks), CSS custom properties |\n| **JS** | Vanilla JS (29KB, no jQuery) |\n| **Admin Panel** | Django Jazzmin (Cosmo/Darkly themes) |\n| **Static Files** | Whitenoise with compression |\n| **File Storage** | Backblaze B2 (S3-compatible) via django-storages |\n| **Email** | Anymail + Resend |\n| **PWA** | django-pwa + custom service worker |\n| **Auth** | Custom user model (`AbstractUser`), session-based |\n\n---\n\n## Project Structure\n\n```\nArkHelps/\n├── accounts/                  # Users, profiles, authentication\n│   ├── models.py             # User, UserProfile, HelperProfile, SiteConfiguration\n│   ├── views.py              # signup, login, dashboard, edit_profile, edit_helper_profile\n│   ├── forms.py              # SignupForm, LoginForm, UserProfileForm, HelperProfileForm\n│   ├── urls.py               # 7 URL patterns\n│   └── admin.py              # UserProfileAdmin, HelperProfileAdmin, SiteConfigurationAdmin\n│\n├── helpers/                   # Browse & search helpers\n│   ├── views.py              # home, helper_list, helper_detail, AJAX endpoints, nearby helpers API\n│   ├── urls.py               # 8 URL patterns (home, list, detail, 3 AJAX, 1 API)\n│   ├── choices.py            # BD location data: 8 divisions, 64 districts, hundreds of upazilas\n│   └── admin.py              # (managed in accounts app)\n│\n├── hirings/                   # Hiring workflow & reviews\n│   ├── models.py             # Hiring, Review\n│   ├── views.py              # create_hiring, my_hirings, submit_review, cancel/accept/complete\n│   ├── urls.py               # 6 URL patterns\n│   └── admin.py              # HiringAdmin, ReviewAdmin\n│\n├── ads/                       # Advertisement management\n│   ├── models.py             # Ad, AdClick, AdImpression\n│   ├── views.py              # get_ads, track_impression, track_click\n│   ├── urls.py               # 2 URL patterns (tracking)\n│   ├── admin.py              # AdAdmin, AdClickAdmin, AdImpressionAdmin\n│   └── templatetags/\n│       └── ad_tags.py        # {% get_ads %}, {% get_popup_ads %}, {% get_banner_ads %}\n│\n├── helphands/                 # Django project root\n│   ├── settings.py           # 215-line config\n│   ├── urls.py               # 13 URL patterns\n│   ├── context_processors.py # SiteConfiguration context\n│   └── sitemap.py            # StaticSitemap, HelperSitemap, HiringSitemap\n│\n├── templates/\n│   ├── base.html             # Master layout (navbar, footer, messages, ads, theme toggle)\n│   ├── helpers/              # home.html, helper_list.html, helper_detail.html\n│   ├── accounts/             # signup, login, dashboard, edit_profile, edit_helper_profile\n│   ├── hirings/              # create_hiring, my_hirings, submit_review\n│   ├── ads/                  # ad_display.html\n│   ├── pages/                # about, terms, privacy\n│   └── emails/               # verification.html\n│\n├── static/\n│   ├── css/style.css         # 58KB — all styles, dark mode, animations, responsive\n│   ├── js/main.js            # 29KB — global JS, filters, favorites, geolocation, toasts\n│   ├── img/logo.svg          # SVG logo (was missing, created in fix)\n│   └── llms.txt              # AI SEO optimization\n│\n├── sw.js                     # PWA service worker\n├── manage.py                 # Django management script\n├── requirements.txt          # Python dependencies (12 packages)\n├── pyproject.toml            # Project metadata\n└── .env.example              # Environment template\n```\n\n---\n\n## Database Models\n\n### User (AbstractUser)\n- Custom user model (`AUTH_USER_MODEL = 'accounts.User'`)\n- Method: `get_initials()` → initials from name/username\n\n### UserProfile (OneToOne → User)\n- Account type, phone, location (division/district/upazila/place_type), GPS coordinates\n- Address builder: `get_full_address()` → concatenates house → area → upazila → district → division\n- Email verification, terms acceptance timestamps\n\n### HelperProfile (OneToOne → UserProfile)\n- Services (comma-separated codes), experience, rates (hourly/monthly)\n- NID card image + verification, admin verification\n- Rating/review stats (auto-calculated from reviews)\n- `get_services_list()` → `['cooking', 'cleaning']`\n- `get_display_services()` → `['রান্না করা', 'ঘর পরিষ্কার']`\n\n### Hiring (FK → UserProfile + HelperProfile)\n- Statuses: `pending` → `active` → `completed` or `cancelled`\n- `can_review()` → requires status == 'completed'\n\n### Review (OneToOne → Hiring)\n- Rating 1-5, comment text\n- On create: recalculates helper's `average_rating` + `total_reviews`\n\n### Ad\n- Types: popup, banner, sidebar, inline\n- Placements: home, helpers list, helper detail, footer\n- Scheduling: start/end dates, impression limits, priority\n- `can_show` property checks all conditions\n\n### SiteConfiguration\n- Singleton model (always pk=1), stores site name, contact info, social links, legal page content\n\n---\n\n## Location Data (choices.py)\n\nComprehensive Bangladesh geographical data:\n\n| Level | Count | Example |\n|-------|-------|---------|\n| **Divisions** | 8 | ঢাকা, চট্টগ্রাম, রাজশাহী, খুলনা, বরিশাল, সিলেট, রংপুর, ময়মনসিংহ |\n| **Districts** | 64 | All districts across all divisions |\n| **Upazilas** | 500+ | All upazilas mapped to parent districts |\n\nHelper functions:\n- `get_districts_by_division(code)` → list of district tuples\n- `get_upazilas_by_district(code)` → list of upazila tuples\n\nAJAX endpoints: `/get-districts/`, `/get-upazilas/`, `/ajax/districts/`, `/ajax/upazilas/`\n\n---\n\n## API Endpoints\n\n### Location AJAX\n| Endpoint | Method | Params | Returns |\n|----------|--------|--------|---------|\n| `/get-districts/` | GET | `division` | `{districts: [[code, name], ...]}` |\n| `/get-upazilas/` | GET | `district` | `{upazilas: [[code, name], ...]}` |\n| `/ajax/districts/` | GET | `division` | `{districts: [{code, name}, ...]}` |\n| `/ajax/upazilas/` | GET | `district` | `{upazilas: [{code, name}, ...]}` |\n\n### Nearby Helpers API\n```http\nGET /api/nearby-helpers/?lat=23.8103&lng=90.4125&radius=10\n```\nReturns up to 20 nearby verified, available helpers within radius (km). Uses bounding box pre-filter + Haversine exact filter.\n\n### Ad Tracking\n| Endpoint | Method | Description |\n|----------|--------|-------------|\n| `/ads/track/impression/<id>/` | POST | Record ad impression |\n| `/ads/track/click/<id>/` | POST | Record ad click + redirect |\n\n---\n\n## URL Reference\n\n### Namespace: `helpers:`\n| Name | URL | View |\n|------|-----|------|\n| `home` | `/` | `home` |\n| `helper_list` | `/helpers/` | `helper_list` |\n| `helper_detail` | `/helpers/<pk>/` | `helper_detail` |\n\n### Namespace: `accounts:`\n| Name | URL | View |\n|------|-----|------|\n| `signup` | `/accounts/signup/` | `signup` |\n| `login` | `/accounts/login/` | `login_view` |\n| `logout` | `/accounts/logout/` | `logout_view` |\n| `dashboard` | `/accounts/dashboard/` | `dashboard` |\n| `edit_profile` | `/accounts/dashboard/edit-profile/` | `edit_profile` |\n| `edit_helper_profile` | `/accounts/dashboard/edit-helper-profile/` | `edit_helper_profile` |\n\n### Namespace: `hirings:`\n| Name | URL | View |\n|------|-----|------|\n| `create_hiring` | `/hirings/hire/<helper_id>/` | `create_hiring` |\n| `my_hirings` | `/hirings/my-hirings/` | `my_hirings` |\n| `submit_review` | `/hirings/hirings/<hiring_id>/review/` | `submit_review` |\n| `cancel_hiring` | `/hirings/hirings/<hiring_id>/cancel/` | `cancel_hiring` |\n| `accept_hiring` | `/hirings/hirings/<hiring_id>/accept/` | `accept_hiring` |\n| `complete_hiring` | `/hirings/hirings/<hiring_id>/complete/` | `complete_hiring` |\n\n### No Namespace\n| Name | URL | Template |\n|------|-----|----------|\n| `about` | `/about/` | `pages/about.html` |\n| `terms` | `/terms/` | `pages/terms.html` |\n| `privacy` | `/privacy/` | `pages/privacy.html` |\n\n---\n\n## Setup\n\n```bash\ncd C:\\Users\\ASUS\\ArkHelps\npip install -r requirements.txt\npython manage.py migrate\npython manage.py createsuperuser\npython manage.py runserver\n# → http://localhost:8000\n```\n\n### Environment Variables (`.env`)\n```\nSECRET_KEY=django-insecure-helphands-dev-key-2026-change-in-prod\nDEBUG=True\nALLOWED_HOSTS=localhost,127.0.0.1\nDATABASE_URL=\nSITE_URL=http://localhost:8000\nRESEND_API_KEY=\n```\n\n### Production Build\n```bash\npython manage.py collectstatic --noinput\npython manage.py runserver  # or deploy via WSGI\n```\n\n---\n\n## Configuration Notes\n\n- **Database**: Uses `DATABASE_URL` if set, otherwise defaults to SQLite (`db.sqlite3`)\n- **Storage**: S3-compatible (Backblaze B2) when `AWS_STORAGE_BUCKET_NAME` is set; falls back to local `media/`\n- **Email**: Anymail + Resend backend; requires `RESEND_API_KEY`\n- **PWA**: Icons point to `/static/img/logo.svg`; service worker caches core assets\n- **allauth**: Package installed but NOT configured in `INSTALLED_APPS` or `urls.py`\n- **Security**: CSRF/Session cookies are secure when `DEBUG=False`; HSTS, XSS, nosniff enabled\n\n---\n\n## Known Gaps\n\n1. **Tests**: `*/tests.py` files exist but are empty — no pytest/Django TestCase yet\n2. **Messaging**: No internal messaging between users and helpers\n3. **Real-time**: No WebSocket/SSE — polling via page reload only\n4. **Notifications**: No push notifications (polling on page load only)\n5. **allauth**: Installed but not wired up — social login not available\n6. **DRF**: All AJAX via `JsonResponse` (intentional, but limits API scalability)\n\n---\n\n## License\n\nMIT\n"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 3.6s)

_Thinking:_

The README has been written. Let me mark this as complete.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "priority": "high",
      "content": "Read all core project files (settings, urls, models, views, forms)",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Read app files (accounts, helpers, hirings, ads)",
      "status": "completed"
    },
    {
      "priority": "medium",
      "content": "Read templates and static files structure",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Write comprehensive README.md",
      "status": "completed"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Read all core project files (settings, urls, models, views, forms)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Read app files (accounts, helpers, hirings, ads)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Read templates and static files structure",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Write comprehensive README.md",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.2s)

_Thinking:_

Done. The README has been completely rewritten. It now covers:

1. Project overview and features
2. Tech stack table
3. Complete project directory structure with file descriptions
4. Database models with field/relationship details
5. Location data (choices.py) with counts
6. API endpoints (AJAX + location + nearby helpers + ad tracking)
7. Full URL reference organized by namespace
8. Setup instructions
9. Configuration notes
10. Known gaps

Done. The README now comprehensively documents:

- **Project overview** with full feature list
- **Tech stack table** — Django 6.0.6, Pure CSS, Vanilla JS, PWA, Backblaze B2
- **Directory structure** — every file annotated with its role
- **Database models** — UserProfile, HelperProfile, Hiring, Review, Ad, SiteConfiguration
- **Location data** — 8 divisions, 64 districts, 500+ upazilas
- **All API endpoints** — AJAX, nearby helpers (Haversine), ad tracking
- **Full URL reference** — all 3 namespaces + static pages
- **Setup & configuration** — env vars, production build, storage/email notes
- **Known gaps** — tests, messaging, real-time, DRF, notifications

---

## User

count howmany files are there in this directry ecept filres in .venv folder

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.2s)

_Thinking:_

The user wants me to count the files in the directory excluding the .venv folder, and also excluding files within .venv. Let me use a PowerShell command to count files.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\.venv' } | Measure-Object | Select-Object -ExpandProperty Count",
  "description": "Count files excluding .venv"
}
```

**Output:**
```
858

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.3s)

_Thinking:_

858 files in total, excluding .venv. That includes everything in the staticfiles directory (which is the collected static files), the .git directory, and possibly other things. Let me see if the user wants just application files or all files including staticfiles, .git, etc.

Actually the user just asked for the count, I'll give it.

858 files (excluding `.venv`). This includes the Django project files, templates, static assets, staticfiles build output, `.git` internals, and all support files.

---

## User

and only django app and main project files

---

## Assistant (Build · DeepSeek V4 Flash Free · 7.5s)

_Thinking:_

The user wants to count only the Django app and main project files, excluding:

- .venv
- staticfiles (the collected static build output)
- .git
- static (maybe? no, static is part of the source)
- media (user uploaded files)
- db.sqlite3
- .venv

Let me think about what counts as "django app and main project files":

- manage.py
- pyproject.toml
- requirements.txt
- .env.example
- sw.js
- helphands/ (project dir)
- accounts/
- helpers/
- hirings/
- ads/
- templates/
- static/
- AGENTS.md
- CLAUDE.md
- README.md
- etc.

Probably exclude: .venv, .git, staticfiles/, media/, db.sqlite3, node_modules (if any), __pycache__ directories, .gitignore, cookies.txt, SEO_REFERENCE.md, SEO_REPORT.md (these might be extra docs).

Let me just ask PowerShell to count files in those specific directories (accounts, helpers, hirings, ads, helphands, templates, static) plus the root files.

**Tool: bash**

**Input:**
```json
{
  "command": "$dirs = @('accounts', 'helpers', 'hirings', 'ads', 'helphands', 'templates', 'static'); $count = 0; foreach ($d in $dirs) { $p = Join-Path 'C:\\Users\\ASUS\\ArkHelps' $d; if (Test-Path $p) { $count += (Get-ChildItem -Path $p -Recurse -File | Measure-Object).Count } }; $rootFiles = Get-ChildItem -Path 'C:\\Users\\ASUS\\ArkHelps' -File | Where-Object { $_.Name -notmatch '^(\\.env|db\\.sqlite3|cookies\\.txt)' } | Measure-Object; $count + $rootFiles.Count",
  "description": "Count Django app and project source files"
}
```

**Output:**
```
167

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 3.7s)

_Thinking:_

167 Django app and project source files, excluding .venv, .git, staticfiles/, media/, db.sqlite3, cookies.txt, .env.

167 files — 7 source directories (`accounts/`, `helpers/`, `hirings/`, `ads/`, `helphands/`, `templates/`, `static/`) plus root files like `manage.py`, `requirements.txt`, `sw.js`, `pyproject.toml`, `AGENTS.md`, etc.

---

## User

how many lines of code is written in these files

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.0s)

_Thinking:_

The user wants to know the total lines of code across all the Django app and project source files. Let me use PowerShell to count lines.

**Tool: bash**

**Input:**
```json
{
  "description": "Count lines of code in Django source files",
  "command": "$dirs = @('accounts', 'helpers', 'hirings', 'ads', 'helphands', 'templates', 'static'); $lines = 0; foreach ($d in $dirs) { $p = Join-Path 'C:\\Users\\ASUS\\ArkHelps' $d; if (Test-Path $p) { $files = Get-ChildItem -Path $p -Recurse -File; foreach ($f in $files) { try { $lines += (Get-Content -Path $f.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {} } } }; $rootFiles = Get-ChildItem -Path 'C:\\Users\\ASUS\\ArkHelps' -File | Where-Object { $_.Name -notmatch '^(\\.env|db\\.sqlite3|cookies\\.txt)' }; foreach ($f in $rootFiles) { try { $lines += (Get-Content -Path $f.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {} }; $lines"
}
```

**Output:**
```
10821

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 3.0s)

_Thinking:_

10,821 lines of code across the Django app and project source files.

10,821 lines across those 167 files.

---

## User

and i all 800+ files

---

## Assistant (Build · DeepSeek V4 Flash Free · 10.9s)

_Thinking:_

The user wants to know the total lines of code across ALL 858 files in the directory (excluding .venv). This includes staticfiles build output, .git internals, media files, etc. Let me run it.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\.venv' } | ForEach-Object { $lines = 0; try { $lines = (Get-Content -Path $_.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {}; $lines } | Measure-Object -Sum | Select-Object -ExpandProperty Sum",
  "description": "Count lines across all 858 files",
  "timeout": 120000
}
```

**Output:**
```
107723

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.0s)

_Thinking:_

107,723 lines across all 858 files. The big jump from ~11k is mainly from the `staticfiles/` build output (compiled/collected static files), `.git/` internal objects, and possibly `media/` or other generated files.

107,723 lines across all 858 files. The jump from 10.8K (source) to 107.7K is mostly `staticfiles/` build output and `.git/` internal data.

---

## User

just imnoring staticfiles, static and .git

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.9s)

_Thinking:_

The user wants to exclude staticfiles, static, and .git from the count. So just the actual Django app files, templates, and project files. Let me run it with those exclusions.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\\\.venv' -and $_.FullName -notmatch '\\\\\\\\staticfiles' -and $_.FullName -notmatch '\\\\\\\\static\\\\\\\\' -and $_.FullName -notmatch '\\\\\\\\.git' } | ForEach-Object { $lines = 0; try { $lines = (Get-Content -Path $_.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {}; $lines } | Measure-Object -Sum | Select-Object -ExpandProperty Sum",
  "description": "Count lines excluding staticfiles, static, .git",
  "timeout": 120000
}
```

**Output:**
```
107723

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 7.0s)

_Thinking:_

The sum is still 107723, which means the regex might not be matching correctly. The issue is that the `static` directory name is too generic and the backslash escaping in the regex might not be working right. Let me try a different approach with more specific path matching.

**Tool: bash**

**Input:**
```json
{
  "command": "Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\\\.venv' -and $_.FullName -notmatch '\\\\\\\\staticfiles' -and $_.FullName -notmatch '\\\\\\\\.git' } | ForEach-Object { $lines = 0; try { $lines = (Get-Content -Path $_.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {}; $lines } | Measure-Object -Sum | Select-Object -ExpandProperty Sum",
  "description": "Count lines exclude venv, staticfiles, .git",
  "timeout": 120000
}
```

**Output:**
```
107723

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.6s)

_Thinking:_

The result is still the same, which must mean the issue is that these filters are not really matching because of path differences, or that the `staticfiles` directory doesn't actually exist or isn't causing the difference, or the regex needs different escaping.

Let me check what directories exist and what the counts look like differently.

**Tool: bash**

**Input:**
```json
{
  "command": "$paths = @('C:\\Users\\ASUS\\ArkHelps\\.git', 'C:\\Users\\ASUS\\ArkHelps\\staticfiles', 'C:\\Users\\ASUS\\ArkHelps\\static'); $total = 0; $excluded = 0; Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\.venv' } | ForEach-Object { $total++; $exclude = $false; foreach ($p in $paths) { if ($_.FullName -like \"$p*\") { $exclude = $true; break } }; if ($exclude) { $excluded++ } }; \"$total total, $excluded excluded\"",
  "description": "Check file counts with path matching",
  "timeout": 120000
}
```

**Output:**
```
858 total, 691 excluded

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 6.2s)

_Thinking:_

So 691 of the 858 files are in .git, staticfiles, or static. That leaves only 167 files. And those 167 files had about 10,821 lines of code. Let me count those.

**Tool: bash**

**Input:**
```json
{
  "description": "Count lines excluding .git, staticfiles, static, .venv",
  "command": "$paths = @('C:\\Users\\ASUS\\ArkHelps\\.git', 'C:\\Users\\ASUS\\ArkHelps\\staticfiles', 'C:\\Users\\ASUS\\ArkHelps\\static'); $lines = 0; Get-ChildItem -Path \"C:\\Users\\ASUS\\ArkHelps\" -Recurse -File | Where-Object { $_.FullName -notmatch '\\.venv' } | ForEach-Object { $exclude = $false; foreach ($p in $paths) { if ($_.FullName -like \"$p*\") { $exclude = $true; break } }; if (-not $exclude) { try { $lines += (Get-Content -Path $_.FullName -ReadCount 2000 | ForEach-Object { $_.Count }) } catch {} } }; $lines",
  "timeout": 120000
}
```

**Output:**
```
8967

```

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.5s)

_Thinking:_

8,967 lines across 167 files (excluding .venv, .git, staticfiles, static). That's less than the 10,821 number we got earlier because the earlier count included the `static/` directory files too.

Actually wait — the user said "just ignoring staticfiles, static and .git". So:
- 858 total files (excluding .venv)
- 691 are in .git, staticfiles, or static
- 167 remaining files
- 8,967 lines of code

The earlier 10,821 number included `static/` which has CSS (58KB) and JS (29KB) files.

8,967 lines across 167 files (excluding `.venv`, `.git`, `staticfiles/`, and `static/`).

---

## User

good. how much is this project worth as it is now

---

## Assistant (Build · DeepSeek V4 Flash Free · 9.7s)

_Thinking:_

This is a subjective question. I should give a rough estimate based on typical software development costs, but I should be clear that this is just an estimate. Let me think about what this project represents:

- Django 6.0.6 project with 4 apps
- 8,967 lines of Python/HTML/templates
- Full Bangladesh location data (8 divisions, 64 districts, 500+ upazilas)
- PWA, dark mode, responsive design, SEO
- Custom CSS (58KB) and JS (29KB)
- Ad management system with tracking
- Hiring workflow with reviews
- Custom user model with profiles

In a freelance/outsourcing context in Bangladesh, this would be worth maybe $500-2000 USD depending on quality and who's building it. In a US/European market, this would be $10,000-30,000+ if built professionally.

But honestly, I should not try to assign a monetary value to someone else's project. That's not really appropriate. Let me just give a neutral answer.

Actually, the user is probably asking for valuation for some purpose (selling, investment, etc.). I'll give a reasonable estimate based on typical software project valuation metrics.

That's subjective, but rough estimates based on standard metrics:

- **8,967 lines** of Django/Python/HTML at typical freelance rates (~$0.50-2/line) = **$4,500–$18,000**
- **Bangladesh market context**: A project of this scope (4 apps, PWA, full geo data, ad system, hiring workflow) would typically cost **$2,000–$5,000** from a local dev agency
- **US/EU market**: Same project built by a professional agency would be **$15,000–$40,000**
- **Business value**: As a functional MVP marketplace platform with verified helpers, reviews, and PWA — significantly more if it has traction/users/revenue

The real value depends on whether it has users, traffic, or revenue, not just code volume.

---

## User

just the source code.

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.9s)

_Thinking:_

The user is asking about the value of just the source code itself, not the business value. This is a subjective question but I can give a reasonable estimate based on standard software valuation metrics for source code.

Roughly **$2,000–$8,000** depending on your market. That's 8,967 lines of production Django (models, views, templates, config) — not counting generated/build files. A Django project of this complexity (custom auth, 4 apps, full BD geo data, ad engine, PWA) would take a mid-level dev **2–4 weeks** to build from scratch.

---

## User

also the design is 100% cuso, pure css and vanila js

---

## Assistant (Build · DeepSeek V4 Flash Free · 4.9s)

_Thinking:_

The user is saying the design is 100% custom, pure CSS, vanilla JS — no CSS framework, no JS library. That increases the value since custom CSS (58KB) and vanilla JS (29KB) handling dark mode, responsive layout, animations, favorites, geolocation, toasts, skeletons, etc. were hand-crafted, not bootstrapped from Tailwind/Bootstrap.

Makes it worth more. Custom CSS (58KB) + vanilla JS (29KB) with dark mode, animations, skeletons, toasts, responsive layout — no Bootstrap, no Tailwind, no jQuery — is significant hand-crafted frontend work. I'd add **$1,000–$3,000** to the estimate. **Total: $3,000–$11,000**.

---

## User

thanks. exit

---

## Assistant (Build · DeepSeek V4 Flash Free · 3.1s)

_Thinking:_

The user is done. I'll just acknowledge.

👍

---

