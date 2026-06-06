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
