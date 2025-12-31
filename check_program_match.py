import os
import django
import sys

sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Program

print("--- Checking Programs ---")
programs = Program.objects.all()
for p in programs:
    print(f"ID: {p.pk} | Code: '{p.code}' | Slug: '{p.url_slug}'")

print("\n--- Checking File Paths ---")
# Verify where the loader thinks templates are
from django.template.loader import get_template
t = get_template('home/bit.html')
print(f"home/bit.html origin: {t.origin.name}")
