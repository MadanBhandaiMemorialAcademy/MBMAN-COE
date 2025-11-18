# Multi-College Website Platform - Django

A completely customizable college website system that can be deployed for **any college** and managed 100% through the admin dashboard. No code changes needed!

## 🎯 What Makes This Special?

- **Zero Hardcoding**: Everything is database-driven
- **One Codebase, Multiple Colleges**: Same code for SOST, COE, CTEVT, or any college
- **100% Admin Managed**: All content, branding, programs via dashboard
- **Production Ready**: Independent databases per deployment

## 🚀 Quick Start (Fresh Deployment)

### 1. Setup Database
```bash
python manage.py migrate
```

### 2. Create Admin User
```bash
python manage.py createsuperuser
```

### 3. Initialize Blank Site
```bash
python manage.py init_site_config
```

That's it! Your college website is ready to customize.

## 📝 Customization Steps

### 1. Login to Admin
Go to `http://your-site.com/admin/` and login

### 2. Configure Site Branding
- Click **"Site Configuration"**
- Set:
  - College Name (e.g., "School of Science and Technology")
  - Short Name (e.g., "SOST")
  - Tagline/Motto
  - Established Year
  - About Us text
  - Mission & Vision
  - Social Media Links (Facebook, Twitter, Instagram, LinkedIn, YouTube)
  - Footer content

### 3. Upload Logo
- Click **"Manage Logo"**
- Upload college logo
- Set logo text and subtext

### 4. Add Programs
- Click **"Manage Programs"**
- Add each program (unlimited):
  - Program Code (e.g., "BIT", "MBA", "BCA")
  - Full Name
  - Description
  - Image for homepage card
  - Color Scheme (6 color options)
  - URL Slug (e.g., "bit" → accessible at `/bit/`)
  - Icon (Font Awesome class)
  - Features (bullet points with icons)

### 5. Add Curricula
- Click **"Manage Curriculum"**
- For each program:
  - Create curriculum
  - Add semesters (1-8)
  - Add courses per semester

### 6. Add Faculty
- Click **"Manage Faculty"**
- Add faculty members:
  - Name, Designation, Department
  - Photo, Email, Phone
  - Department can be **anything** (Computer Science, Agriculture, Engineering, Business, etc.)

### 7. Add Content
- **Slideshows**: Upload images for homepage hero/gallery
- **About Sections**: Build custom About Us page
- **Hero Slides**: Multiple slides with different images/text
- **Notices & Events**: Post announcements
- **Contact Info**: Set address, phone, email, map

## 🏫 Multi-College Deployment

### For SOST Server:
```bash
# Setup
python manage.py migrate
python manage.py createsuperuser
python manage.py init_site_config

# Then customize in admin:
- College Name: "School of Science and Technology"
- Programs: BIT, B.Sc. Agriculture
- Departments: IT, Agriculture
```

### For College of Engineering Server:
```bash
# Setup (same commands)
python manage.py migrate
python manage.py createsuperuser
python manage.py init_site_config

# Then customize in admin:
- College Name: "College of Engineering"
- Programs: Civil Eng, Mechanical Eng, Electrical Eng
- Departments: Civil, Mechanical, Electrical
```

### For CTEVT Server:
```bash
# Setup (same commands)
python manage.py migrate
python manage.py createsuperuser
python manage.py init_site_config

# Then customize in admin:
- College Name: "CTEVT Technical College"
- Programs: Diploma in IT, Diploma in Construction
- Departments: Technical, Vocational
```

## ✨ Key Features

### ✅ Fully Customizable
- **Programs**: Add unlimited programs (BIT, MBA, BCA, Engineering, Medical, etc.)
- **Departments**: Any departments (IT, Agriculture, Engineering, Business, Medical, etc.)
- **Curricula**: Flexible semester system (1-8 semesters, any number of courses)
- **Faculty**: Unlimited faculty with photos and details
- **Content**: About Us sections, slideshows, hero banners

### ✅ Beautiful UI
- Modern Tailwind CSS design
- Responsive (mobile, tablet, desktop)
- Dynamic color theming per program
- Image slideshows and carousels
- Professional admin dashboard

### ✅ SEO Ready
- Meta descriptions and keywords
- Custom page titles
- Social media integration
- Clean URLs

## 📂 Admin Dashboard Features

- **Site Configuration**: College branding, social links, SEO
- **Programs**: Add/edit/delete programs with custom colors/icons
- **Curriculum**: Manage semesters and courses per program
- **Faculty**: Manage faculty members with photos
- **Image Slideshows**: Upload and manage image galleries
- **About Sections**: Build modular About Us pages
- **Hero Slides**: Multiple homepage hero slides
- **Notices & Events**: Post announcements
- **Contact Messages**: View form submissions

## 🎨 Customization Examples

### Program Color Schemes
Choose from 6 beautiful color schemes:
- Blue (default)
- Green
- Purple
- Red
- Orange
- Indigo

### URL Slugs
Programs automatically get clean URLs:
- `/bit/` - Bachelor of Information Technology
- `/mba/` - Master of Business Administration
- `/agriculture/` - B.Sc. Agriculture
- `/civil-engineering/` - Civil Engineering

### Department Flexibility
Add any departments:
- Computer Science
- Agriculture
- Civil Engineering
- Business Administration
- Medical Sciences
- ... anything!

## 🔧 Technical Details

- **Framework**: Django 5.2.8
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Tailwind CSS
- **Icons**: Font Awesome
- **Authentication**: Django built-in + bcrypt

## 📱 Features for Visitors

- Browse programs and curricula
- View faculty profiles
- Read notices and events
- View image galleries
- Contact form
- About Us page
- Responsive mobile design

## 🎯 Perfect For

- Schools of Science & Technology
- Engineering Colleges
- Technical/Vocational Colleges
- Business Schools
- Medical Colleges
- Any educational institution!

## 📞 Support

Just customize everything through the admin dashboard. No coding required!

---

**One System. Any College. Completely Customizable.** 🎓
