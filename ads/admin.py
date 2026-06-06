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
