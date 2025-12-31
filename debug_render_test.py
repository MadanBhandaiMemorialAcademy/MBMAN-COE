import os
import django
import sys
from django.template import Context, Template, Engine
from django.template.loader import get_template
from django.conf import settings

# Setup Django environment
sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Curriculum, CurriculumSemester, Course, Program

print("--- 1. Data Integrity Check & Creation ---")
# Create dummy data if needed
program, _ = Program.objects.get_or_create(code="TEST", defaults={"full_name": "Test Program", "url_slug": "test-prog", "short_description": "Test", "full_description": "Test"})
curriculum, _ = Curriculum.objects.get_or_create(program=program, defaults={"overview_text": "Test Overview"})
semester, _ = CurriculumSemester.objects.get_or_create(curriculum=curriculum, semester_number=1, defaults={"description": "Sem 1"})
course, created = Course.objects.get_or_create(semester=semester, code="TEST101", defaults={"title": "Test Course", "credits": 3})

if created:
    print("Created dummy test data.")
else:
    print("Using existing dummy test data.")
# Check a sample course
course = Course.objects.first()
if course:
    print(f"Sample Course ID: {course.pk}")
    print(f"Code: '{course.code}'")
    print(f"Title: '{course.title}'")
    
    if "{{" in course.code:
        print("CRITICAL: Found '{{' in course code in DB!")
    else:
        print("Data looks clean (no '{{' in code).")
else:
    print("No courses found in DB.")

print("\n--- 2. Template Rendering Test (Minimal) ---")
# Test basic string rendering
t = Template("My name is {{ name }}.")
c = Context({"name": "Django"})
print(f"Basic Render: {t.render(c)}")

print("\n--- 3. Template Rendering Test (curriculum_list.html) ---")
# Use the specific test curriculum we created
test_curriculum = Curriculum.objects.filter(program__code="TEST").first()

# Mock request with messages
from django.http import HttpRequest
request = HttpRequest()
request.user = type('User', (object,), {'is_authenticated': True, 'is_staff': True, 'username': 'testuser'})()

try:
        # Test BIT template rendering specifically for tabs
        t = get_template('home/bit.html')
        
        # Ensure we have semester data
        if not test_curriculum.semesters.exists():
            print("Adding dummy semester for testing...")
            CurriculumSemester.objects.create(curriculum=test_curriculum, semester_number=1, description="Sem 1 Desc")
            
        semesters = test_curriculum.semesters.all()
        
        context = {
            'curriculum': test_curriculum,
            'semesters': semesters,
            'program': test_curriculum.program,
            'user': request.user,
        }
        
        output = t.render(context)
        
        # Check for tab buttons and script
        print("\n--- HTML Inspection ---")
        if "switchSemesterTab" in output:
             print("SUCCESS: Found 'switchSemesterTab' function call/definition.")
        else:
             print("FAILURE: 'switchSemesterTab' NOT found.")
             
        # Check onclick matching
        import re
        onclicks = re.findall(r"onclick=\"switchSemesterTab\('([^']+)', this\)\"", output)
        divs = re.findall(r'id="([^"]+)"', output)
        print(f"Onclick targets: {onclicks}")
        print(f"Div IDs found: {divs}")
        
        common = set(onclicks) & set(divs)
        if common:
            print(f"SUCCESS: Match found for IDs: {common}")
        else:
            print("FAILURE: No matching Button->Div IDs found.")

except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error rendering template: {e}")

print("\n--- 4. Checking Settings ---")
print(f"TEMPLATES backend: {settings.TEMPLATES[0]['BACKEND']}")
