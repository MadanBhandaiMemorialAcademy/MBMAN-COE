"""
Management command to initialize a blank site configuration.
Creates a generic template that can be customized entirely through admin dashboard.
"""

from django.core.management.base import BaseCommand

from home.models import SiteConfiguration


class Command(BaseCommand):
    help = "Initialize blank site configuration for any college deployment"

    def handle(self, *args, **options):
        # Check if configuration already exists
        existing = SiteConfiguration.objects.filter(is_active=True).first()
        if existing:
            self.stdout.write(
                self.style.WARNING(
                    f"Site configuration already exists: {existing.college_name}"
                )
            )
            self.stdout.write(
                "To reconfigure, edit via Admin Dashboard → Site Configuration"
            )
            return

        # Create blank configuration with placeholder values
        SiteConfiguration.objects.create(
            college_name="Your College Name",
            short_name="YCN",
            tagline="Your College Tagline or Motto",
            established_year="20XX BS",
            about_us=(
                "Add information about your college here. "
                "This can be edited from the admin dashboard."
            ),
            mission="Enter your college mission statement here.",
            vision="Enter your college vision statement here.",
            core_values=(
                "Quality Education\n"
                "Student Success\n"
                "Innovation\n"
                "Community Service\n"
                "Excellence"
            ),
            footer_about="Brief description of your college for the footer section.",
            footer_text="All rights reserved.",
            is_active=True,
        )

        self.stdout.write(
            self.style.SUCCESS("✓ Created blank site configuration successfully!")
        )
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Next steps:"))
        self.stdout.write("  1. Go to Admin Dashboard (/admin/)")
        self.stdout.write("  2. Click 'Site Configuration'")
        self.stdout.write("  3. Customize college name, tagline, about, social links, etc.")
        self.stdout.write("  4. Add Programs via 'Manage Programs'")
        self.stdout.write("  5. Add Faculty via 'Manage Faculty'")
        self.stdout.write("  6. Upload slideshows via 'Image Slideshows'")
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Your college website is ready to customize!"))
