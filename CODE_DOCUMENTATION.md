# Project Documentation

## 1. Overview
This project is a Django-based college website management system. It includes a public-facing website and a custom Admin Dashboard for content management.

## 2. Application Structure
The project consists of two main apps:
- **`config/`**: The main project configuration directory (settings, urls, wsgi/asgi).
- **`home/`**: The core application containing all models, views, and logic for the website.
- **`auth/`** (or `custom_auth`): Custom authentication logic if extended beyond Django's default.

### Directory Layout
```
mbman-coe/
├── config/             # Project settings
├── home/               # Main Application
│   ├── models.py       # Database schema
│   ├── views.py        # Logic for pages
│   ├── urls.py         # URL routing
│   ├── forms.py        # Forms for Admin Dashboard
│   ├── context_processors.py # Global context (e.g., site config available in all templates)
│   └── migrations/     # Database changes
├── templates/          # HTML Files
│   ├── base.html       # Main layout (header/footer)
│   ├── home/           # Public pages (index, contact, etc.)
│   └── home/admin/     # Custom Admin Dashboard pages
├── static/             # CSS, JS, Images (System assets)
└── media/              # User uploaded files (Photos, PDFs)
```

## 3. Key Models (`home/models.py`)

### Content Management
- **`SiteConfiguration`**: Singleton model storing global site data (Name, Logo, Footer Text, SEO).
- **`ContactInfo`**: Singleton model for Phone, Email, Map URLs.
- **`PrincipalMessage`**: Stores the principal's quote and photo.
- **`HeroSection`**: Slides for the homepage carousel.
- **`Notice`** & **`Event`**: Announcements and Calendar events.

### Academic & Faculty
- **`Program`**: Academic degrees (e.g., BIT, Civil). Linked to `Curriculum`.
- **`FacultyTab`**: Defines the department tabs shown on the Faculty page (e.g., "IT Dept", "Admin").
- **`Faculty`**: Individual staff members. Linked to `FacultyTab` via `department` field.

### Gallery
- **`GalleryAlbum`**: Collections of photos.
- **`GalleryImage`**: Individual photos. Can be part of an Album, a Cover image, or a Spotlight image (homepage).

## 4. Views & Logic (`home/views.py`)

### Public Views
- `index()`: Renders the homepage. Fetches Heroes, Spotlights, Notices, etc.
- `programs_page()`: Lists all academic programs.
- `faculty_page()`: Groups faculty by their Tabs for display.
- `contact_page()`: Simple view for contact info (Form POST logic was removed to prevent spam).

### Admin Views (`/admin/` - Custom Dashboard)
*Note: This is NOT the standard Django Admin. It is a custom-built dashboard for easier user experience.*
- `admin_dashboard()`: The main stats overview.
- `*_list`, `*_add`, `*_edit`, `*_delete`: CRUD views for every model (Faculty, Notices, Gallery, etc.).
- **Reordering**: `notice_reorder`, `faculty_reorder` handle AJAX requests to update `display_order` fields using SortableJS in the frontend.

## 5. Forms (`home/forms.py`)
All forms used in the custom admin dashboard are defined here. They generally use `ModelForm` and include Tailwind CSS classes (`form-input`) for styling.

## 6. Templates & Design
- **Tailwind CSS**: Used for styling. Custom colors are defined in `base.html` script config (e.g., `mbman-blue`).
- **`base.html`**: The skeleton template. Contains the Navbar, Footer, and block definitions (`{% block content %}`).
- **Admin Templates**: Located in `templates/home/admin/`. They extend `base.html` but usually wrap content in a restricted container.

## 7. Cloudinary & Database
- **Images**: Configured to use Cloudinary in production (via `.env`) or local `media/` folder in development.
- **Database**: Uses SQLite locally. In production (cPanel), it connects to MySQL via `dj_database_url` settings.

## 8. Deployment Notes
- **cPanel**: Uses `passenger_wsgi.py` as the entry point.
- **Static Files**: Must run `python manage.py collectstatic` to serve assets in production.
- **Env Vars**: Managed via `.env` file (create one from `.env.example`).

---
*Generated for future developers to understand the MBMAN-COE codebase.*