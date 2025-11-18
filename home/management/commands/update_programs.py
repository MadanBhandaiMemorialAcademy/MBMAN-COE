from django.core.management.base import BaseCommand

from home.models import Program


class Command(BaseCommand):
    help = "Update existing programs with new fields"

    def handle(self, *args, **kwargs):
        # Update BIT program
        try:
            bit = Program.objects.get(code="BIT")
            bit.url_slug = "bit"
            bit.color_scheme = "blue"
            bit.icon_class = "fas fa-code"
            bit.display_order = 1
            bit.save()
            self.stdout.write(self.style.SUCCESS("Updated BIT program"))
        except Program.DoesNotExist:
            self.stdout.write(self.style.WARNING("BIT program not found"))

        # Update AG program
        try:
            ag = Program.objects.get(code="AG")
            ag.url_slug = "agriculture"
            ag.color_scheme = "green"
            ag.icon_class = "fas fa-leaf"
            ag.display_order = 2
            ag.save()
            self.stdout.write(self.style.SUCCESS("Updated AG program"))
        except Program.DoesNotExist:
            self.stdout.write(self.style.WARNING("AG program not found"))

        self.stdout.write(self.style.SUCCESS("Program updates complete!"))
