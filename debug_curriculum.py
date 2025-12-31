import os
import django
import sys

# Setup Django environment
sys.path.append("/home/aaxyat/Projects/MBMAN-COE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from home.models import Program, Curriculum, CurriculumSemester

print("--- Debugging Curriculum Display Issue ---")

programs = Program.objects.all()
for program in programs:
    print(f"\nProgram: {program.full_name} (Code: {program.code})")
    curriculums = Curriculum.objects.filter(program=program)
    print(f"  Total Curriculums Found: {curriculums.count()}")
    
    for i, curr in enumerate(curriculums):
        sem_count = curr.semesters.count()
        print(f"  {i+1}. ID: {curr.pk} | Is Active: {curr.is_active} | Semester Count: {sem_count}")
        
    # Simulate view logic
    simulated_curr = Curriculum.objects.filter(program=program, is_active=True).first()
    if simulated_curr:
        print(f"  -> View Logic selects ID: {simulated_curr.pk} which has {simulated_curr.semesters.count()} semesters.")
    else:
        print("  -> View Logic selects None.")
