from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    # Legacy URLs for backwards compatibility
    path("programs/bit/", views.bit, name="bit"),
    path("programs/agriculture/", views.agriculture, name="agriculture"),
    path("faculty/<int:pk>/", views.faculty_detail, name="faculty_detail"),
    path("account/manage/", views.manage_account, name="manage_account"),
    # Public Notice Pages
    path("notices/", views.notices_page, name="notices_page"),
    path("notices/<int:pk>/", views.notice_detail, name="notice_detail"),
    # Public Event Pages
    path("events/", views.events_page, name="events_page"),
    path("events/<int:pk>/", views.event_detail, name="event_detail"),
    # Public Pages
    path("programs/", views.programs_page, name="programs"),
    path("faculty/", views.faculty_page, name="faculty"),
    path("contact/", views.contact_page, name="contact"),
    # Public Gallery
    path("gallery/", views.gallery_page, name="gallery"),
    path("gallery/<int:pk>/", views.gallery_album_detail, name="gallery_album_detail"),
    # Admin Dashboard
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    # Notice Management
    path("admin/notices/", views.notice_list, name="notice_list"),
    path("admin/notices/add/", views.notice_add, name="notice_add"),
    path("admin/notices/<int:pk>/edit/", views.notice_edit, name="notice_edit"),
    path("admin/notices/<int:pk>/delete/", views.notice_delete, name="notice_delete"),
    path("admin/notices/reorder/", views.notice_reorder, name="notice_reorder"),
    # Event Management
    path("admin/events/", views.event_list, name="event_list"),
    path("admin/events/add/", views.event_add, name="event_add"),
    path("admin/events/<int:pk>/edit/", views.event_edit, name="event_edit"),
    path("admin/events/<int:pk>/delete/", views.event_delete, name="event_delete"),
    # Faculty Management
    path("admin/faculty/", views.faculty_list, name="faculty_list"),
    path("admin/faculty/add/", views.faculty_add, name="faculty_add"),
    path("admin/faculty/<int:pk>/edit/", views.faculty_edit, name="faculty_edit"),
    path("admin/faculty/<int:pk>/delete/", views.faculty_delete, name="faculty_delete"),
    path("admin/faculty/reorder/", views.faculty_reorder, name="faculty_reorder"),
    # Faculty Tab Management
    path("admin/faculty-tabs/", views.faculty_tab_list, name="faculty_tab_list"),
    path("admin/faculty-tabs/add/", views.faculty_tab_add, name="faculty_tab_add"),
    path(
        "admin/faculty-tabs/<int:pk>/edit/",
        views.faculty_tab_edit,
        name="faculty_tab_edit",
    ),
    path(
        "admin/faculty-tabs/<int:pk>/delete/",
        views.faculty_tab_delete,
        name="faculty_tab_delete",
    ),
    # Page Content Management
    path("admin/page-content/", views.page_content, name="page_content"),
    # Hero Management
    path("admin/hero/", views.hero_list, name="hero_list"),
    path("admin/hero/add/", views.hero_add, name="hero_add"),
    path("admin/hero/<int:pk>/edit/", views.hero_edit, name="hero_edit"),
    path("admin/hero/<int:pk>/delete/", views.hero_delete, name="hero_delete"),
    
    path("admin/logo/edit/", views.logo_edit, name="logo_edit"),
    path("admin/marquee/add/", views.marquee_add, name="marquee_add"),
    path("admin/marquee/<int:pk>/edit/", views.marquee_edit, name="marquee_edit"),
    path("admin/marquee/<int:pk>/delete/", views.marquee_delete, name="marquee_delete"),
    path(
        "admin/principal-message/edit/",
        views.principal_message_edit,
        name="principal_message_edit",
    ),
    path("admin/contact-info/edit/", views.contact_info_edit, name="contact_info_edit"),
    # Footer Link Management
    path("admin/footer-links/", views.footer_link_list, name="footer_link_list"),
    path("admin/footer-links/add/", views.footer_link_add, name="footer_link_add"),
    path(
        "admin/footer-links/<int:pk>/edit/",
        views.footer_link_edit,
        name="footer_link_edit",
    ),
    path(
        "admin/footer-links/<int:pk>/delete/",
        views.footer_link_delete,
        name="footer_link_delete",
    ),
    # Curriculum Management
    path("admin/curriculum/", views.curriculum_list, name="curriculum_list"),
    path("admin/curriculum/add/", views.curriculum_add, name="curriculum_add"),
    path("admin/curriculum/<int:pk>/edit/", views.curriculum_edit, name="curriculum_edit"),
    path(
        "admin/curriculum/<int:pk>/delete/",
        views.curriculum_delete,
        name="curriculum_delete",
    ),
    path(
        "admin/curriculum/<int:curriculum_pk>/semester/add/",
        views.semester_add,
        name="semester_add",
    ),
    path(
        "admin/curriculum/semester/<int:pk>/edit/",
        views.semester_edit,
        name="semester_edit",
    ),
    path(
        "admin/curriculum/semester/<int:pk>/delete/",
        views.semester_delete,
        name="semester_delete",
    ),
    path(
        "admin/curriculum/semester/<int:semester_pk>/course/add/",
        views.course_add,
        name="course_add",
    ),
    path("admin/curriculum/course/<int:pk>/edit/", views.course_edit, name="course_edit"),
    path(
        "admin/curriculum/course/<int:pk>/delete/",
        views.course_delete,
        name="course_delete",
    ),
    # Program Management
    path("admin/programs/", views.program_list, name="program_list"),
    path("admin/programs/add/", views.program_add, name="program_add"),
    path("admin/programs/<int:pk>/edit/", views.program_edit, name="program_edit"),
    path(
        "admin/programs/<int:pk>/delete/",
        views.program_delete,
        name="program_delete",
    ),
    path(
        "admin/programs/<int:program_pk>/feature/add/",
        views.program_feature_add,
        name="program_feature_add",
    ),
    path(
        "admin/programs/feature/<int:pk>/edit/",
        views.program_feature_edit,
        name="program_feature_edit",
    ),
    path(
        "admin/programs/feature/<int:pk>/delete/",
        views.program_feature_delete,
        name="program_feature_delete",
    ),
    # Contact Messages
    path("admin/messages/", views.message_list, name="message_list"),
    path("admin/messages/<int:pk>/", views.message_view, name="message_view"),
    path("admin/messages/<int:pk>/delete/", views.message_delete, name="message_delete"),
    # Site Configuration
    path("admin/site-config/edit/", views.site_configuration_edit, name="site_config_edit"),
    # Image Slideshows
    path("admin/slideshows/", views.slideshow_list, name="slideshow_list"),
    path("admin/slideshows/add/", views.slideshow_add, name="slideshow_add"),
    path("admin/slideshows/<int:pk>/edit/", views.slideshow_edit, name="slideshow_edit"),
    path(
        "admin/slideshows/<int:pk>/delete/",
        views.slideshow_delete,
        name="slideshow_delete",
    ),
    # Gallery Album Management
    path("admin/albums/", views.album_list, name="album_list"),
    path("admin/albums/add/", views.album_add, name="album_add"),
    path("admin/albums/<int:pk>/edit/", views.album_edit, name="album_edit"),
    path("admin/albums/<int:pk>/delete/", views.album_delete, name="album_delete"),
    # Gallery Management
    path("admin/gallery/", views.gallery_list, name="gallery_list"),
    path("admin/gallery/add/", views.gallery_add, name="gallery_add"),
    path("admin/gallery/<int:pk>/edit/", views.gallery_edit, name="gallery_edit"),
    path("admin/gallery/<int:pk>/delete/", views.gallery_delete, name="gallery_delete"),
    path("admin/gallery/reorder/", views.gallery_reorder, name="gallery_reorder"),
    # About Sections
    path("admin/about-sections/", views.about_section_list, name="about_section_list"),
    path("admin/about-sections/add/", views.about_section_add, name="about_section_add"),
    path(
        "admin/about-sections/<int:pk>/edit/",
        views.about_section_edit,
        name="about_section_edit",
    ),
    path(
        "admin/about-sections/<int:pk>/delete/",
        views.about_section_delete,
        name="about_section_delete",
    ),
    # Public About Page
    path("about/", views.about_page, name="about"),
    # Dynamic curriculum pages (must be last to avoid catching other URLs)
    path("<slug:slug>/", views.curriculum_page, name="curriculum_page"),
]
