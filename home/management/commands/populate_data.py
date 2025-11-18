from django.core.management.base import BaseCommand

from home.models import (
    ContactInfo,
    Event,
    Faculty,
    HeroSection,
    MarqueeItem,
    Notice,
    PrincipalMessage,
    Program,
    ProgramFeature,
)


class Command(BaseCommand):
    help = "Populate database with initial sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database...")

        # Create Hero Section
        HeroSection.objects.get_or_create(
            title="Future Leaders in Technology & Agriculture",
            defaults={
                "subtitle": "Embark on a journey of practical excellence"
                " at Eastern Nepal's premier technical institute.",
                "is_active": True,
            },
        )

        # Create Marquee Items
        MarqueeItem.objects.get_or_create(
            text="BIT Entrance Results Published (Kartik 25)",
            defaults={"is_new": True, "display_order": 1},
        )
        MarqueeItem.objects.get_or_create(
            text="Scholarship Deadline Extended (Kartik 11)",
            defaults={"is_urgent": True, "display_order": 2},
        )
        MarqueeItem.objects.get_or_create(
            text="Tech Fest 2082 Registration Open", defaults={"display_order": 3}
        )

        # Create Notices
        Notice.objects.get_or_create(
            title="BIT Entrance Examination Results",
            defaults={
                "description": "The merit list for the 2082 batch has been"
                " published. Admitted students must visit the"
                " administration by Mangsir 5.",
                "date_bs": "Kartik 25, 2082",
                "priority": "normal",
            },
        )
        Notice.objects.get_or_create(
            title="URGENT: Scholarship Deadline Extended",
            defaults={
                "description": "Merit-based scholarship application deadline"
                " extended for 3 more days due to technical"
                " maintenance.",
                "date_bs": "Kartik 11, 2082",
                "priority": "urgent",
            },
        )

        # Create Events
        Event.objects.get_or_create(
            title="Eastern Nepal Tech Fest 2082",
            defaults={
                "description": "Join us for the largest technical exhibition"
                " in the province, featuring projects from BIT"
                " and Ag students.",
                "date_bs": "Poush 01",
                "time": "10:00 AM - 5:00 PM",
                "location": "Main Auditorium",
                "is_highlight": True,
            },
        )

        # Create Programs
        bit_program, created = Program.objects.get_or_create(
            code="BIT",
            defaults={
                "full_name": "Bachelor of Information Technology",
                "short_description": "A comprehensive program focusing on"
                " software engineering, artificial"
                " intelligence, and network security.",
                "full_description": "We emphasize practical coding skills"
                " and industry internships.",
                "duration": "4 Years / 8 Semesters",
            },
        )

        if created:
            # Create BIT Features
            features = [
                "Modern IT Labs",
                "Industry Tie-ups",
                "Project Based Learning",
                "Career Placement",
            ]
            for i, feature in enumerate(features):
                ProgramFeature.objects.create(
                    program=bit_program,
                    feature_text=feature,
                    icon="fas fa-check-circle",
                    display_order=i,
                )

        ag_program, created = Program.objects.get_or_create(
            code="AG",
            defaults={
                "full_name": "Bachelor of Science in Agriculture",
                "short_description": "Blending traditional farming wisdom"
                " with modern agricultural science.",
                "full_description": "Our program focuses on sustainable"
                " practices, research, and"
                " agri-entrepreneurship.",
                "duration": "4 Years / 8 Semesters",
            },
        )

        if created:
            # Create Agriculture Features
            features = [
                "Research Farms",
                "Field Visits",
                "Organic Farming",
                "Lab Facilities",
            ]
            for i, feature in enumerate(features):
                ProgramFeature.objects.create(
                    program=ag_program,
                    feature_text=feature,
                    icon="fas fa-check-circle",
                    display_order=i,
                )

        # Create Faculty
        Faculty.objects.get_or_create(
            name="Er. Sameer Sharma",
            defaults={
                "designation": "HoD, IT Department",
                "department": "IT",
                "specialization": "M.Sc. CSIT, specializing in AI & Data" " Science",
                "display_order": 1,
            },
        )
        Faculty.objects.get_or_create(
            name="Dr. Suman Adhikari",
            defaults={
                "designation": "HoD, Agriculture Dept.",
                "department": "AG",
                "specialization": "Ph.D. in Soil Science & Agronomy",
                "display_order": 1,
            },
        )

        # Create Principal Message
        PrincipalMessage.objects.get_or_create(
            principal_name="Prof. Dr. Name Surname",
            defaults={
                "quote": "Empowering the next generation of innovators for"
                " a prosperous Nepal.",
                "full_message": "At MBMAN School of Science & Technology,"
                " we believe in education that translates into"
                " action.",
                "principal_title": "Principal",
            },
        )

        # Create Contact Info
        ContactInfo.objects.get_or_create(
            email="info@mbman.edu.np",
            defaults={"phone": "+977-021-540000", "address": "Urlabari-3, Morang, Nepal"},
        )

        self.stdout.write(self.style.SUCCESS("Successfully populated database!"))
