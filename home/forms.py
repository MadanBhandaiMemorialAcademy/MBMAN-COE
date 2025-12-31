from django import forms

from .models import (
    AboutSection,
    CareerProspect,
    ContactInfo,
    Course,
    Curriculum,
    CurriculumSemester,
    Department,
    Event,
    Faculty,
    FacultyTab,
    FooterLink,
    HeroSection,
    ImageSlideshow,
    MarqueeItem,
    Notice,
    PrincipalMessage,
    Program,
    ProgramFeature,
    SiteConfiguration,
    SiteLogo,
    GalleryImage,
    GalleryAlbum,
)


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            "title",
            "description",
            "date_bs",
            "priority",
            "image",
            "file",
            "is_active",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Enter notice title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                    "placeholder": "Enter notice description",
                }
            ),
            "date_bs": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "YYYY-MM-DD",
                    "id": "nepali-datepicker",
                }
            ),
            "priority": forms.Select(attrs={"class": "form-input"}),
            "image": forms.FileInput(attrs={"class": "form-input", "accept": "image/*"}),
            "file": forms.FileInput(
                attrs={"class": "form-input", "accept": ".pdf,.doc,.docx"}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "date_bs",
            "time",
            "location",
            "is_highlight",
            "is_active",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Enter event title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                    "placeholder": "Enter event description",
                }
            ),
            "date_bs": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "YYYY-MM-DD",
                    "id": "nepali-datepicker-event",
                }
            ),
            "time": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "e.g., 10:00 AM - 5:00 PM"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Event location"}
            ),
        }


class FacultyForm(forms.ModelForm):
    department = forms.ChoiceField(label="Department")

    class Meta:
        model = Faculty
        fields = [
            "name",
            "designation",
            "department",
            "qualification",
            "photo",
            "email",
            "phone",
            "website",
            "facebook_url",
            "twitter_url",
            "linkedin_url",
            "bio",
            "is_active",
            "display_order",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Full name"}
            ),
            "designation": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "e.g., HoD, IT Department"}
            ),
            "qualification": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., M.Sc. Computer Science, Ph.D.",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "email@mbman.edu.np"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "+977-XXX-XXXXXX"}
            ),
            "website": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "https://example.com"}
            ),
            "facebook_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "Facebook URL"}
            ),
            "twitter_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "Twitter URL"}
            ),
            "linkedin_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "LinkedIn URL"}
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Brief biography (optional)",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Display order (lower numbers first)",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate department choices from FacultyTab
        # Using department_filter as value, and name as label
        tabs = FacultyTab.objects.filter(is_active=True)
        choices = [(tab.department_filter, tab.name) for tab in tabs]
        # If no tabs, maybe fallback or empty?
        if not choices:
            choices = [("", "No departments/tabs available")]
        
        self.fields["department"].choices = choices
        self.fields["department"].widget.attrs.update({"class": "form-input"})


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "short_name", "description", "display_order", "is_active"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Computer Science",
                }
            ),
            "short_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "e.g., CS"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Department description (optional)",
                }
            ),
            "display_order": forms.NumberInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class FacultyTabForm(forms.ModelForm):
    class Meta:
        model = FacultyTab
        fields = [
            "name",
            "slug",
            "department_filter",
            "color_scheme",
            "display_order",
            "is_active",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., IT Department",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., it, agriculture (lowercase, no spaces)",
                }
            ),
            "department_filter": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Must match Faculty department field exactly",
                }
            ),
            "color_scheme": forms.Select(attrs={"class": "form-input"}),
            "display_order": forms.NumberInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class HeroSectionForm(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = [
            "title",
            "subtitle",
            "background_image",
            "background_overlay",
            "cta_text",
            "cta_link",
            "display_order",
            "is_active",
        ]
        help_texts = {
            'title': 'Main large heading. Use &lt;span class="text-transparent bg-clip-text bg-gradient-to-r from-mbman-gold to-yellow-300"&gt;Word&lt;/span&gt; to make a word gold.',
            'subtitle': 'Smaller text displayed below the title.',
            'background_image': 'High-quality image (1920x1080 recommended).',
            'background_overlay': 'Darkens the image to make text readable.',
            'cta_text': 'Label for the main action button (e.g., "Apply Now"). Leave empty to hide.',
            'cta_link': 'Where the button should link to (e.g., "#programs" or "https://example.com").',
            'display_order': 'Lower numbers (1, 2, 3) appear first in the slideshow.',
        }
        widgets = {
            "title": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Hero section title"}
            ),
            "subtitle": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Hero section subtitle"}
            ),
            "background_image": forms.FileInput(attrs={"class": "form-input"}),
            "background_overlay": forms.Select(attrs={"class": "form-input"}),
            "cta_text": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Call-to-action text (optional)",
                }
            ),
            "cta_link": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Link URL"}
            ),
            "display_order": forms.NumberInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class MarqueeItemForm(forms.ModelForm):
    class Meta:
        model = MarqueeItem
        fields = ["text", "link", "is_new", "is_urgent", "is_active", "display_order"]
        widgets = {
            "text": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Announcement text"}
            ),
            "link": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Link URL"}
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class PrincipalMessageForm(forms.ModelForm):
    class Meta:
        model = PrincipalMessage
        fields = [
            "quote",
            "full_message",
            "principal_name",
            "principal_title",
            "photo",
            "is_active",
        ]
        widgets = {
            "quote": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Principal's quote"}
            ),
            "full_message": forms.Textarea(
                attrs={"class": "form-input", "rows": 5, "placeholder": "Full message"}
            ),
            "principal_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Principal's name"}
            ),
            "principal_title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Principal"}
            ),
        }


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = [
            "phone",
            "email",
            "address",
            "facebook_url",
            "twitter_url",
            "linkedin_url",
            "youtube_url",
            "map_embed_url",
            "map_url",
            "is_active",
        ]
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "+977-XXX-XXXXXX"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "info@mbman.edu.np"}
            ),
            "address": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Full address"}
            ),
            "facebook_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "Facebook URL"}
            ),
            "twitter_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "Twitter URL"}
            ),
            "linkedin_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "LinkedIn URL"}
            ),
            "youtube_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "YouTube URL"}
            ),
            "map_embed_url": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 2,
                    "placeholder": "e.g. https://www.google.com/maps/embed?pb=...",
                }
            ),
            "map_url": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. https://maps.app.goo.gl/..."
                }
            ),
        }
        help_texts = {
            "map_embed_url": "Go to Google Maps > Share > Embed a map > Copy HTML. Paste ONLY the URL inside src='...'. Example: https://www.google.com/maps/embed?pb=...",
            "map_url": "Go to Google Maps > Share > Send a link > Copy Link. This is the link used when clicking 'Visit Us'.",
            "phone": "Primary contact number displayed in header and contact page.",
            "email": "Primary email address for inquiries.",
        }


class SiteLogoForm(forms.ModelForm):
    class Meta:
        model = SiteLogo
        fields = ["logo", "logo_text", "logo_subtext", "is_active"]
        widgets = {
            "logo": forms.FileInput(attrs={"class": "form-input", "accept": "image/*"}),
            "logo_text": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "School of Science & Technology",
                }
            ),
            "logo_subtext": forms.TextInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ["program", "overview_text", "duration", "hero_image", "is_active"]
        widgets = {
            "program": forms.Select(attrs={"class": "form-input"}),
            "overview_text": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 6,
                    "placeholder": "Program overview description",
                }
            ),
            "duration": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "4 Years / 8 Semesters",
                }
            ),
            "hero_image": forms.FileInput(
                attrs={"class": "form-input", "accept": "image/*"}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class CurriculumSemesterForm(forms.ModelForm):
    class Meta:
        model = CurriculumSemester
        fields = ["semester_number", "description", "display_order"]
        widgets = {
            "semester_number": forms.NumberInput(
                attrs={"class": "form-input", "min": "1", "max": "8"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Optional semester description",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["code", "title", "credits", "description", "display_order"]
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "e.g., BIT101"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Course title"}
            ),
            "credits": forms.NumberInput(
                attrs={"class": "form-input", "min": "1", "max": "10", "value": "3"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Optional course description",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class CareerProspectForm(forms.ModelForm):
    class Meta:
        model = CareerProspect
        fields = ["curriculum", "title", "icon", "display_order"]
        widgets = {
            "curriculum": forms.Select(attrs={"class": "form-input"}),
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Career title"}
            ),
            "icon": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "fas fa-briefcase",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            "code",
            "degree_level",
            "full_name",
            "short_description",
            "full_description",
            "duration",
            "image",
            "brochure",
            "color_scheme",
            "url_slug",
            "icon_class",
            "display_order",
            "is_active",
        ]
        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., BIT, AG, MBA",
                }
            ),
            "degree_level": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Bachelors, Masters",
                }
            ),
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Bachelor of Information Technology",
                }
            ),
            "short_description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Short description for program card",
                }
            ),
            "full_description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 6,
                    "placeholder": "Detailed program description",
                }
            ),
            "duration": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., 4 Years / 8 Semesters",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-input",
                    "accept": "image/*",
                }
            ),
            "brochure": forms.FileInput(attrs={"class": "form-input", "accept": ".pdf"}),
            "color_scheme": forms.Select(attrs={"class": "form-input"}),
            "url_slug": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., bit, agriculture, mba",
                }
            ),
            "icon_class": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "fas fa-code",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "0"}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class ProgramFeatureForm(forms.ModelForm):
    class Meta:
        model = ProgramFeature
        fields = ["program", "feature_text", "icon", "display_order"]
        widgets = {
            "program": forms.Select(attrs={"class": "form-input"}),
            "feature_text": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Modern IT Labs",
                }
            ),
            "icon": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "fas fa-check-circle",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class SiteConfigurationForm(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = [
            "college_name",
            "short_name",
            "tagline",
            "wiki_url",
            "established_year",
            "spotlight_title",
            "spotlight_subtitle",
            "spotlight_description",
            "about_us",
            "mission",
            "vision",
            "core_values",
            "footer_about",
            "footer_text",
            "facebook_url",
            "twitter_url",
            "instagram_url",
            "linkedin_url",
            "youtube_url",
            "meta_description",
            "meta_keywords",
            "is_active",
        ]
        widgets = {
            "college_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "School of Science and Technology",
                }
            ),
            "short_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "SOST"}
            ),
            "tagline": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Excellence in Education"}
            ),
            "wiki_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "https://gist.github.com/..."}
            ),
            "established_year": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "2067 BS"}
            ),
            "spotlight_title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "In the Spotlight"}
            ),
            "spotlight_subtitle": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Campus Life"}
            ),
            "spotlight_description": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Description"}
            ),
            "about_us": forms.Textarea(
                attrs={"class": "form-input", "rows": 6, "placeholder": "About"}
            ),
            "mission": forms.Textarea(
                attrs={"class": "form-input", "rows": 4, "placeholder": "Mission"}
            ),
            "vision": forms.Textarea(
                attrs={"class": "form-input", "rows": 4, "placeholder": "Vision"}
            ),
            "core_values": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                    "placeholder": "One value per line",
                }
            ),
            "footer_about": forms.Textarea(
                attrs={"class": "form-input", "rows": 3, "placeholder": "Brief"}
            ),
            "footer_text": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "© 2025"}
            ),
            "facebook_url": forms.URLInput(attrs={"class": "form-input"}),
            "twitter_url": forms.URLInput(attrs={"class": "form-input"}),
            "instagram_url": forms.URLInput(attrs={"class": "form-input"}),
            "linkedin_url": forms.URLInput(attrs={"class": "form-input"}),
            "youtube_url": forms.URLInput(attrs={"class": "form-input"}),
            "meta_description": forms.Textarea(attrs={"class": "form-input", "rows": 3}),
            "meta_keywords": forms.Textarea(attrs={"class": "form-input", "rows": 2}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
        help_texts = {
            "college_name": "The main name displayed in the header and footer (e.g., School of Science & Technology).",
            "short_name": "Acronym used in smaller spaces (e.g., SOST).",
            "established_year": "Displayed in the footer or about section.",
            "spotlight_title": "Heading for the photo spotlight section on the homepage.",
            "spotlight_description": "Brief text describing the campus life photos.",
            "footer_about": "A short paragraph (2-3 sentences) about the college shown in the footer.",
            "footer_text": "Full copyright text (e.g., 'My College. All rights reserved.'). Year and © symbol are added automatically.",
            "meta_description": "Important for SEO. A summary of the website shown in Google search results.",
            "meta_keywords": "Comma-separated keywords (e.g., engineering, nepal, bit, agriculture).",
        }


class FooterLinkForm(forms.ModelForm):
    class Meta:
        model = FooterLink
        fields = ["name", "url", "display_order"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Link name"}
            ),
            "url": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "URL"}
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class ImageSlideshowForm(forms.ModelForm):
    class Meta:
        model = ImageSlideshow
        fields = [
            "title",
            "description",
            "image",
            "display_location",
            "link_url",
            "cta_text",
            "display_order",
            "is_active",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Image title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Optional caption",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-input"}),
            "display_location": forms.Select(attrs={"class": "form-input"}),
            "link_url": forms.URLInput(
                attrs={"class": "form-input", "placeholder": "https://example.com"}
            ),
            "cta_text": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Learn More"}
            ),
            "display_order": forms.NumberInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class GalleryAlbumForm(forms.ModelForm):
    class Meta:
        model = GalleryAlbum
        fields = ["title", "description", "display_order"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Album title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 3,
                    "placeholder": "Album description",
                }
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["album", "caption", "image", "is_spotlight", "is_cover", "display_order"]
        widgets = {
            "album": forms.Select(attrs={"class": "form-input"}),
            "caption": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Image caption (optional)"}
            ),
            "image": forms.FileInput(attrs={"class": "form-input"}),
            "is_spotlight": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
            "is_cover": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
            "display_order": forms.NumberInput(
                attrs={"class": "form-input", "placeholder": "Display order"}
            ),
        }


class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = [
            "section_type",
            "title",
            "content",
            "image",
            "icon",
            "display_order",
            "is_active",
        ]
        widgets = {
            "section_type": forms.Select(attrs={"class": "form-input"}),
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Section title"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-input", "rows": 6, "placeholder": "Content"}
            ),
            "image": forms.FileInput(attrs={"class": "form-input"}),
            "icon": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "fas fa-history"}
            ),
            "display_order": forms.NumberInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
