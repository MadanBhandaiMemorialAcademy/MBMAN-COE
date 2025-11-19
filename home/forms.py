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
                    "placeholder": "DD/MM/YYYY (e.g., 15/08/2081)",
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
                    "placeholder": "DD/MM/YYYY (e.g., 15/08/2081)",
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
            "department": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Computer Science, Agriculture",
                }
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
            'title': 'Use &lt;span class="text-transparent bg-clip-text bg-gradient-to-r from-mbman-gold to-yellow-300"&gt;Technology&lt;/span&gt; to colorize words.',
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
                    "placeholder": "Google Maps embed URL",
                }
            ),
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
        fields = ["curriculum", "semester_number", "description", "display_order"]
        widgets = {
            "curriculum": forms.Select(attrs={"class": "form-input"}),
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
        fields = ["semester", "code", "title", "credits", "description", "display_order"]
        widgets = {
            "semester": forms.Select(attrs={"class": "form-input"}),
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
            "established_year",
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
            "established_year": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "2067 BS"}
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
