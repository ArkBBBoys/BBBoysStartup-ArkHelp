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
