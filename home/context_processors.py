from .models import ContactInfo, Program, SiteConfiguration, SiteLogo, FooterLink


def site_context(request):
    """Add global site configuration, contact info, site logo, and programs"""
    return {
        "site_config": SiteConfiguration.objects.filter(is_active=True).first(),
        "contact_info": ContactInfo.objects.filter(is_active=True).first(),
        "site_logo": SiteLogo.objects.filter(is_active=True).first(),
        "all_programs": Program.objects.filter(is_active=True).order_by("display_order"),
        "footer_links": FooterLink.objects.all(),
    }
