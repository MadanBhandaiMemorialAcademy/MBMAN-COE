from django.contrib import admin

from .models import (
    CareerProspect,
    ContactInfo,
    ContactMessage,
    Course,
    Curriculum,
    CurriculumSemester,
    Event,
    Faculty,
    HeroSection,
    MarqueeItem,
    Notice,
    PrincipalMessage,
    Program,
    ProgramFeature,
    SiteLogo,
)


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["title", "date_bs", "priority", "is_active", "created_at"]
    list_filter = ["priority", "is_active", "created_at"]
    search_fields = ["title", "description"]
    list_editable = ["is_active"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Notice Information", {"fields": ("title", "description", "date_bs", "priority")}),
        ("File Attachment", {"fields": ("file",), "classes": ("collapse",)}),
        ("Status", {"fields": ("is_active",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date_bs", "time", "location", "is_highlight", "is_active"]
    list_filter = ["is_highlight", "is_active", "created_at"]
    search_fields = ["title", "description", "location"]
    list_editable = ["is_highlight", "is_active"]
    ordering = ["-created_at"]

    fieldsets = (
        (
            "Event Information",
            {"fields": ("title", "description", "date_bs", "time", "location")},
        ),
        ("Display Options", {"fields": ("is_highlight", "is_active")}),
    )


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["name", "designation", "department", "is_active", "display_order"]
    list_filter = ["department", "is_active"]
    search_fields = ["name", "designation", "qualification"]
    list_editable = ["is_active", "display_order"]
    ordering = ["display_order", "name"]

    fieldsets = (
        (
            "Personal Information",
            {"fields": ("name", "photo", "email", "phone", "website")},
        ),
        (
            "Professional Details",
            {"fields": ("designation", "department", "qualification", "bio")},
        ),
        ("Display Settings", {"fields": ("is_active", "display_order")}),
    )


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    list_editable = ["is_active"]

    fieldsets = (
        ("Content", {"fields": ("title", "subtitle", "background_image")}),
        ("Call to Action", {"fields": ("cta_text", "cta_link")}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(MarqueeItem)
class MarqueeItemAdmin(admin.ModelAdmin):
    list_display = ["text", "is_new", "is_urgent", "is_active", "display_order"]
    list_filter = ["is_new", "is_urgent", "is_active"]
    search_fields = ["text"]
    list_editable = ["is_new", "is_urgent", "is_active", "display_order"]
    ordering = ["display_order"]


@admin.register(PrincipalMessage)
class PrincipalMessageAdmin(admin.ModelAdmin):
    list_display = ["principal_name", "principal_title", "is_active"]
    list_editable = ["is_active"]

    fieldsets = (
        (
            "Principal Information",
            {"fields": ("principal_name", "principal_title", "photo")},
        ),
        ("Message", {"fields": ("quote", "full_message")}),
        ("Status", {"fields": ("is_active",)}),
    )


class ProgramFeatureInline(admin.TabularInline):
    model = ProgramFeature
    extra = 1
    fields = ["feature_text", "icon", "display_order"]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["code", "full_name", "duration", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["code", "full_name", "short_description"]
    list_editable = ["is_active"]
    inlines = [ProgramFeatureInline]

    fieldsets = (
        ("Basic Information", {"fields": ("code", "full_name", "duration")}),
        ("Description", {"fields": ("short_description", "full_description")}),
        ("Media", {"fields": ("image", "brochure")}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "is_active"]
    list_editable = ["is_active"]

    fieldsets = (
        ("Contact Details", {"fields": ("phone", "email", "address")}),
        (
            "Social Media",
            {"fields": ("facebook_url", "twitter_url", "linkedin_url", "youtube_url")},
        ),
        ("Map", {"fields": ("map_embed_url",)}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "submitted_at", "is_read"]
    list_filter = ["is_read", "submitted_at"]
    search_fields = ["name", "email", "message"]
    list_editable = ["is_read"]
    ordering = ["-submitted_at"]
    readonly_fields = ["name", "email", "message", "submitted_at"]

    def has_add_permission(self, request):
        return False


@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ["logo_text", "is_active"]
    list_editable = ["is_active"]

    fieldsets = (
        ("Logo", {"fields": ("logo",)}),
        ("Text", {"fields": ("logo_text", "logo_subtext")}),
        ("Status", {"fields": ("is_active",)}),
    )

    def has_add_permission(self, request):
        # Only allow one logo
        return not SiteLogo.objects.exists()


class CourseInline(admin.TabularInline):
    model = Course
    extra = 1
    fields = ["code", "title", "credits", "display_order"]
    ordering = ["display_order", "code"]


class CurriculumSemesterInline(admin.StackedInline):
    model = CurriculumSemester
    extra = 0
    fields = ["semester_number", "description", "display_order"]
    ordering = ["semester_number"]


class CareerProspectInline(admin.TabularInline):
    model = CareerProspect
    extra = 1
    fields = ["title", "icon", "display_order"]
    ordering = ["display_order"]


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ["program", "duration", "is_active"]
    list_editable = ["is_active"]
    inlines = [CurriculumSemesterInline, CareerProspectInline]

    fieldsets = (
        ("Program Information", {"fields": ("program", "duration")}),
        ("Content", {"fields": ("overview_text", "hero_image")}),
        ("Status", {"fields": ("is_active",)}),
    )

    def has_add_permission(self, request):
        # Only allow BIT and AG
        return Curriculum.objects.count() < 2


@admin.register(CurriculumSemester)
class CurriculumSemesterAdmin(admin.ModelAdmin):
    list_display = ["curriculum", "semester_number", "display_order"]
    list_filter = ["curriculum"]
    ordering = ["curriculum", "semester_number"]
    inlines = [CourseInline]

    fieldsets = (
        ("Semester Information", {"fields": ("curriculum", "semester_number")}),
        ("Content", {"fields": ("description", "display_order")}),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "title", "semester", "credits", "display_order"]
    list_filter = ["semester__curriculum", "semester__semester_number"]
    search_fields = ["code", "title"]
    ordering = [
        "semester__curriculum",
        "semester__semester_number",
        "display_order",
        "code",
    ]

    fieldsets = (
        ("Course Information", {"fields": ("semester", "code", "title", "credits")}),
        ("Details", {"fields": ("description", "display_order")}),
    )


@admin.register(CareerProspect)
class CareerProspectAdmin(admin.ModelAdmin):
    list_display = ["curriculum", "title", "icon", "display_order"]
    list_filter = ["curriculum"]
    ordering = ["curriculum", "display_order"]

    fieldsets = (
        ("Career Information", {"fields": ("curriculum", "title")}),
        ("Display", {"fields": ("icon", "display_order")}),
    )
