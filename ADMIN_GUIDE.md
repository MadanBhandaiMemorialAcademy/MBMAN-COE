# Admin System Implementation Guide

## What Has Been Implemented

### 1. Custom User Model with bcrypt
- ✅ Extended `AbstractUser` for custom user fields
- ✅ Configured bcrypt as the primary password hasher
- ✅ Added fields: phone, designation, department
- ✅ User model registered in Django admin

### 2. Database Models for Website Content
All website elements are now editable from the admin dashboard:

#### Content Models:
- **Notice**: Announcements with priority levels (normal/urgent/highlight)
- **Event**: Upcoming events with dates, times, locations
- **Faculty**: Faculty members with photos, departments, and bio
- **Program**: Academic programs (BIT, Agriculture) with descriptions
- **ProgramFeature**: Features/highlights for each program
- **HeroSection**: Hero section content (title, subtitle, CTA)
- **MarqueeItem**: Scrolling announcement items
- **PrincipalMessage**: Principal's message/quote
- **ContactInfo**: Contact details and social media links
- **ContactMessage**: Form submissions from website visitors

### 3. Django Admin Configuration
- ✅ Rich admin interfaces for all models
- ✅ List displays with filtering and searching
- ✅ Inline editing for related models
- ✅ Custom fieldsets for better organization
- ✅ File/image upload support
- ✅ Ordering and display controls

### 4. Dynamic Views
- ✅ All views now fetch content from database
- ✅ Homepage displays dynamic notices, events, faculty, programs
- ✅ Contact form saves to database
- ✅ Admin dashboard shows statistics

### 5. Media Files Configuration
- ✅ Media uploads enabled for images and files
- ✅ Separate directories for different content types
- ✅ URLs configured for serving media in development

## Access Information

### Admin Login Credentials
```
URL: http://127.0.0.1:8000/django-admin/
Username: admin
Password: admin123
```

### URL Structure
- **Homepage**: http://127.0.0.1:8000/
- **Django Admin**: http://127.0.0.1:8000/django-admin/
- **Custom Admin Dashboard**: http://127.0.0.1:8000/admin/
- **Login**: http://127.0.0.1:8000/auth/login/
- **BIT Program**: http://127.0.0.1:8000/programs/bit/
- **Agriculture Program**: http://127.0.0.1:8000/programs/agriculture/

## How to Manage Website Content

### 1. Adding/Editing Notices
1. Go to Django Admin → Home → Notices
2. Click "Add Notice" or edit existing
3. Fields:
   - Title: Notice headline
   - Description: Full notice text
   - Date (B.S.): Nepali date (e.g., "Kartik 25, 2082")
   - Priority: Normal, Urgent, or Highlight
   - File: Optional PDF attachment
   - Is Active: Check to display on website

### 2. Managing Events
1. Go to Django Admin → Home → Events
2. Add/edit events with:
   - Title, Description
   - Date (B.S.), Time, Location
   - Is Highlight: Featured events
   - Is Active: Show/hide

### 3. Managing Faculty
1. Go to Django Admin → Home → Faculty Members
2. Add faculty with:
   - Name, Photo
   - Designation, Department (IT/Agriculture)
   - Specialization, Bio
   - Display Order: Lower numbers appear first
   - Email, Phone (optional)

### 4. Managing Programs
1. Go to Django Admin → Home → Programs
2. Edit BIT or Agriculture programs
3. Add features inline (shown as checkmarks on website)

### 5. Updating Hero Section
1. Go to Django Admin → Home → Hero Sections
2. Edit content:
   - Title, Subtitle
   - Background Image
   - Call-to-Action text and link

### 6. Managing Marquee Items
1. Go to Django Admin → Home → Marquee Items
2. Add scrolling announcements
3. Mark as "New" or "Urgent" for badges
4. Set Display Order

### 7. Updating Principal's Message
1. Go to Django Admin → Home → Principal's Messages
2. Edit quote and full message
3. Update principal's name and photo

### 8. Contact Information
1. Go to Django Admin → Home → Contact Information
2. Update phone, email, address
3. Add social media URLs
4. Update map embed URL

### 9. Viewing Contact Messages
1. Go to Django Admin → Home → Contact Messages
2. View form submissions from website
3. Mark as read/unread

## Security Features

### Password Hashing
```python
# Using bcrypt (strongest available)
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]
```

### Custom User Model
- Extended from AbstractUser
- Additional fields for staff information
- Centralized user management

### File Uploads
- Organized by content type (notices/, faculty/, programs/, etc.)
- Supports images (JPG, PNG) and documents (PDF)

## Database Schema

### Key Tables
- `users` - Custom user model
- `home_notice` - Notices/announcements
- `home_event` - Events
- `home_faculty` - Faculty members
- `home_program` - Academic programs
- `home_programfeature` - Program features
- `home_herosection` - Hero content
- `home_marqueeitem` - Scrolling items
- `home_principalmessage` - Principal's message
- `home_contactinfo` - Contact details
- `home_contactmessage` - Form submissions

## Initial Data

Sample data has been populated:
- 3 Marquee items
- 2 Notices
- 1 Event
- 2 Programs (BIT & Agriculture) with features
- 2 Faculty members
- 1 Hero section
- 1 Principal's message
- 1 Contact info

## Next Steps

### For Further Development:
1. **Update Templates**: Modify templates to display dynamic content from database
2. **Add More Faculty**: Populate faculty database
3. **Upload Images**: Add photos for faculty, programs, etc.
4. **Create More Notices**: Add current notices and events
5. **Customize Content**: Update all text to match actual institution details

### Recommended Enhancements:
1. Rich text editor for descriptions (django-ckeditor)
2. Image cropping/resizing (easy-thumbnails)
3. Email notifications for contact form submissions
4. Bulk upload for faculty members
5. Academic calendar integration
6. Student portal integration

## File Structure
```
SOST-Django/
├── media/              # User uploads (created automatically)
│   ├── notices/       # Notice attachments
│   ├── faculty/       # Faculty photos
│   ├── programs/      # Program images
│   ├── hero/          # Hero backgrounds
│   └── principal/     # Principal photos
├── home/
│   ├── models.py      # Database models
│   ├── admin.py       # Admin configurations
│   ├── views.py       # Dynamic views
│   └── management/
│       └── commands/
│           └── populate_data.py  # Sample data
└── auth/
    ├── models.py      # Custom User model
    └── admin.py       # User admin

```

## Common Tasks

### Create New Admin User
```bash
python manage.py createsuperuser
```

### Reset Admin Password
```bash
python manage.py changepassword admin
```

### Repopulate Sample Data
```bash
python manage.py populate_data
```

### Clear Database (Careful!)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py populate_data
python manage.py createsuperuser
```

## Support

For questions or issues:
1. Check Django admin error messages
2. Review model field requirements
3. Ensure images are proper format (JPG/PNG)
4. Verify file sizes (keep under 5MB)

Happy content managing! 🎉
