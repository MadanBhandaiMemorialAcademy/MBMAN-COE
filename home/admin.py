from django.contrib import admin

from .models import (
    CareerProspect,
    ContactInfo,
    ContactMessage,
    Course,
    Curriculum,
    CurriculumSemester,
    Department,
    Event,
    Faculty,
    FacultyTab,
    FooterLink,
    HeroSection,
    MarqueeItem,
    Notice,
    PrincipalMessage,
    Program,
    ProgramFeature,
    SiteConfiguration,
    SiteLogo,
)


from admin_ordering.admin import OrderableAdmin

from adminsortable2.admin import SortableAdminMixin

@admin.register(Notice)
class NoticeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["title", "date_bs", "priority", "is_active", "display_order", "created_at"]
    list_filter = ["priority", "is_active", "created_at"]
    search_fields = ["title", "description"]
    list_editable = ["is_active"]
    ordering = ["display_order", "-created_at"]
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
    list_display = ["title", "is_active", "display_order"]
    list_editable = ["is_active", "display_order"]

    fieldsets = (
        ("Content", {"fields": ("title", "subtitle", "background_image")}),
        ("Call to Action", {"fields": ("cta_text", "cta_link")}),
        ("Status", {"fields": ("is_active", "display_order")}),
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


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["code", "degree_level", "full_name", "duration", "is_active"]
    list_filter = ["is_active", "degree_level"]
    search_fields = ["code", "full_name", "short_description"]
    list_editable = ["is_active"]

    fieldsets = (
        ("Basic Information", {"fields": ("code", "degree_level", "full_name", "duration")}),
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


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ["program", "duration", "is_active"]
    list_editable = ["is_active"]

    fieldsets = (
        ("Program Information", {"fields": ("program", "duration")}),
        ("Content", {"fields": ("overview_text", "hero_image")}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(CurriculumSemester)
class CurriculumSemesterAdmin(admin.ModelAdmin):
    list_display = ["curriculum", "semester_number", "display_order"]
    list_filter = ["curriculum"]
    ordering = ["curriculum", "semester_number"]
    inlines = [CourseInline]

    fieldsets = (
        ("Semester Information", {"fields": ("curriculum", "semester_number")}),
        ("Content", {"fields": ("description", "syllabus_file", "display_order")}),
    )
    
@admin.register(ProgramFeature)
class ProgramFeatureAdmin(admin.ModelAdmin):
    list_display = ('program', 'feature_text', 'display_order')
    list_filter = ('program',)
    search_fields = ('feature_text',)
    list_editable = ('display_order',)


@admin.register(CareerProspect)
class CareerProspectAdmin(admin.ModelAdmin):
    list_display = ('curriculum', 'title', 'display_order')
    list_filter = ('curriculum',)
    search_fields = ('title',)
    list_editable = ('display_order',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name', 'short_name')

@admin.register(FacultyTab)
class FacultyTabAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'department_filter', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'short_name', 'is_active')
    list_editable = ('is_active',)

    fieldsets = (
        ("College Identity", {"fields": ("college_name", "short_name", "tagline", "established_year")}),
        ("About Section", {"fields": ("about_us", "mission", "vision", "core_values")}),
        ("Footer", {"fields": ("footer_about", "footer_text")}),
        ("Social Media Links", {"fields": ("facebook_url", "twitter_url", "instagram_url", "linkedin_url", "youtube_url")}),
        ("SEO", {"fields": ("meta_description", "meta_keywords")}),
        ("Settings", {"fields": ("is_active",)}),
    )

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'display_order')
    list_editable = ('display_order',)

