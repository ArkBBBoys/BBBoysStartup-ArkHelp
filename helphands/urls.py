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
