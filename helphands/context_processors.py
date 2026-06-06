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
