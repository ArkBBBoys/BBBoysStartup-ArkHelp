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
