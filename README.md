# MBMAN College of Engineering (SOST)

A comprehensive college website and management system built with Django for the School of Science & Technology, Madan Bhandari Memorial Academy Nepal (MBMAN).

![Dashboard Preview](docs/dashboard_preview.png) <!-- Add a screenshot if available -->

## 🚀 Features

### Public Website
*   **Dynamic Homepage**: Customizable Hero section, Scrolling Marquee for notices, Spotlight Gallery, and Principal's Message.
*   **Academic Programs**: Detailed pages for BIT, Agriculture, etc., with curriculum structure and semester details.
*   **Faculty Directory**: Categorized faculty members with profiles, social links, and contact info.
*   **Notices & Events**: Dedicated pages for announcements and events with priority highlighting.
*   **Photo Gallery**: Album-based masonry gallery with lightbox viewer and cover slideshows.
*   **About Us**: Customizable sections for history, mission, vision, and leadership.

### Admin Dashboard (`/admin/`)
*   **Custom Dashboard**: A user-friendly, non-technical dashboard for staff to manage content.
*   **Drag-and-Drop Sorting**: Easily reorder Notices, Faculty members, and Gallery images/albums.
*   **Image Management**:
    *   **Gallery**: Create albums, upload bulk photos, set cover images.
    *   **Spotlight**: Mark images to feature on the homepage spotlight section.
    *   **Hero Slides**: Manage homepage carousel slides.
*   **Site Configuration**: Update college name, logo, social links, footer text, and SEO metadata without touching code.
*   **Content Management**:
    *   Add/Edit Faculty with department categorization.
    *   Manage Notices (Urgent, Highlight, Normal).
    *   Update Curriculum and Courses.

## 🛠 Technology Stack

*   **Backend**: Django 5.2 (Python 3.12+)
*   **Database**: SQLite (Dev) / MySQL (Prod)
*   **Frontend**: HTML5, Tailwind CSS, JavaScript
*   **Media Storage**: Local Storage or Cloudinary (Configurable via .env)
*   **Deployment**: cPanel / Linux Server compatible

## 📦 Installation & Setup

### Prerequisites
*   Python 3.12+
*   `uv` (Recommended) or `pip`

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mbman-coe.git
cd mbman-coe
```

### 2. Set Up Environment
Create a `.env` file in the project root (use `.env.example` as a template):
```ini
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost,https://yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
# Optional: Cloudinary for media
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 3. Install Dependencies
Using `uv`:
```bash
uv sync
```
Or using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Run migrations to set up the database schema:
```bash
python manage.py migrate
```

### 5. Create Admin User
Create a superuser to access the dashboard:
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to view the site.
Visit `http://127.0.0.1:8000/admin/` to access the dashboard.

## 🚀 Deployment (cPanel/Linux)

1.  **Upload Code**: Upload project files to your server.
2.  **Install Dependencies**: `pip install -r requirements.txt`
    *   *Note:* If `mysqlclient` fails on cPanel, `pymysql` is included as a fallback.
3.  **Configure .env**: Ensure your production `.env` has `DEBUG=False` and correct database credentials.
4.  **Static Files**:
    ```bash
    python manage.py collectstatic
    ```
5.  **Migrations**:
    ```bash
    python manage.py migrate
    ```
6.  **Restart App**: Restart your Python application via cPanel or systemd.

## 📁 Project Structure

```
mbman-coe/
├── config/             # Project settings & WSGI/ASGI config
├── home/               # Main app (Views, Models, URL conf)
├── templates/          # HTML Templates
│   ├── base.html       # Base layout
│   └── home/           # App-specific templates
├── static/             # CSS, JS, Images
├── media/              # User uploaded files (if local storage)
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📝 License

This project is licensed under the MIT License.
