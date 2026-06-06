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