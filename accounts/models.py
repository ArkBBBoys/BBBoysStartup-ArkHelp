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
    site_name = models.CharField(max_length=100, default='Khujo')
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
