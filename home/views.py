from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import (
    ContactInfoForm,
    EventForm,
    FacultyForm,
    FooterLinkForm,
    GalleryAlbumForm,
    GalleryImageForm,
    HeroSectionForm,
    MarqueeItemForm,
    NoticeForm,
    PrincipalMessageForm,
    SiteLogoForm,
)
from .models import (
    CareerProspect,
    ContactInfo,
    ContactMessage,
    Course,
    Curriculum,
    CurriculumSemester,
    Event,
    Faculty,
    FooterLink,
    GalleryAlbum,
    GalleryImage,
    HeroSection,
    MarqueeItem,
    Notice,
    PrincipalMessage,
    Program,
    ProgramFeature,
    SiteLogo,
)


def index(request):
    """Homepage view with dynamic content"""
    from .models import FacultyTab, ImageSlideshow, SiteConfiguration

    # Get marquee items from notices - urgent first, then by created date, limit to 5
    marquee_notices = Notice.objects.filter(is_active=True).order_by(
        models.Case(
            models.When(priority="urgent", then=0),
            models.When(priority="highlight", then=1),
            models.When(priority="normal", then=2),
            default=3,
            output_field=models.IntegerField(),
        ),
        "-created_at",
    )[:5]

    # Get faculty tabs and organize faculty by department
    faculty_tabs = FacultyTab.objects.filter(is_active=True)
    faculty_by_tab = {}
    for tab in faculty_tabs:
        faculty_by_tab[tab.slug] = Faculty.objects.filter(
            department=tab.department_filter, is_active=True
        )

    # Check for graduate programs (programs with "graduate" or "master" in name)
    has_graduate_programs = (
        Program.objects.filter(is_active=True)
        .filter(
            models.Q(full_name__icontains="master")
            | models.Q(full_name__icontains="graduate")
            | models.Q(full_name__icontains="phd")
            | models.Q(full_name__icontains="doctoral")
        )
        .exists()
    )

    context = {
        "site_config": SiteConfiguration.objects.filter(is_active=True).first(),
        "hero_slides": HeroSection.objects.filter(is_active=True),
        "hero": HeroSection.objects.filter(is_active=True).first(),
        "spotlight_images": GalleryImage.objects.filter(is_spotlight=True).order_by("?")[:8],
        "gallery_slides": ImageSlideshow.objects.filter(
            display_location="homepage_gallery", is_active=True
        ),
        "marquee_items": MarqueeItem.objects.filter(is_active=True),
        "marquee_notices": marquee_notices,
        "notices": Notice.objects.filter(is_active=True)[:3],
        "events": Event.objects.filter(is_active=True)[:3],
        "programs": Program.objects.filter(is_active=True),
        "faculty_tabs": faculty_tabs,
        "faculty_by_tab": faculty_by_tab,
        "has_graduate_programs": has_graduate_programs,
        "principal_message": PrincipalMessage.objects.filter(is_active=True).first(),
        "contact_info": ContactInfo.objects.filter(is_active=True).first(),
        "site_logo": SiteLogo.objects.filter(is_active=True).first(),
    }
    return render(request, "home/index.html", context)


def gallery_page(request):
    """Public gallery page - Lists Albums"""
    albums = GalleryAlbum.objects.all().order_by("display_order", "-created_at")
    return render(request, "home/gallery.html", {"albums": albums})


def gallery_album_detail(request, pk):
    """View images in a specific album"""
    album = get_object_or_404(GalleryAlbum, pk=pk)
    images = album.images.all().order_by("display_order", "-created_at")
    
    # Pagination
    paginator = Paginator(images, 12)
    page = request.GET.get("page")
    try:
        gallery_images = paginator.page(page)
    except PageNotAnInteger:
        gallery_images = paginator.page(1)
    except EmptyPage:
        gallery_images = paginator.page(paginator.num_pages)

    return render(
        request, 
        "home/gallery_album_detail.html", 
        {"album": album, "gallery_images": gallery_images}
    )


def curriculum_page(request, slug):
    """Dynamic curriculum page for any program"""
    # Get program by URL slug
    program = get_object_or_404(Program, url_slug=slug, is_active=True)

    # Get curriculum for this program
    curriculum = Curriculum.objects.filter(program=program, is_active=True).first()

    # Get semesters and courses
    semesters = (
        CurriculumSemester.objects.filter(curriculum=curriculum)
        .prefetch_related("courses")
        .order_by("semester_number")
        if curriculum
        else []
    )

    # Get career prospects
    career_prospects = (
        curriculum.career_prospects.all().order_by("display_order") if curriculum else []
    )

    context = {
        "program": program,
        "curriculum": curriculum,
        "semesters": semesters,
        "career_prospects": career_prospects,
    }

    # Determine template based on program code or use generic
    template_map = {
        "BIT": "home/bit.html",
        "AG": "home/agriculture.html",
    }
    template = template_map.get(program.code, "home/curriculum_detail.html")

    return render(request, template, context)


def bit(request):
    """BIT curriculum page - redirect to dynamic view"""
    return curriculum_page(request, "bit")


def agriculture(request):
    """Agriculture curriculum page - redirect to dynamic view"""
    return curriculum_page(request, "agriculture")


def faculty_detail(request, pk):
    """View individual faculty member details"""
    faculty = get_object_or_404(Faculty, pk=pk, is_active=True)
    # Get related faculty from same department
    related_faculty = (
        Faculty.objects.filter(department=faculty.department, is_active=True)
        .exclude(pk=pk)
        .order_by("display_order")[:3]
    )

    context = {
        "faculty": faculty,
        "related_faculty": related_faculty,
    }
    return render(request, "home/faculty_detail.html", context)


@login_required
def manage_account(request):
    """Manage account page - under construction"""
    return render(request, "home/manage_account.html")


# Error handlers
def error_403(request, exception=None):
    """403 Forbidden error handler"""
    return render(request, "403.html", status=403)


def error_404(request, exception=None):
    """404 Not Found error handler"""
    return render(request, "404.html", status=404)


def error_500(request):
    """500 Internal Server Error handler"""
    return render(request, "500.html", status=500)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def notices_page(request):
    """Public notices page - list all notices"""
    query = request.GET.get('q')
    notices_list = Notice.objects.filter(is_active=True).order_by(
        'display_order',
        models.Case(
            models.When(priority="urgent", then=0),
            models.When(priority="highlight", then=1),
            models.When(priority="normal", then=2),
            default=3,
            output_field=models.IntegerField(),
        ),
        "-created_at",
    )

    if query:
        notices_list = notices_list.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(notices_list, 10)  # Show 10 notices per page
    page = request.GET.get('page')
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    context = {
        "notices": notices,
        'query': query,
    }
    return render(request, "home/notices.html", context)


def events_page(request):
    """View all events"""
    events = Event.objects.filter(is_active=True).order_by("-is_highlight", "-created_at")
    context = {
        "events": events,
    }
    return render(request, "home/events.html", context)


def event_detail(request, pk):
    """View individual event details"""
    event = get_object_or_404(Event, pk=pk, is_active=True)
    # Get related events (highlighted or recent)
    related_events = (
        Event.objects.filter(is_active=True)
        .exclude(pk=pk)
        .order_by("-is_highlight", "-created_at")[:3]
    )

    context = {
        "event": event,
        "related_events": related_events,
    }
    return render(request, "home/event_detail.html", context)


def notice_detail(request, pk):
    """View individual notice details"""
    notice = get_object_or_404(Notice, pk=pk, is_active=True)
    # Get related notices (same priority or recent)
    related_notices = (
        Notice.objects.filter(is_active=True).exclude(pk=pk).order_by("-created_at")[:3]
    )

    context = {
        "notice": notice,
        "related_notices": related_notices,
    }
    return render(request, "home/notice_detail.html", context)


# ============= ADMIN DASHBOARD VIEWS =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    """Admin dashboard view - requires staff permission"""
    context = {
        "total_notices": Notice.objects.count(),
        "total_events": Event.objects.count(),
        "total_faculty": Faculty.objects.count(),
        "total_programs": Program.objects.count(),
        "recent_messages": ContactMessage.objects.order_by("-submitted_at")[:5],
    }
    return render(request, "home/admin_dashboard.html", context)


# ============= NOTICE MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def notice_list(request):
    """List all notices"""
    notices = Notice.objects.all().order_by("display_order", "-date_bs", "-created_at")
    return render(request, "home/admin/notice_list.html", {"notices": notices})


@login_required
@user_passes_test(lambda u: u.is_staff)
def notice_add(request):
    """Add new notice"""
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice created successfully!")
            return redirect("home:notice_list")
    else:
        form = NoticeForm()

    return render(
        request, "home/admin/notice_form.html", {"form": form, "title": "Add Notice"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def notice_edit(request, pk):
    """Edit existing notice"""
    notice = get_object_or_404(Notice, pk=pk)

    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice updated successfully!")
            return redirect("home:notice_list")
    else:
        form = NoticeForm(instance=notice)

    return render(
        request,
        "home/admin/notice_form.html",
        {"form": form, "title": "Edit Notice", "notice": notice},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def notice_delete(request, pk):
    """Delete notice"""
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    messages.success(request, "Notice deleted successfully!")
    return redirect("home:notice_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def notice_reorder(request):
    """Reorder notices via AJAX"""
    import json
    from django.http import JsonResponse

    try:
        data = json.loads(request.body)
        order = data.get("order", [])
        
        if not order:
            return JsonResponse({"status": "error", "message": "No order provided"}, status=400)

        # Update display_order for each item
        for index, pk in enumerate(order):
            Notice.objects.filter(pk=pk).update(display_order=index)

        return JsonResponse({"status": "success", "message": "Order updated successfully"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


# ============= EVENT MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def event_list(request):
    """List all events"""
    events = Event.objects.all().order_by("-created_at")
    return render(request, "home/admin/event_list.html", {"events": events})


@login_required
@user_passes_test(lambda u: u.is_staff)
def event_add(request):
    """Add new event"""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("home:event_list")
    else:
        form = EventForm()

    return render(
        request, "home/admin/event_form.html", {"form": form, "title": "Add Event"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def event_edit(request, pk):
    """Edit existing event"""
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect("home:event_list")
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "home/admin/event_form.html",
        {"form": form, "title": "Edit Event", "event": event},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def event_delete(request, pk):
    """Delete event"""
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect("home:event_list")


# ============= FACULTY MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_list(request):
    """List all faculty members"""
    faculty = Faculty.objects.all().order_by("department", "display_order")
    return render(request, "home/admin/faculty_list.html", {"faculty": faculty})


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_add(request):
    """Add new faculty member"""
    if request.method == "POST":
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty member added successfully!")
            return redirect("home:faculty_list")
    else:
        form = FacultyForm()

    return render(
        request, "home/admin/faculty_form.html", {"form": form, "title": "Add Faculty"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_edit(request, pk):
    """Edit existing faculty member"""
    faculty = get_object_or_404(Faculty, pk=pk)

    if request.method == "POST":
        form = FacultyForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty member updated successfully!")
            return redirect("home:faculty_list")
    else:
        form = FacultyForm(instance=faculty)

    return render(
        request,
        "home/admin/faculty_form.html",
        {"form": form, "title": "Edit Faculty", "faculty": faculty},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def faculty_delete(request, pk):
    """Delete faculty member"""
    faculty = get_object_or_404(Faculty, pk=pk)
    faculty.delete()
    messages.success(request, "Faculty member deleted successfully!")
    return redirect("home:faculty_list")


# ============= FACULTY TAB MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_tab_list(request):
    """List all faculty tabs"""
    from .models import FacultyTab

    tabs = FacultyTab.objects.all()
    return render(request, "home/admin/faculty_tab_list.html", {"tabs": tabs})


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_tab_add(request):
    """Add new faculty tab"""
    from .forms import FacultyTabForm

    if request.method == "POST":
        form = FacultyTabForm(request.POST)
        if form.is_valid():
            tab = form.save()
            messages.success(request, f"Faculty tab '{tab.name}' created!")
            return redirect("home:faculty_tab_list")
    else:
        form = FacultyTabForm()

    return render(
        request,
        "home/admin/faculty_tab_form.html",
        {"form": form, "title": "Add Faculty Tab"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def faculty_tab_edit(request, pk):
    """Edit faculty tab"""
    from .forms import FacultyTabForm
    from .models import FacultyTab

    tab = get_object_or_404(FacultyTab, pk=pk)

    if request.method == "POST":
        form = FacultyTabForm(request.POST, instance=tab)
        if form.is_valid():
            form.save()
            messages.success(request, f"Faculty tab '{tab.name}' updated!")
            return redirect("home:faculty_tab_list")
    else:
        form = FacultyTabForm(instance=tab)

    return render(
        request,
        "home/admin/faculty_tab_form.html",
        {"form": form, "tab": tab, "title": f"Edit {tab.name}"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def faculty_tab_delete(request, pk):
    """Delete faculty tab"""
    from .models import FacultyTab

    tab = get_object_or_404(FacultyTab, pk=pk)
    tab_name = tab.name
    tab.delete()
    messages.success(request, f"Faculty tab '{tab_name}' deleted!")
    return redirect("home:faculty_tab_list")


# ============= PAGE CONTENT MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def page_content(request):
    """Manage page content (hero, marquee, principal message, contact info)"""
    hero = HeroSection.objects.filter(is_active=True).first()
    marquee_items = MarqueeItem.objects.all().order_by("display_order")
    principal_message = PrincipalMessage.objects.filter(is_active=True).first()
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    site_logo = SiteLogo.objects.filter(is_active=True).first()

    return render(
        request,
        "home/admin/page_content.html",
        {
            "hero": hero,
            "marquee_items": marquee_items,
            "principal_message": principal_message,
            "contact_info": contact_info,
            "site_logo": site_logo,
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def hero_list(request):
    """List all hero slides"""
    slides = HeroSection.objects.all().order_by("display_order", "-created_at")
    return render(request, "home/admin/hero_list.html", {"slides": slides})


@login_required
@user_passes_test(lambda u: u.is_staff)
def hero_add(request):
    """Add new hero slide"""
    if request.method == "POST":
        form = HeroSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Hero slide added successfully!")
            return redirect("home:hero_list")
    else:
        form = HeroSectionForm()

    return render(
        request, "home/admin/hero_form.html", {"form": form, "title": "Add Hero Slide"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def hero_edit(request, pk):
    """Edit hero slide"""
    hero = get_object_or_404(HeroSection, pk=pk)

    if request.method == "POST":
        form = HeroSectionForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            messages.success(request, "Hero slide updated successfully!")
            return redirect("home:hero_list")
    else:
        form = HeroSectionForm(instance=hero)

    return render(
        request, "home/admin/hero_form.html", {"form": form, "title": "Edit Hero Slide"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def hero_delete(request, pk):
    """Delete hero slide"""
    hero = get_object_or_404(HeroSection, pk=pk)
    hero.delete()
    messages.success(request, "Hero slide deleted successfully!")
    return redirect("home:hero_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def marquee_add(request):
    """Add marquee item"""
    if request.method == "POST":
        form = MarqueeItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marquee item added successfully!")
            return redirect("home:page_content")
    else:
        form = MarqueeItemForm()

    return render(
        request, "home/admin/marquee_form.html", {"form": form, "title": "Add Marquee Item"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def marquee_edit(request, pk):
    """Edit marquee item"""
    marquee = get_object_or_404(MarqueeItem, pk=pk)

    if request.method == "POST":
        form = MarqueeItemForm(request.POST, instance=marquee)
        if form.is_valid():
            form.save()
            messages.success(request, "Marquee item updated successfully!")
            return redirect("home:page_content")
    else:
        form = MarqueeItemForm(instance=marquee)

    return render(
        request,
        "home/admin/marquee_form.html",
        {"form": form, "title": "Edit Marquee Item", "marquee": marquee},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def marquee_delete(request, pk):
    """Delete marquee item"""
    marquee = get_object_or_404(MarqueeItem, pk=pk)
    marquee.delete()
    messages.success(request, "Marquee item deleted successfully!")
    return redirect("home:page_content")


@login_required
@user_passes_test(lambda u: u.is_staff)
def principal_message_edit(request):
    """Edit principal message"""
    principal_message = PrincipalMessage.objects.filter(is_active=True).first()

    if request.method == "POST":
        form = PrincipalMessageForm(request.POST, request.FILES, instance=principal_message)
        if form.is_valid():
            # Deactivate all other principal messages
            PrincipalMessage.objects.all().update(is_active=False)
            form.save()
            messages.success(request, "Principal message updated successfully!")
            return redirect("home:page_content")
    else:
        form = PrincipalMessageForm(instance=principal_message)

    return render(
        request,
        "home/admin/principal_message_form.html",
        {"form": form, "title": "Edit Principal Message"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def contact_info_edit(request):
    """Edit contact information"""
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    if request.method == "POST":
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            # Deactivate all other contact info
            ContactInfo.objects.all().update(is_active=False)
            form.save()
            messages.success(request, "Contact information updated successfully!")
            return redirect("home:page_content")
    else:
        form = ContactInfoForm(instance=contact_info)

    return render(
        request,
        "home/admin/contact_info_form.html",
        {"form": form, "title": "Edit Contact Information"},
    )


# ============= CONTACT MESSAGES =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def message_list(request):
    """List all contact messages"""
    messages_list = ContactMessage.objects.all().order_by("-submitted_at")
    return render(request, "home/admin/message_list.html", {"messages_list": messages_list})


@login_required
@user_passes_test(lambda u: u.is_staff)
def message_view(request, pk):
    """View contact message details"""
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()

    return render(request, "home/admin/message_view.html", {"message": message})


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def message_delete(request, pk):
    """Delete contact message"""
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    messages.success(request, "Message deleted successfully!")
    return redirect("home:message_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def logo_edit(request):
    """Edit site logo"""
    logo = SiteLogo.objects.filter(is_active=True).first()

    if request.method == "POST":
        form = SiteLogoForm(request.POST, request.FILES, instance=logo)
        if form.is_valid():
            # Deactivate all other logos
            SiteLogo.objects.all().update(is_active=False)
            form.save()
            messages.success(request, "Logo updated successfully!")
            return redirect("home:page_content")
    else:
        form = SiteLogoForm(instance=logo)

    return render(
        request,
        "home/admin/logo_form.html",
        {"form": form, "logo": logo, "title": "Edit Site Logo"},
    )


# ============= CURRICULUM MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def curriculum_list(request):
    """List all curriculum pages"""
    curriculums = Curriculum.objects.all().prefetch_related("semesters__courses")
    return render(request, "home/admin/curriculum_list.html", {"curriculums": curriculums})


@login_required
@user_passes_test(lambda u: u.is_staff)
def curriculum_add(request):
    """Add new curriculum"""
    from .forms import CurriculumForm

    if request.method == "POST":
        form = CurriculumForm(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save()
            messages.success(
                request, f"{curriculum.program} curriculum created successfully!"
            )
            return redirect("home:curriculum_list")
    else:
        form = CurriculumForm()

    return render(
        request,
        "home/admin/curriculum_form.html",
        {"form": form, "title": "Add New Curriculum"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def curriculum_edit(request, pk):
    """Edit curriculum page"""
    from .forms import CurriculumForm

    curriculum = get_object_or_404(Curriculum, pk=pk)

    if request.method == "POST":
        form = CurriculumForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            form.save()
            messages.success(request, f"{curriculum.program} curriculum updated!")
            return redirect("home:curriculum_list")
    else:
        form = CurriculumForm(instance=curriculum)

    context = {
        "form": form,
        "curriculum": curriculum,
        "title": f"Edit {curriculum.program} Curriculum",
    }
    return render(request, "home/admin/curriculum_form.html", context)


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def curriculum_delete(request, pk):
    """Delete curriculum"""
    curriculum = get_object_or_404(Curriculum, pk=pk)
    program_name = str(curriculum.program)
    curriculum.delete()
    messages.success(request, f"{program_name} curriculum deleted successfully!")
    return redirect("home:curriculum_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def semester_add(request, curriculum_pk):
    """Add semester to curriculum"""
    from .forms import CurriculumSemesterForm

    curriculum = get_object_or_404(Curriculum, pk=curriculum_pk)

    if request.method == "POST":
        form = CurriculumSemesterForm(request.POST)
        if form.is_valid():
            semester = form.save(commit=False)
            semester.curriculum = curriculum
            semester.save()
            messages.success(request, "Semester added successfully!")
            return redirect("home:curriculum_list")
    else:
        form = CurriculumSemesterForm(initial={"curriculum": curriculum})

    return render(
        request,
        "home/admin/semester_form.html",
        {
            "form": form,
            "curriculum": curriculum,
            "title": f"Add Semester to {curriculum.program}",
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def semester_edit(request, pk):
    """Edit semester"""
    from .forms import CurriculumSemesterForm

    semester = get_object_or_404(CurriculumSemester, pk=pk)

    if request.method == "POST":
        form = CurriculumSemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            messages.success(request, "Semester updated successfully!")
            return redirect("home:curriculum_list")
    else:
        form = CurriculumSemesterForm(instance=semester)

    return render(
        request,
        "home/admin/semester_form.html",
        {
            "form": form,
            "semester": semester,
            "title": f"Edit Semester {semester.semester_number}",
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def semester_delete(request, pk):
    """Delete semester"""
    semester = get_object_or_404(CurriculumSemester, pk=pk)
    semester.delete()
    messages.success(request, "Semester deleted successfully!")
    return redirect("home:curriculum_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def course_add(request, semester_pk):
    """Add course to semester"""
    from .forms import CourseForm

    semester = get_object_or_404(CurriculumSemester, pk=semester_pk)

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.semester = semester
            course.save()
            messages.success(request, "Course added successfully!")
            return redirect("home:curriculum_list")
    else:
        form = CourseForm(initial={"semester": semester})

    return render(
        request,
        "home/admin/course_form.html",
        {
            "form": form,
            "semester": semester,
            "title": f"Add Course to Semester {semester.semester_number}",
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def course_edit(request, pk):
    """Edit course"""
    from .forms import CourseForm

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect("home:curriculum_list")
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "home/admin/course_form.html",
        {"form": form, "course": course, "title": f"Edit {course.code}"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def course_delete(request, pk):
    """Delete course"""
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect("home:curriculum_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_list(request):
    """List all programs with features"""
    programs = Program.objects.prefetch_related("features").all()
    return render(request, "home/admin/program_list.html", {"programs": programs})


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_add(request):
    """Add new program"""
    from .forms import ProgramForm

    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.save()
            messages.success(request, f"{program.full_name} created successfully!")
            return redirect("home:program_list")
    else:
        form = ProgramForm()

    return render(
        request,
        "home/admin/program_form.html",
        {"form": form, "title": "Add New Program"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_edit(request, pk):
    """Edit program"""
    from .forms import ProgramForm

    program = get_object_or_404(Program, pk=pk)

    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, f"{program.full_name} updated!")
            return redirect("home:program_list")
    else:
        form = ProgramForm(instance=program)

    return render(
        request,
        "home/admin/program_form.html",
        {"form": form, "program": program, "title": f"Edit {program.code}"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def program_delete(request, pk):
    """Delete program"""
    program = get_object_or_404(Program, pk=pk)
    program_name = program.full_name
    program.delete()
    messages.success(request, f"{program_name} deleted successfully!")
    return redirect("home:program_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_feature_add(request, program_pk):
    """Add feature to program"""
    from .forms import ProgramFeatureForm

    program = get_object_or_404(Program, pk=program_pk)

    if request.method == "POST":
        form = ProgramFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.program = program
            feature.save()
            messages.success(request, "Feature added successfully!")
            return redirect("home:program_list")
    else:
        form = ProgramFeatureForm(initial={"program": program})

    return render(
        request,
        "home/admin/program_feature_form.html",
        {
            "form": form,
            "program": program,
            "title": f"Add Feature to {program.code}",
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_feature_edit(request, pk):
    """Edit program feature"""
    from .forms import ProgramFeatureForm

    feature = get_object_or_404(ProgramFeature, pk=pk)

    if request.method == "POST":
        form = ProgramFeatureForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            messages.success(request, "Feature updated successfully!")
            return redirect("home:program_list")
    else:
        form = ProgramFeatureForm(instance=feature)

    return render(
        request,
        "home/admin/program_feature_form.html",
        {"form": form, "feature": feature, "title": "Edit Feature"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def program_feature_delete(request, pk):
    """Delete program feature"""
    feature = get_object_or_404(ProgramFeature, pk=pk)
    feature.delete()
    messages.success(request, "Feature deleted successfully!")
    return redirect("home:program_list")


# Site Configuration Views
@login_required
@user_passes_test(lambda u: u.is_staff)
def site_configuration_edit(request):
    """Edit site configuration"""
    from .forms import SiteConfigurationForm
    from .models import SiteConfiguration

    config = SiteConfiguration.objects.filter(is_active=True).first()
    if not config:
        config = SiteConfiguration.objects.create()

    if request.method == "POST":
        form = SiteConfigurationForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, "Site configuration updated successfully!")
            return redirect("home:admin_dashboard")
    else:
        form = SiteConfigurationForm(instance=config)

    return render(
        request,
        "home/admin/site_config_form.html",
        {"form": form, "title": "Edit Site Configuration"},
    )


# ============= FOOTER LINK MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def footer_link_list(request):
    """List all footer links"""
    links = FooterLink.objects.all().order_by("display_order")
    return render(request, "home/admin/footer_link_list.html", {"links": links})


@login_required
@user_passes_test(lambda u: u.is_staff)
def footer_link_add(request):
    """Add new footer link"""
    if request.method == "POST":
        form = FooterLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Footer link created successfully!")
            return redirect("home:footer_link_list")
    else:
        form = FooterLinkForm()

    return render(
        request, "home/admin/footer_link_form.html", {"form": form, "title": "Add Footer Link"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def footer_link_edit(request, pk):
    """Edit existing footer link"""
    link = get_object_or_404(FooterLink, pk=pk)

    if request.method == "POST":
        form = FooterLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, "Footer link updated successfully!")
            return redirect("home:footer_link_list")
    else:
        form = FooterLinkForm(instance=link)

    return render(
        request,
        "home/admin/footer_link_form.html",
        {"form": form, "title": "Edit Footer Link", "link": link},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def footer_link_delete(request, pk):
    """Delete footer link"""
    link = get_object_or_404(FooterLink, pk=pk)
    link.delete()
    messages.success(request, "Footer link deleted successfully!")
    return redirect("home:footer_link_list")


# Image Slideshow Views
@login_required
@user_passes_test(lambda u: u.is_staff)
def slideshow_list(request):
    """List all slideshows"""
    from .models import ImageSlideshow

    slideshows = ImageSlideshow.objects.all()
    return render(
        request,
        "home/admin/slideshow_list.html",
        {"slideshows": slideshows, "title": "Image Slideshows"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def slideshow_add(request):
    """Add new slideshow image"""
    from .forms import ImageSlideshowForm

    if request.method == "POST":
        form = ImageSlideshowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Slideshow image added successfully!")
            return redirect("home:slideshow_list")
    else:
        form = ImageSlideshowForm()

    return render(
        request,
        "home/admin/slideshow_form.html",
        {"form": form, "title": "Add Slideshow Image"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def slideshow_edit(request, pk):
    """Edit slideshow image"""
    from .forms import ImageSlideshowForm
    from .models import ImageSlideshow

    slideshow = get_object_or_404(ImageSlideshow, pk=pk)
    if request.method == "POST":
        form = ImageSlideshowForm(request.POST, request.FILES, instance=slideshow)
        if form.is_valid():
            form.save()
            messages.success(request, "Slideshow image updated successfully!")
            return redirect("home:slideshow_list")
    else:
        form = ImageSlideshowForm(instance=slideshow)

    return render(
        request,
        "home/admin/slideshow_form.html",
        {"form": form, "title": "Edit Slideshow Image"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def slideshow_delete(request, pk):
    """Delete slideshow image"""
    from .models import ImageSlideshow

    slideshow = get_object_or_404(ImageSlideshow, pk=pk)
    slideshow.delete()
    messages.success(request, "Slideshow image deleted successfully!")
    return redirect("home:slideshow_list")


# About Section Views
@login_required
@user_passes_test(lambda u: u.is_staff)
def about_section_list(request):
    """List all about sections"""
    from .models import AboutSection

    sections = AboutSection.objects.all()
    return render(
        request,
        "home/admin/about_section_list.html",
        {"sections": sections, "title": "About Sections"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def about_section_add(request):
    """Add new about section"""
    from .forms import AboutSectionForm

    if request.method == "POST":
        form = AboutSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "About section added successfully!")
            return redirect("home:about_section_list")
    else:
        form = AboutSectionForm()

    return render(
        request,
        "home/admin/about_section_form.html",
        {"form": form, "title": "Add About Section"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def about_section_edit(request, pk):
    """Edit about section"""
    from .forms import AboutSectionForm
    from .models import AboutSection

    section = get_object_or_404(AboutSection, pk=pk)
    if request.method == "POST":
        form = AboutSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, "About section updated successfully!")
            return redirect("home:about_section_list")
    else:
        form = AboutSectionForm(instance=section)

    return render(
        request,
        "home/admin/about_section_form.html",
        {"form": form, "title": "Edit About Section"},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def about_section_delete(request, pk):
    """Delete about section"""
    from .models import AboutSection

    section = get_object_or_404(AboutSection, pk=pk)
    section.delete()
    messages.success(request, "About section deleted successfully!")
    return redirect("home:about_section_list")


# Public About Page
def about_page(request):
    """Public about us page"""
    from .models import AboutSection, SiteConfiguration

    site_config = SiteConfiguration.objects.filter(is_active=True).first()
    sections = AboutSection.objects.filter(is_active=True)

    return render(
        request,
        "home/about.html",
        {
            "site_config": site_config,
            "sections": sections,
            "contact_info": ContactInfo.objects.filter(is_active=True).first(),
            "site_logo": SiteLogo.objects.filter(is_active=True).first(),
        },
    )


# ============= GALLERY ALBUM MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def album_list(request):
    """List all gallery albums"""
    albums = GalleryAlbum.objects.all().order_by("display_order", "-created_at")
    return render(request, "home/admin/album_list.html", {"albums": albums})


@login_required
@user_passes_test(lambda u: u.is_staff)
def album_add(request):
    """Add new album"""
    if request.method == "POST":
        form = GalleryAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Album created successfully!")
            return redirect("home:album_list")
    else:
        form = GalleryAlbumForm()

    return render(
        request, "home/admin/album_form.html", {"form": form, "title": "Add Album"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def album_edit(request, pk):
    """Edit album"""
    album = get_object_or_404(GalleryAlbum, pk=pk)

    if request.method == "POST":
        form = GalleryAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, "Album updated!")
            return redirect("home:album_list")
    else:
        form = GalleryAlbumForm(instance=album)

    return render(
        request,
        "home/admin/album_form.html",
        {"form": form, "title": "Edit Album", "album": album},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def album_delete(request, pk):
    """Delete album"""
    album = get_object_or_404(GalleryAlbum, pk=pk)
    album.delete()
    messages.success(request, "Album deleted!")
    return redirect("home:album_list")


# ============= GALLERY MANAGEMENT =============


@login_required
@user_passes_test(lambda u: u.is_staff)
def gallery_list(request):
    """List all gallery images"""
    filter_type = request.GET.get("filter")
    images = GalleryImage.objects.all()
    title = "Manage Photo Gallery"

    if filter_type == "spotlight":
        images = images.filter(is_spotlight=True)
        title = "Manage Spotlight Images"

    images = images.order_by("display_order", "-created_at")
    return render(
        request,
        "home/admin/gallery_list.html",
        {"images": images, "title": title, "filter": filter_type},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def gallery_add(request):
    """Add new gallery image"""
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image added to gallery!")
            return redirect("home:gallery_list")
    else:
        form = GalleryImageForm()

    return render(
        request, "home/admin/gallery_form.html", {"form": form, "title": "Add Gallery Image"}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def gallery_edit(request, pk):
    """Edit gallery image"""
    image = get_object_or_404(GalleryImage, pk=pk)

    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Gallery image updated!")
            return redirect("home:gallery_list")
    else:
        form = GalleryImageForm(instance=image)

    return render(
        request,
        "home/admin/gallery_form.html",
        {"form": form, "title": "Edit Gallery Image", "image": image},
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def gallery_delete(request, pk):
    """Delete gallery image"""
    image = get_object_or_404(GalleryImage, pk=pk)
    image.delete()
    messages.success(request, "Gallery image deleted!")
    return redirect("home:gallery_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def gallery_reorder(request):
    """Reorder gallery images via AJAX"""
    import json
    from django.http import JsonResponse

    try:
        data = json.loads(request.body)
        order = data.get("order", [])
        
        if not order:
            return JsonResponse({"status": "error", "message": "No order provided"}, status=400)

        # Update display_order for each item
        for index, pk in enumerate(order):
            GalleryImage.objects.filter(pk=pk).update(display_order=index)

        return JsonResponse({"status": "success", "message": "Order updated successfully"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
