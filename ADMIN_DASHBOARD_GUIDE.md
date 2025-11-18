# Custom Admin Dashboard - User Guide

## Overview
The custom admin dashboard at `/admin/` provides a comprehensive interface for managing all website content without using Django's built-in admin interface.

## Access

**URL:** `http://localhost:8000/admin/`

**Credentials:**
- Username: `admin`
- Password: `admin123`

**Requirements:**
- User must be logged in
- User must have staff status (is_staff=True)

## Dashboard Features

### Main Dashboard
The dashboard homepage displays:
- **Statistics Cards:** Total notices, events, faculty, and programs
- **Quick Access Cards:** Links to all management sections
- **Recent Messages Preview:** Last 5 contact form submissions

### Management Sections

#### 1. Notice Management (`/admin/notices/`)
- **List Notices:** View all notices with title, date, priority, and status
- **Add Notice:** Create new notices with:
  - Title and description
  - Date (BS calendar)
  - Priority level (Low, Medium, High)
  - File attachment (optional)
  - Active/inactive status
- **Edit Notice:** Update existing notices
- **Delete Notice:** Remove notices (with confirmation)

#### 2. Event Management (`/admin/events/`)
- **List Events:** View all events with details
- **Add Event:** Create events with:
  - Title and description
  - Date and time
  - Location
  - Highlight flag
  - Active/inactive status
- **Edit Event:** Update event details
- **Delete Event:** Remove events (with confirmation)

#### 3. Faculty Management (`/admin/faculty/`)
- **List Faculty:** Grid view of all faculty members with photos
- **Add Faculty:** Add new faculty with:
  - Name and designation
  - Department (IT/Agriculture)
  - Specialization
  - Photo upload
  - Email and phone
  - Biography
  - Display order
  - Active/inactive status
- **Edit Faculty:** Update faculty information
- **Delete Faculty:** Remove faculty members (with confirmation)

#### 4. Page Content Management (`/admin/page-content/`)
Manage homepage sections:

**Hero Section** (`/admin/hero/edit/`)
- Title and subtitle
- Background image
- Call-to-action button text and link
- Active/inactive status

**Marquee Items** (`/admin/marquee/add/`, `/admin/marquee/<id>/edit/`)
- Notification text
- Link URL
- New/Urgent badges
- Display order
- Active/inactive status

**Principal Message** (`/admin/principal-message/edit/`)
- Quote text
- Full message
- Principal name and title
- Photo upload
- Active/inactive status

**Contact Information** (`/admin/contact-info/edit/`)
- Phone and email
- Address
- Social media links (Facebook, Twitter, Instagram, YouTube)
- Google Maps embed URL
- Active/inactive status

#### 5. Contact Messages (`/admin/messages/`)
- **List Messages:** View all contact form submissions
- **View Message:** Read full message details
- **Mark as Read:** Automatically marked when viewing
- **Reply:** Quick link to reply via email
- **Delete:** Remove messages (with confirmation)

## URL Structure

```
/admin/                                  # Main dashboard
/admin/notices/                          # Notice list
/admin/notices/add/                      # Add notice
/admin/notices/<id>/edit/                # Edit notice
/admin/notices/<id>/delete/              # Delete notice

/admin/events/                           # Event list
/admin/events/add/                       # Add event
/admin/events/<id>/edit/                 # Edit event
/admin/events/<id>/delete/               # Delete event

/admin/faculty/                          # Faculty list
/admin/faculty/add/                      # Add faculty
/admin/faculty/<id>/edit/                # Edit faculty
/admin/faculty/<id>/delete/              # Delete faculty

/admin/page-content/                     # Page content overview
/admin/hero/edit/                        # Edit hero section
/admin/marquee/add/                      # Add marquee item
/admin/marquee/<id>/edit/                # Edit marquee item
/admin/marquee/<id>/delete/              # Delete marquee item
/admin/principal-message/edit/           # Edit principal message
/admin/contact-info/edit/                # Edit contact info

/admin/messages/                         # Contact messages list
/admin/messages/<id>/                    # View message
/admin/messages/<id>/delete/             # Delete message
```

## Features

### Security
- All admin views require login (`@login_required`)
- All admin views require staff status (`@user_passes_test`)
- Delete operations require POST method (`@require_POST`)
- Confirmation dialogs for all delete operations

### User Experience
- Success/error messages for all operations
- Breadcrumb navigation
- Responsive design (mobile-friendly)
- Form validation with error messages
- Image previews for uploads
- Consistent styling with Tailwind CSS

### Form Features
- Auto-styled form inputs with 'form-input' class
- File upload support for notices, faculty photos, hero images
- Checkbox fields for flags (is_active, is_highlight, is_new, is_urgent)
- Textarea fields for long content
- URL validation for links and social media
- Email validation

## Comparison with Django Admin

| Feature | Custom Admin | Django Admin |
|---------|--------------|--------------|
| URL | `/admin/` | `/django-admin/` |
| Interface | Custom designed | Django default |
| User Control | Full customization | Limited |
| Branding | MBMAN theme | Django branding |
| Access | Staff users | Superuser/staff |
| Features | Content-focused | Full database |

## Tips

1. **Quick Access:** Use the dashboard cards to navigate to different sections
2. **Recent Messages:** Check the dashboard for new contact form submissions
3. **Status Indicators:** Use the "Active" toggle to show/hide content on the public site
4. **Priority Levels:** Use notice priority to highlight important announcements
5. **Event Highlights:** Mark important events as highlights to feature them
6. **Faculty Order:** Use display_order field to control faculty listing sequence
7. **Marquee Badges:** Use "New" and "Urgent" flags for important notifications
8. **Image Optimization:** Upload appropriately sized images to improve page load times

## Troubleshooting

**Cannot access /admin/**
- Ensure you're logged in
- Check that your user has is_staff=True

**Changes not visible on homepage**
- Check that content is marked as "Active"
- Refresh the homepage
- Check browser cache

**File upload errors**
- Ensure MEDIA_ROOT is configured correctly
- Check file size limits
- Verify file permissions

## Next Steps

After managing content through the custom admin:
1. View changes on the homepage at `/`
2. Test on different devices (mobile, tablet, desktop)
3. Share the admin credentials with authorized staff
4. Regularly backup the database
5. Monitor contact messages for inquiries

## Support

For technical issues:
- Check Django logs for errors
- Review settings.py configuration
- Verify database migrations are up to date
- Contact system administrator

---

**Note:** This is the custom admin interface. For advanced database management, use Django's built-in admin at `/django-admin/`.
