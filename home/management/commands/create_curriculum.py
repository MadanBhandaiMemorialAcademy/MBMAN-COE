from django.core.management.base import BaseCommand

from home.models import Course, Curriculum, CurriculumSemester


class Command(BaseCommand):
    help = "Create initial curriculum entries for BIT and Agriculture programs"

    def handle(self, *args, **kwargs):
        # Create BIT Curriculum
        bit_curriculum, created = Curriculum.objects.get_or_create(
            program="BIT",
            defaults={
                "overview_text": "The Bachelor of Information Technology (BIT) program is designed to provide students with comprehensive knowledge in software development, network security, artificial intelligence, and modern IT practices. Our curriculum emphasizes hands-on learning, industry partnerships, and real-world project experience.",
                "duration": "4 Years",
                "is_active": True,
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Created BIT Curriculum"))
        else:
            self.stdout.write(self.style.WARNING("BIT Curriculum already exists"))

        # Create Agriculture Curriculum
        ag_curriculum, created = Curriculum.objects.get_or_create(
            program="AG",
            defaults={
                "overview_text": "The Bachelor of Science in Agriculture program combines traditional agricultural wisdom with modern scientific practices. Students learn sustainable farming techniques, crop management, soil science, and agri-entrepreneurship through extensive fieldwork and research.",
                "duration": "4 Years",
                "is_active": True,
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Created Agriculture Curriculum"))
        else:
            self.stdout.write(self.style.WARNING("Agriculture Curriculum already exists"))

        # Create sample semesters and courses for BIT
        if bit_curriculum:
            self._create_bit_semesters(bit_curriculum)

        # Create sample semesters and courses for Agriculture
        if ag_curriculum:
            self._create_ag_semesters(ag_curriculum)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created curriculum entries! You can now edit them in the admin dashboard."
            )
        )

    def _create_bit_semesters(self, curriculum):
        """Create sample semesters and courses for BIT"""
        # Semester 1
        sem1, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=1,
            defaults={"description": "Foundation courses"},
        )
        if created:
            Course.objects.create(
                semester=sem1,
                code="CSC 109",
                title="Computer Fundamentals & Application",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem1,
                code="MTH 112",
                title="Mathematics I",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem1,
                code="PHY 113",
                title="Physics",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem1,
                code="ENG 114",
                title="English I",
                credits=3,
                display_order=4,
            )

        # Semester 2
        sem2, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=2,
            defaults={"description": "Core programming concepts"},
        )
        if created:
            Course.objects.create(
                semester=sem2,
                code="CSC 160",
                title="C Programming",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem2,
                code="MTH 162",
                title="Mathematics II",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem2,
                code="STA 163",
                title="Statistics I",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem2,
                code="ENG 164",
                title="English II",
                credits=3,
                display_order=4,
            )

        # Semester 3
        sem3, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=3,
            defaults={"description": "Data structures and algorithms"},
        )
        if created:
            Course.objects.create(
                semester=sem3,
                code="CSC 206",
                title="Data Structure and Algorithms",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem3,
                code="CSC 207",
                title="Numerical Methods",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem3,
                code="CSC 208",
                title="Object Oriented Programming",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem3,
                code="STA 209",
                title="Statistics II",
                credits=3,
                display_order=4,
            )

        # Semester 4
        sem4, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=4,
            defaults={"description": "Operating systems and databases"},
        )
        if created:
            Course.objects.create(
                semester=sem4,
                code="CSC 257",
                title="Operating System",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem4,
                code="CSC 258",
                title="Database Management System",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem4,
                code="CSC 259",
                title="System Analysis and Design",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem4,
                code="CSC 260",
                title="Discrete Structure",
                credits=3,
                display_order=4,
            )

    def _create_ag_semesters(self, curriculum):
        """Create sample semesters and courses for Agriculture"""
        # Semester 1
        sem1, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=1,
            defaults={"description": "Agricultural foundations"},
        )
        if created:
            Course.objects.create(
                semester=sem1,
                code="AGR 101",
                title="Introduction to Agriculture",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem1,
                code="BOT 102",
                title="Agricultural Botany",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem1,
                code="CHE 103",
                title="Agricultural Chemistry",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem1,
                code="ENG 104",
                title="English",
                credits=3,
                display_order=4,
            )

        # Semester 2
        sem2, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=2,
            defaults={"description": "Soil and crop science basics"},
        )
        if created:
            Course.objects.create(
                semester=sem2,
                code="AGR 151",
                title="Fundamentals of Soil Science",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem2,
                code="AGR 152",
                title="Principles of Crop Production",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem2,
                code="BIO 153",
                title="Agricultural Microbiology",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem2,
                code="STA 154",
                title="Statistics",
                credits=3,
                display_order=4,
            )

        # Semester 3
        sem3, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=3,
            defaults={"description": "Plant protection and genetics"},
        )
        if created:
            Course.objects.create(
                semester=sem3,
                code="AGR 201",
                title="Principles of Plant Pathology",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem3,
                code="AGR 202",
                title="Principles of Entomology",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem3,
                code="AGR 203",
                title="Principles of Genetics",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem3,
                code="AGR 204",
                title="Irrigation and Drainage",
                credits=3,
                display_order=4,
            )

        # Semester 4
        sem4, created = CurriculumSemester.objects.get_or_create(
            curriculum=curriculum,
            semester_number=4,
            defaults={"description": "Livestock and agricultural economics"},
        )
        if created:
            Course.objects.create(
                semester=sem4,
                code="AGR 251",
                title="Animal Husbandry",
                credits=3,
                display_order=1,
            )
            Course.objects.create(
                semester=sem4,
                code="AGR 252",
                title="Agricultural Economics",
                credits=3,
                display_order=2,
            )
            Course.objects.create(
                semester=sem4,
                code="AGR 253",
                title="Agronomy",
                credits=3,
                display_order=3,
            )
            Course.objects.create(
                semester=sem4,
                code="AGR 254",
                title="Farm Machinery and Equipment",
                credits=3,
                display_order=4,
            )
