import os
import django
import sys

# Setup Django environment
sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Curriculum

print("--- Reactivating Inactive Curriculums ---")

count = Curriculum.objects.filter(is_active=False).update(is_active=True)
print(f"Successfully activated {count} hidden curriculums.")
