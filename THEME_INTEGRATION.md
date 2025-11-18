# Django Theme Integration - SOST Project

## Overview
The theme files from `templates/theme/` have been successfully converted to Django-compatible templates. The website now uses Django's template inheritance system with a reusable base template.

## Files Created/Modified

### 1. Base Template
- **File**: `templates/base.html`
- **Purpose**: Master template with common elements (navigation, footer, scripts)
- **Features**:
  - Dynamic navigation with user authentication support
  - Responsive design with Tailwind CSS
  - Font Awesome icons integration
  - Block system for child templates to extend

### 2. Page Templates

#### Home Page
- **File**: `templates/home/index.html`
- **Extends**: `base.html`
- **Sections**:
  - Hero section with marquee announcements
  - Notices & Events (with tab switching)
  - Academic Programs (BIT & Agriculture)
  - Principal's Message
  - Faculty Section (with department tabs)
  - Contact Form

#### Login Page
- **File**: `templates/auth/login.html`
- **Extends**: `base.html`
- **Features**:
  - Django form with CSRF protection
  - Error message display
  - "Forgot Password" modal
  - Remember me checkbox

#### Admin Dashboard
- **File**: `templates/home/admin_dashboard.html`
- **Extends**: `base.html`
- **Features**:
  - Sidebar navigation
  - Dashboard statistics
  - Quick actions
  - Multiple admin pages (notices, faculty, curriculum, content, settings)
  - Staff-only access

#### Program Pages
- **Files**: `templates/home/bit.html`, `templates/home/agriculture.html`
- **Extends**: `base.html`
- **Purpose**: Dedicated pages for BIT and Agriculture programs

### 3. Views

#### Home App (`home/views.py`)
```python
- index(): Homepage view
- bit(): BIT program page
- agriculture(): Agriculture program page
- admin_dashboard(): Admin dashboard (staff-only)
```

#### Auth App (`auth/views.py`)
```python
- login(): Handle user authentication
- logout(): Handle user logout
```

### 4. URL Configuration

#### Home URLs (`home/urls.py`)
```
/                       - Homepage
/programs/bit/          - BIT program page
/programs/agriculture/  - Agriculture program page
/admin/dashboard/       - Admin dashboard
```

#### Auth URLs (`auth/urls.py`)
```
/auth/login/   - Login page
/auth/logout/  - Logout action
```

#### Main URLs (`config/urls.py`)
- Includes home and auth app URLs
- Serves static files in DEBUG mode

## Django Features Used

### Template Tags
- `{% extends %}` - Template inheritance
- `{% load static %}` - Load static files
- `{% static %}` - Reference static files
- `{% url %}` - Generate URLs from view names
- `{% if user.is_authenticated %}` - Check authentication
- `{% csrf_token %}` - CSRF protection
- `{% now %}` - Current date/time

### Authentication
- `@login_required` decorator for protected views
- `@user_passes_test` for staff-only access
- Django's built-in authentication system
- User context available in all templates

### Messages Framework
- Success/error messages on login/logout
- Flash messages displayed in templates

## Key Improvements

1. **DRY Principle**: Common elements (nav, footer) defined once in base.html
2. **Security**: CSRF protection, authentication decorators
3. **Dynamic Content**: User-specific navigation (logged in/out states)
4. **URL Management**: Named URLs for easy maintenance
5. **Static Files**: Properly configured with {% static %} tags
6. **Responsive Design**: Mobile-friendly navigation and layouts

## Configuration Updates

### Settings (`config/settings.py`)
```python
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

## Running the Project

### 1. Apply Migrations (if needed)
```bash
python manage.py migrate
```

### 2. Create a Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 3. Collect Static Files (for production)
```bash
python manage.py collectstatic
```

### 4. Run Development Server
```bash
python manage.py runserver
```

### 5. Access the Website
- Homepage: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/auth/login/
- Admin Dashboard: http://127.0.0.1:8000/admin/dashboard/ (requires staff login)
- Django Admin: http://127.0.0.1:8000/admin/

## Theme Features Preserved

### From Original Theme
✅ Tailwind CSS configuration
✅ MBMAN brand colors (#06437a blue, #d97706 gold)
✅ Google Fonts (Inter)
✅ Font Awesome icons
✅ Smooth scrolling
✅ Marquee animations
✅ Tab switching (notices/events, faculty departments)
✅ Responsive mobile menu
✅ User dropdown menu
✅ Forgot password modal

### Enhanced with Django
✅ Template inheritance
✅ Dynamic user authentication states
✅ CSRF protection
✅ URL reversing
✅ Static file management
✅ Message framework
✅ Permission-based access control

## Next Steps

1. **Create Models**: Define database models for Notices, Faculty, Programs, etc.
2. **Admin Interface**: Register models in Django admin for content management
3. **Dynamic Content**: Replace static content with database-driven data
4. **Forms**: Create Django forms for contact, applications, etc.
5. **File Uploads**: Enable file uploads for notices, faculty photos, etc.
6. **Search**: Add search functionality for notices and programs
7. **Pagination**: Add pagination for notices and events
8. **API**: Consider creating REST API for mobile apps

## Notes

- Original theme files remain in `templates/theme/` for reference
- Static files (CSS, JS) are in the `static/` directory
- All templates use Django template language
- Authentication required for admin dashboard
- Staff permission required to access admin features

## Support

For questions or issues, contact the development team.
