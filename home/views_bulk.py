from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curriculum, CurriculumSemester, Course
from .bulk_forms import BulkSemesterForm, BulkCourseForm, BulkSemesterDeleteForm, BulkCourseDeleteForm

@login_required
@user_passes_test(lambda u: u.is_staff)
def semester_bulk_add(request, curriculum_pk):
    """Bulk add semesters to curriculum"""
    curriculum = get_object_or_404(Curriculum, pk=curriculum_pk)

    if request.method == "POST":
        form = BulkSemesterForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data["number_of_semesters"]
            start = form.cleaned_data["start_from"]
            created_count = 0
            
            for i in range(count):
                num = start + i
                # Check if semester already exists
                semester, created = CurriculumSemester.objects.get_or_create(
                    curriculum=curriculum,
                    semester_number=num,
                    defaults={
                        "display_order": num,
                        "description": f"Semester {num}"
                    }
                )
                if created:
                    created_count += 1
            
            messages.success(request, f"Successfully created {created_count} semesters!")
            return redirect("home:curriculum_list")
    else:
        # Auto-calculate start_from based on existing semesters
        last_semester = curriculum.semesters.order_by("-semester_number").first()
        initial_start = (last_semester.semester_number + 1) if last_semester else 1
        form = BulkSemesterForm(initial={"start_from": initial_start})

    return render(
        request,
        "home/admin/bulk_semester_form.html",
        {
            "form": form,
            "curriculum": curriculum,
            "title": f"Bulk Add Semesters - {curriculum.program}",
        },
    )

@login_required
@user_passes_test(lambda u: u.is_staff)
def course_bulk_add(request, semester_pk):
    """Bulk add courses to semester"""
    semester = get_object_or_404(CurriculumSemester, pk=semester_pk)

    if request.method == "POST":
        form = BulkCourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["course_data"]
            lines = data.strip().split("\n")
            created_count = 0
            errors = []
            
            # Get current max display order
            last_course = semester.courses.order_by("-display_order").first()
            current_order = (last_course.display_order + 1) if last_course else 1

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                parts = [p.strip() for p in line.split(",")]
                if len(parts) >= 3:
                    code = parts[0]
                    title = parts[1]
                    try:
                        credits = int(parts[2])
                    except ValueError:
                        errors.append(f"Invalid credits for {code}: {parts[2]}")
                        continue
                        
                    # Create course
                    Course.objects.create(
                        semester=semester,
                        code=code,
                        title=title,
                        credits=credits,
                        display_order=current_order
                    )
                    current_order += 1
                    created_count += 1
                else:
                    errors.append(f"Invalid format: {line}")
            
            if created_count > 0:
                messages.success(request, f"Successfully added {created_count} courses!")
            
            if errors:
                for err in errors:
                    messages.warning(request, err)
                    
            if created_count > 0:
                return redirect("home:curriculum_list")
                
    else:
        form = BulkCourseForm()

    return render(
        request,
        "home/admin/bulk_course_form.html",
        {
            "form": form,
            "semester": semester,
            "title": f"Bulk Add Courses - Semester {semester.semester_number}",
        },
    )

@login_required
@user_passes_test(lambda u: u.is_staff)
def semester_bulk_delete(request, curriculum_pk):
    """Bulk delete semesters from curriculum"""
    curriculum = get_object_or_404(Curriculum, pk=curriculum_pk)

    if request.method == "POST":
        form = BulkSemesterDeleteForm(request.POST, curriculum=curriculum)
        if form.is_valid():
            selected_semesters = form.cleaned_data["semesters"]
            count = selected_semesters.count()
            selected_semesters.delete()
            messages.success(request, f"Successfully deleted {count} semesters.")
            return redirect("home:curriculum_list")
    else:
        form = BulkSemesterDeleteForm(curriculum=curriculum)
    
    return render(
        request,
        "home/admin/bulk_semester_delete_form.html",
        {
            "form": form,
            "curriculum": curriculum,
            "title": f"Bulk Delete Semesters - {curriculum.program}",
        }
    )

@login_required
@user_passes_test(lambda u: u.is_staff)
def course_bulk_delete(request, semester_pk):
    """Bulk delete courses from semester"""
    semester = get_object_or_404(CurriculumSemester, pk=semester_pk)

    if request.method == "POST":
        form = BulkCourseDeleteForm(request.POST, semester=semester)
        if form.is_valid():
            selected_courses = form.cleaned_data["courses"]
            count = selected_courses.count()
            selected_courses.delete()
            messages.success(request, f"Successfully deleted {count} courses.")
            return redirect("home:curriculum_list")
    else:
        form = BulkCourseDeleteForm(semester=semester)
    
    return render(
        request,
        "home/admin/bulk_course_delete_form.html",
        {
            "form": form,
            "semester": semester,
            "title": f"Bulk Delete Courses - Semester {semester.semester_number}",
        }
    )
