from django.db import models


from admin_ordering.models import OrderableModel

class Notice(models.Model):
    """Model for notices and announcements"""

    PRIORITY_CHOICES = [
        ("normal", "Normal"),
        ("urgent", "Urgent"),
        ("highlight", "Highlight"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_bs = models.CharField(
        max_length=50, help_text="Date in Bikram Sambat (e.g., Kartik 25, 2082)"
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="normal")
    image = models.ImageField(
        upload_to="notices/images/", blank=True, null=True, help_text="Notice image"
    )
    file = models.FileField(
        upload_to="notices/files/",
        blank=True,
        null=True,
        help_text="PDF or document attachment",
    )
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', "-created_at"]
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title


class Event(models.Model):
    """Model for upcoming events"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    date_bs = models.CharField(max_length=50, help_text="Date in Bikram Sambat")
    time = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    is_highlight = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Department(models.Model):
    """Model for college departments - fully customizable per college"""

    name = models.CharField(
        max_length=100, unique=True, help_text="Department name (e.g., Computer Science)"
    )
    short_name = models.CharField(
        max_length=20, blank=True, null=True, help_text="Abbreviation (e.g., CS)"
    )
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.short_name if self.short_name else self.name


class Faculty(models.Model):
    """Model for faculty members"""

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(
        max_length=100, help_text="Department name (e.g., Computer Science, Agriculture)"
    )
    qualification = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="faculty/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(
        blank=True, null=True, help_text="Personal or professional website"
    )
    facebook_url = models.URLField(blank=True, null=True, help_text="Facebook profile URL")
    twitter_url = models.URLField(blank=True, null=True, help_text="Twitter/X profile URL")
    linkedin_url = models.URLField(blank=True, null=True, help_text="LinkedIn profile URL")
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Faculty Member"
        verbose_name_plural = "Faculty Members"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class FacultyTab(models.Model):
    """Model for faculty section tabs - allows dynamic tab management"""

    name = models.CharField(
        max_length=100,
        help_text="Tab display name (e.g., IT Department, Agriculture Dept.)",
    )
    slug = models.SlugField(
        unique=True, help_text="URL-friendly identifier (e.g., it, agriculture)"
    )
    department_filter = models.CharField(
        max_length=100,
        help_text="Department name to filter faculty (must match Faculty.department)",
    )
    color_scheme = models.CharField(
        max_length=20,
        default="blue",
        choices=[
            ("blue", "Blue"),
            ("green", "Green"),
            ("purple", "Purple"),
            ("orange", "Orange"),
            ("red", "Red"),
            ("indigo", "Indigo"),
        ],
        help_text="Color scheme for this tab",
    )
    display_order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Faculty Tab"
        verbose_name_plural = "Faculty Tabs"

    def __str__(self):
        return self.name

    def get_color_classes(self):
        """Return Tailwind color classes based on color scheme"""
        colors = {
            "blue": {
                "border": "border-blue-50",
                "hover_border": "group-hover:border-mbman-blue",
                "text": "text-mbman-blue",
                "bg": "bg-mbman-blue",
            },
            "green": {
                "border": "border-green-50",
                "hover_border": "group-hover:border-green-600",
                "text": "text-green-600",
                "bg": "bg-green-600",
            },
            "purple": {
                "border": "border-purple-50",
                "hover_border": "group-hover:border-purple-600",
                "text": "text-purple-600",
                "bg": "bg-purple-600",
            },
            "orange": {
                "border": "border-orange-50",
                "hover_border": "group-hover:border-orange-600",
                "text": "text-orange-600",
                "bg": "bg-orange-600",
            },
            "red": {
                "border": "border-red-50",
                "hover_border": "group-hover:border-red-600",
                "text": "text-red-600",
                "bg": "bg-red-600",
            },
            "indigo": {
                "border": "border-indigo-50",
                "hover_border": "group-hover:border-indigo-600",
                "text": "text-indigo-600",
                "bg": "bg-indigo-600",
            },
        }
        return colors.get(self.color_scheme, colors["blue"])


class HeroSection(models.Model):
    """Model for hero section slides - supports multiple slides in carousel"""

    title = models.CharField(max_length=200, help_text="Main heading")
    subtitle = models.CharField(max_length=300, help_text="Subheading or description")
    background_image = models.ImageField(
        upload_to="hero/",
        blank=True,
        null=True,
        help_text="Background image for this slide",
    )
    background_overlay = models.CharField(
        max_length=20,
        default="dark",
        choices=[
            ("dark", "Dark Overlay"),
            ("light", "Light Overlay"),
            ("blue", "Blue Overlay"),
            ("green", "Green Overlay"),
            ("none", "No Overlay"),
        ],
        help_text="Overlay color to make text readable",
    )
    cta_text = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Call-to-action button text (leave empty to hide button)",
    )
    cta_link = models.CharField(
        max_length=200, blank=True, null=True, help_text="Button link URL"
    )
    display_order = models.IntegerField(
        default=0, help_text="Lower numbers appear first in carousel"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Hero Section Slide"
        verbose_name_plural = "Hero Section Slides"

    def __str__(self):
        return self.title

    def get_overlay_class(self):
        """Return CSS class for overlay"""
        overlay_map = {
            "dark": "bg-black/60",
            "light": "bg-white/40",
            "blue": "bg-blue-900/70",
            "green": "bg-green-900/70",
            "none": "",
        }
        return overlay_map.get(self.background_overlay, "bg-black/60")


class MarqueeItem(models.Model):
    """Model for scrolling marquee announcements"""

    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default="#notices")
    is_new = models.BooleanField(default=False, help_text="Shows [New] badge")
    is_urgent = models.BooleanField(default=False, help_text="Shows warning icon")
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Marquee Item"
        verbose_name_plural = "Marquee Items"

    def __str__(self):
        return self.text


class PrincipalMessage(models.Model):
    """Model for principal's message"""

    quote = models.TextField()
    full_message = models.TextField()
    principal_name = models.CharField(max_length=100)
    principal_title = models.CharField(max_length=100, default="Principal")
    photo = models.ImageField(upload_to="principal/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Principal's Message"
        verbose_name_plural = "Principal's Messages"

    def __str__(self):
        return f"Message by {self.principal_name}"


class Program(models.Model):
    """Model for academic programs"""

    PROGRAM_CHOICES = [
        ("BIT", "Bachelor of Information Technology"),
        ("AG", "Bachelor of Science in Agriculture"),
    ]

    COLOR_CHOICES = [
        ("blue", "Blue Theme"),
        ("green", "Green Theme"),
        ("purple", "Purple Theme"),
        ("red", "Red Theme"),
        ("orange", "Orange Theme"),
        ("indigo", "Indigo Theme"),
    ]

    code = models.CharField(max_length=10, unique=True)
    degree_level = models.CharField(
        max_length=50,
        default="Bachelors",
        help_text="Level of the degree (e.g., Bachelors, Masters, Ph.D.)",
    )
    full_name = models.CharField(max_length=200)
    short_description = models.TextField()
    full_description = models.TextField()
    duration = models.CharField(max_length=50, default="4 Years / 8 Semesters")
    image = models.ImageField(
        upload_to="programs/",
        blank=True,
        null=True,
        help_text="Program card image on homepage",
    )
    brochure = models.FileField(upload_to="programs/brochures/", blank=True, null=True)
    color_scheme = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default="blue",
        help_text="Color theme for program card",
    )
    url_slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text="URL path for curriculum page (e.g., 'bit', 'agriculture')",
    )
    icon_class = models.CharField(
        max_length=50,
        default="fas fa-graduation-cap",
        help_text="Font Awesome icon class",
    )
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0, help_text="Order on homepage")

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"
        ordering = ["display_order", "code"]

    def __str__(self):
        return self.full_name

    def get_color_classes(self):
        """Return Tailwind color classes based on color scheme"""
        color_map = {
            "blue": {
                "bg": "bg-mbman-blue",
                "text": "text-mbman-blue",
                "bg_light": "bg-mbman-blue/20",
                "bg_hover": "group-hover:bg-mbman-blue/10",
                "icon_text": "text-blue-100",
                "feature_icon": "text-blue-500",
                "hover_bg": "hover:bg-mbman-blue",
            },
            "green": {
                "bg": "bg-green-600",
                "text": "text-green-600",
                "bg_light": "bg-green-900/20",
                "bg_hover": "group-hover:bg-green-900/10",
                "icon_text": "text-green-100",
                "feature_icon": "text-green-500",
                "hover_bg": "hover:bg-green-600",
            },
            "purple": {
                "bg": "bg-purple-600",
                "text": "text-purple-600",
                "bg_light": "bg-purple-900/20",
                "bg_hover": "group-hover:bg-purple-900/10",
                "icon_text": "text-purple-100",
                "feature_icon": "text-purple-500",
                "hover_bg": "hover:bg-purple-600",
            },
            "red": {
                "bg": "bg-red-600",
                "text": "text-red-600",
                "bg_light": "bg-red-900/20",
                "bg_hover": "group-hover:bg-red-900/10",
                "icon_text": "text-red-100",
                "feature_icon": "text-red-500",
                "hover_bg": "hover:bg-red-600",
            },
            "orange": {
                "bg": "bg-orange-600",
                "text": "text-orange-600",
                "bg_light": "bg-orange-900/20",
                "bg_hover": "group-hover:bg-orange-900/10",
                "icon_text": "text-orange-100",
                "feature_icon": "text-orange-500",
                "hover_bg": "hover:bg-orange-600",
            },
            "indigo": {
                "bg": "bg-indigo-600",
                "text": "text-indigo-600",
                "bg_light": "bg-indigo-900/20",
                "bg_hover": "group-hover:bg-indigo-900/10",
                "icon_text": "text-indigo-100",
                "feature_icon": "text-indigo-500",
                "hover_bg": "hover:bg-indigo-600",
            },
        }
        return color_map.get(self.color_scheme, color_map["blue"])


class ProgramFeature(models.Model):
    """Model for program features/highlights"""

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="features")
    feature_text = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50, default="fas fa-check-circle", help_text="Font Awesome icon class"
    )
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Program Feature"
        verbose_name_plural = "Program Features"

    def __str__(self):
        return f"{self.program.code} - {self.feature_text}"


class SiteLogo(models.Model):
    """Model for site logo"""

    logo = models.ImageField(upload_to="logo/", help_text="Upload college logo")
    logo_text = models.CharField(max_length=100, default="School of Science & Technology")
    logo_subtext = models.CharField(
        max_length=150, default="Madan Bhandari Memorial Academy Nepal"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site Logo"
        verbose_name_plural = "Site Logos"

    def __str__(self):
        return "Site Logo"


class ContactInfo(models.Model):
    """Model for contact information"""

    phone = models.CharField(
        max_length=100,
        help_text="Enter phone numbers separated by commas (e.g., +977-021-540000, 98520xxxxx)",
    )
    email = models.EmailField()
    address = models.TextField()
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    map_embed_url = models.TextField(blank=True, null=True)
    map_url = models.URLField(
        blank=True, null=True, help_text="Google Maps link for 'Visit Us' button"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"Contact Info - {self.email}"


class ContactMessage(models.Model):
    """Model to store contact form submissions"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default="")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"


class Curriculum(models.Model):
    """Curriculum pages - linked to Program model for complete flexibility"""

    program = models.ForeignKey(
        "Program",
        on_delete=models.CASCADE,
        related_name="curriculums",
        help_text="Program this curriculum belongs to",
    )
    hero_image = models.ImageField(
        upload_to="curriculum/hero/",
        blank=True,
        null=True,
        help_text="Background image for curriculum page header",
    )
    overview_text = models.TextField(help_text="Program overview description")
    duration = models.CharField(max_length=100, default="4 Years / 8 Semesters")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Curriculum Page"
        verbose_name_plural = "Curriculum Pages"

    def __str__(self):
        return f"{self.program.full_name} Curriculum"


class CurriculumSemester(models.Model):
    """Model for semester information in curriculum"""

    curriculum = models.ForeignKey(
        Curriculum, on_delete=models.CASCADE, related_name="semesters"
    )
    semester_number = models.IntegerField(help_text="Semester number (1-8)")
    description = models.TextField(
        blank=True, null=True, help_text="Optional semester description"
    )
    syllabus_file = models.FileField(
        upload_to="syllabus/",
        blank=True,
        null=True,
        help_text="Upload PDF syllabus for this semester",
    )
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["curriculum", "semester_number"]
        unique_together = ["curriculum", "semester_number"]
        verbose_name = "Curriculum Semester"
        verbose_name_plural = "Curriculum Semesters"

    def __str__(self):
        return f"{self.curriculum.program} - Semester {self.semester_number}"


class Course(models.Model):
    """Model for courses in each semester"""

    semester = models.ForeignKey(
        CurriculumSemester, on_delete=models.CASCADE, related_name="courses"
    )
    code = models.CharField(max_length=20, help_text="Course code (e.g., BIT101)")
    title = models.CharField(max_length=200, help_text="Course title")
    credits = models.IntegerField(default=3, help_text="Credit hours")
    description = models.TextField(blank=True, null=True, help_text="Course description")
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["semester", "display_order", "code"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.code} - {self.title}"


class CareerProspect(models.Model):
    """Model for career prospects for each program"""

    curriculum = models.ForeignKey(
        Curriculum, on_delete=models.CASCADE, related_name="career_prospects"
    )
    title = models.CharField(max_length=200, help_text="Career title")
    icon = models.CharField(
        max_length=50,
        default="fas fa-briefcase",
        help_text="Font Awesome icon class",
    )
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["curriculum", "display_order"]
        verbose_name = "Career Prospect"
        verbose_name_plural = "Career Prospects"

    def __str__(self):
        return f"{self.curriculum.program} - {self.title}"


class SiteConfiguration(models.Model):
    """Model for site-wide configuration - allows each college to customize their site"""

    # College Identity
    college_name = models.CharField(
        max_length=200,
        default="School of Science and Technology",
        help_text="Full college name",
    )
    short_name = models.CharField(
        max_length=50, default="SOST", help_text="Short name/acronym"
    )
    tagline = models.CharField(
        max_length=300,
        default="Excellence in Education",
        help_text="College tagline or motto",
    )
    wiki_url = models.URLField(
        blank=True, null=True, help_text="URL for the Admin Wiki/Documentation (e.g., Gist link)."
    )
    established_year = models.CharField(
        max_length=20, blank=True, null=True, help_text="Year established (e.g., 2010 BS)"
    )

    # Spotlight Section
    spotlight_title = models.CharField(
        max_length=200, default="In the Spotlight", help_text="Main title for spotlight section"
    )
    spotlight_subtitle = models.CharField(
        max_length=200, default="Campus Life", help_text="Small eyebrow title above main title"
    )
    spotlight_description = models.TextField(
        blank=True,
        null=True,
        default="Capturing moments of creativity, learning, and celebration at MBMAN.",
        help_text="Description text for spotlight section",
    )

    # About Section
    about_us = models.TextField(
        blank=True, null=True, help_text="About the college (for About page)"
    )
    mission = models.TextField(blank=True, null=True, help_text="Mission statement")
    vision = models.TextField(blank=True, null=True, help_text="Vision statement")
    core_values = models.TextField(
        blank=True, null=True, help_text="Core values (one per line)"
    )

    # Footer Content
    footer_about = models.TextField(
        blank=True,
        null=True,
        help_text="Brief description for footer (max 200 chars recommended)",
    )
    footer_text = models.CharField(
        max_length=200,
        default="Madan Bhandari Memorial Academy Nepal. All rights reserved.",
        help_text="Full copyright text (e.g., 'My College. All rights reserved.'). Year and © symbol are added automatically.",
    )

    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    # SEO
    meta_description = models.TextField(
        blank=True, null=True, help_text="Meta description for search engines"
    )
    meta_keywords = models.TextField(
        blank=True, null=True, help_text="Meta keywords (comma separated)"
    )

    # Settings
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return f"Site Configuration - {self.college_name}"

    def save(self, *args, **kwargs):
        """Ensure only one active configuration exists"""
        if self.is_active:
            SiteConfiguration.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class FooterLink(models.Model):
    """Model for footer links"""

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"

    def __str__(self):
        return self.name
		

class ImageSlideshow(models.Model):
    """Model for image slideshows that can be displayed on various pages"""

    LOCATION_CHOICES = [
        ("homepage_hero", "Homepage Hero Section"),
        ("homepage_gallery", "Homepage Gallery"),
        ("programs", "Programs Page"),
        ("about", "About Page"),
        ("campus", "Campus Life/Gallery"),
        ("custom", "Custom Location"),
    ]

    title = models.CharField(max_length=200, help_text="Image title")
    description = models.TextField(
        blank=True, null=True, help_text="Optional caption or description"
    )
    image = models.ImageField(upload_to="slideshow/", help_text="Slideshow image")
    display_location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default="homepage_gallery",
        help_text="Where to display this image",
    )
    link_url = models.URLField(
        blank=True, null=True, help_text="Optional link when image is clicked"
    )
    cta_text = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Call-to-action button text (for hero slides)",
    )
    display_order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_location", "display_order", "-created_at"]
        verbose_name = "Image Slideshow"
        verbose_name_plural = "Image Slideshows"

    def __str__(self):
        return f"{self.title} ({self.get_display_location_display()})"


class AboutSection(models.Model):
    """Model for About Us page sections"""

    SECTION_TYPE_CHOICES = [
        ("history", "History"),
        ("mission", "Mission & Vision"),
        ("leadership", "Leadership Team"),
        ("facilities", "Facilities & Infrastructure"),
        ("achievements", "Achievements & Awards"),
        ("accreditation", "Accreditation & Affiliations"),
        ("custom", "Custom Section"),
    ]

    section_type = models.CharField(max_length=20, choices=SECTION_TYPE_CHOICES)
    title = models.CharField(max_length=200, help_text="Section title")
    content = models.TextField(help_text="Section content")
    image = models.ImageField(
        upload_to="about/", blank=True, null=True, help_text="Optional section image"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Font Awesome icon class (e.g., fas fa-history)",
    )
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "section_type"]
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"


class GalleryAlbum(models.Model):
    """Model for photo gallery albums"""

    title = models.CharField(max_length=200, help_text="Album title")
    description = models.TextField(blank=True, null=True, help_text="Optional description")
    date_bs = models.CharField(max_length=50, blank=True, null=True, help_text="Date in Bikram Sambat")
    display_order = models.IntegerField(default=0, help_text="Order of display")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Gallery Album"
        verbose_name_plural = "Gallery Albums"

    def __str__(self):
        return self.title

    def get_cover_images(self):
        """Return images marked as cover for this album"""
        return self.images.filter(is_cover=True)

    def get_random_cover(self):
        """Return a single cover image or first image if no cover"""
        cover = self.images.filter(is_cover=True).first()
        if not cover:
            cover = self.images.first()
        return cover


class GalleryImage(models.Model):
    """Model for photo gallery images"""

    album = models.ForeignKey(
        GalleryAlbum,
        on_delete=models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
        help_text="Album this image belongs to",
    )
    caption = models.CharField(
        max_length=200, blank=True, null=True, help_text="Optional caption for the image"
    )
    image = models.ImageField(upload_to="gallery/", help_text="Gallery image")
    is_spotlight = models.BooleanField(
        default=False, help_text="Show this image on homepage spotlight section"
    )
    is_cover = models.BooleanField(
        default=False, help_text="Use this image as album cover"
    )
    display_order = models.IntegerField(default=0, help_text="Order of display")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.caption if self.caption else f"Image {self.id}"
