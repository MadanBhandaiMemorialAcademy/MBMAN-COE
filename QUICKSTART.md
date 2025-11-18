# Quick Start Guide

## Prerequisites
- Python 3.10+ installed
- Django 5.2.8 installed
- Virtual environment (recommended)

## Installation Steps

### 1. Set Up Python Environment
```bash
# If using pyenv, install and set the correct Python version
pyenv install 3.12
pyenv local 3.12

# Or use your system Python and create a virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies
```bash
pip install django
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
# Follow the prompts to create username, email, and password
```

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Access the Website
Open your browser and visit:
- **Homepage**: http://127.0.0.1:8000/
- **Login**: http://127.0.0.1:8000/auth/login/
- **Admin Dashboard**: http://127.0.0.1:8000/admin/dashboard/
  - Requires staff privileges (make your user staff via Django admin)
- **Django Admin**: http://127.0.0.1:8000/admin/

## Testing the Website

### Test Public Pages
1. Visit homepage - should see hero section, programs, notices, etc.
2. Click on navigation links - all sections should scroll smoothly
3. Try the mobile menu - should work on smaller screens

### Test Authentication
1. Visit login page at `/auth/login/`
2. Try logging in with your superuser credentials
3. After login, you should see "Welcome, [username]" in navigation
4. User dropdown should appear in desktop navigation
5. Click logout to test logout functionality

### Test Admin Dashboard
1. Make sure your user has staff status:
   - Go to http://127.0.0.1:8000/admin/
   - Login with superuser
   - Go to Users
   - Edit your user
   - Check "Staff status"
   - Save
2. Visit http://127.0.0.1:8000/admin/dashboard/
3. You should see the admin dashboard with statistics
4. Test sidebar navigation between different sections

## Common Issues

### Static Files Not Loading
```bash
# Make sure static files are configured in settings.py
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### Template Not Found
- Check that template files are in the correct directories
- Verify `TEMPLATES['DIRS']` includes `BASE_DIR / "templates"`

### Permission Denied on Admin Dashboard
- Make sure your user has `is_staff=True`
- Set this via Django admin panel

## Project Structure
```
SOST-Django/
├── config/              # Project settings and main URLs
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── home/                # Home app (main website pages)
│   ├── views.py
│   ├── urls.py
│   └── ...
├── auth/                # Authentication app
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/           # HTML templates
│   ├── base.html       # Master template
│   ├── home/           # Home app templates
│   │   ├── index.html
│   │   ├── bit.html
│   │   ├── agriculture.html
│   │   └── admin_dashboard.html
│   └── auth/           # Auth app templates
│       └── login.html
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
├── manage.py
└── db.sqlite3          # Database (created after migrations)
```

## What's Working

✅ Homepage with all sections (hero, notices, programs, faculty, contact)
✅ Responsive navigation with mobile menu
✅ User authentication (login/logout)
✅ Dynamic navigation based on auth status
✅ Admin dashboard (for staff users)
✅ Program pages (BIT and Agriculture)
✅ Template inheritance system
✅ Static file serving
✅ CSRF protection
✅ Message framework

## Next Development Steps

1. **Create Models** for dynamic content:
   - Notice/Event model
   - Faculty model
   - Program model
   - Course model

2. **Set Up Django Admin** for content management

3. **Make Content Dynamic**:
   - Load notices from database
   - Load faculty from database
   - Load programs from database

4. **Add Forms**:
   - Contact form
   - Application form
   - Search form

5. **Implement Features**:
   - File uploads for notices
   - Image uploads for faculty
   - Search functionality
   - Filtering and sorting

## Support

If you encounter any issues:
1. Check the Django development server console for error messages
2. Review `THEME_INTEGRATION.md` for detailed documentation
3. Ensure all dependencies are installed
4. Verify database migrations are applied

Happy coding! 🚀
