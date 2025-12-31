import os
import django
import sys

# Setup Django environment
sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Course, CurriculumSemester

print("--- Checking for suspicious Course data ---")

suspicious_courses = Course.objects.filter(code__contains="{{")
if suspicious_courses.exists():
    print(f"Found {suspicious_courses.count()} courses with '{{' in the code:")
    for c in selected_courses:
        print(f"  ID: {c.pk} | Code: {c.code} | Title: {c.title}")
else:
    print("No courses found with '{{' in code.")

print("\n--- Checking for suspicious Semester data ---")
suspicious_semesters = CurriculumSemester.objects.filter(description__contains="{{")
if suspicious_semesters.exists():
    print(f"Found {suspicious_semesters.count()} semesters with '{{' in description:")
    for s in suspicious_semesters:
        print(f"  ID: {s.pk} | Description: {s.description}")
else:
    print("No semesters found with '{{' in description.")
