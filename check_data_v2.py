import os
import django
import sys

sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Course

print("--- Checking ALL Courses for curly braces ---")
courses = Course.objects.all()
found_issue = False
for c in courses:
    if "{{" in c.code or "}}" in c.code:
        print(f"ISSUE FOUND: ID={c.pk}, Code='{c.code}'")
        found_issue = True
    
    # Also check title
    if "{{" in c.title:
        print(f"ISSUE FOUND: ID={c.pk}, Title='{c.title}'")
        found_issue = True

if not found_issue:
    print(f"Checked {courses.count()} courses. No curly braces found.")
else:
    print("Found issues!")
