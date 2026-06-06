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