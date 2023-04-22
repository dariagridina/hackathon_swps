from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand

from projects.models import Project, ProjectRole, ProjectRoleReview
from users.models import User, UserProfile, UserSkill


people_images = settings.BASE_DIR / "main" / "code_fixtures" / "images" / "people"


class Command(BaseCommand):
    help = "Loads code fixtures"

    def handle(self, *args, **options):
        self.load_fixtures()

    def load_fixtures(self):
        self.setup_users()
        self.setup_projects()

    def setup_users(self):
        User.objects.all().delete()
        admin = User.objects.create_superuser(
            email="admin@example.com",
            password="admin",
            first_name="Jane",
            last_name="Doe",
        )
        profile = UserProfile.objects.create(
            user=admin,
            image="",
            bio="I am a project manager with 10 years of experience in the IT industry. I have a strong background in "
            "software development and project management. I am passionate about building and managing high "
            "performing teams and delivering successful projects.",
            location="Warsaw",
            linkedin_url="https://www.linkedin.com/in/admin/",
            github_url="https://github.com/admin/",
        )
        with open(people_images / "01.jpg", "rb") as image:
            profile.image.save(
                "admin.jpg",
                SimpleUploadedFile("admin.jpg", image.read(), content_type="image/jpg"),
            )
        UserSkill.objects.create(
            user=admin,
            name="Project Management",
        )
        UserSkill.objects.create(
            user=admin,
            name="Scrum",
        )
        UserSkill.objects.create(
            user=admin,
            name="Agile",
        )

        user1 = User.objects.create_user(
            email="user1@example.com",
            password="user1",
            first_name="John",
            last_name="Smith",
        )
        profile1 = UserProfile.objects.create(
            user=user1,
            image="",
            bio="Hi! I'm a passionate web developer with expertise in React.js and Node.js. With a keen eye for design and "
            "a strong foundation in programming, I love transforming creative ideas into functional and visually "
            "appealing web applications. Always eager to learn and stay updated with the latest trends, I strive "
            "to build user-centric solutions that make a positive impact.",
            location="Warsaw",
            linkedin_url="https://www.linkedin.com/in/user1/",
            github_url="https://github.com/user1/",
        )
        with open(people_images / "02.jpg", "rb") as image:
            profile1.image.save(
                "user1.jpg",
                SimpleUploadedFile("user1.jpg", image.read(), content_type="image/jpg"),
            )

        UserSkill.objects.create(
            user=user1,
            name="React.js",
        )
        UserSkill.objects.create(
            user=user1,
            name="Node.js",
        )
        UserSkill.objects.create(
            user=user1,
            name="HTML",
        )
        UserSkill.objects.create(
            user=user1,
            name="CSS",
        )

        user2 = User.objects.create_user(
            email="user2@example.com",
            password="user2",
            first_name="Sarah",
            last_name="Connor",
        )
        profile2 = UserProfile.objects.create(
            user=user2,
            image="",
            bio="I am a designer with a passion for creating beautiful and functional web applications. I love working "
            "with a team of talented developers to bring ideas to life. I am always looking for new challenges "
            "and opportunities to learn and grow.",
            location="London",
            linkedin_url="https://www.linkedin.com/in/user2/",
            github_url="https://github.com/user2/",
        )
        with open(people_images / "03.jpg", "rb") as image:
            profile2.image.save(
                "user2.jpg",
                SimpleUploadedFile("user2.jpg", image.read(), content_type="image/jpg"),
            )
        UserSkill.objects.create(
            user=user2,
            name="Figma",
        )
        UserSkill.objects.create(
            user=user2,
            name="Adobe XD",
        )
        UserSkill.objects.create(
            user=user2,
            name="HTML",
        )

        user3 = User.objects.create_user(
            email="user3@example.com",
            password="user3",
            first_name="Timothy",
            last_name="Jones",
        )
        profile3 = UserProfile.objects.create(
            user=user3,
            image="",
            bio="I am a marketing specialist. I want to help you grow your business by creating a strong online "
            "presence and building a loyal customer base. I have experience in SEO, social media marketing, and "
            "content marketing. I am always looking for new opportunities to learn and grow.",
            location="New York",
            linkedin_url="https://www.linkedin.com/in/user3/",
        )
        with open(people_images / "04.jpg", "rb") as image:
            profile3.image.save(
                "user3.jpg",
                SimpleUploadedFile("user3.jpg", image.read(), content_type="image/jpg"),
            )
        UserSkill.objects.create(
            user=user3,
            name="SEO",
        )
        UserSkill.objects.create(
            user=user3,
            name="Social Media Marketing",
        )
        UserSkill.objects.create(
            user=user3,
            name="Content Marketing",
        )

    def setup_projects(self):
        Project.objects.all().delete()
        project1 = Project.objects.create(
            name="GreenApp",
            description="GreenApp is a web application that helps users reduce their carbon footprint by providing "
            "them with personalized tips and advice on how to live a more sustainable lifestyle. "
            "The app also allows users to track their progress and compare their carbon footprint "
            "with other users.",
            location="Remote",
            ended=True,
            responsible_user=User.objects.get(email="admin@example.com"),
        )
        project1_pm = ProjectRole.objects.create(
            project=project1,
            user=User.objects.get(email="admin@example.com"),
            name="Project Manager",
            description="Overseeing and coordinating all aspects of project development from inception to completion. Defining project scope, goals, and deliverables while ensuring alignment with business objectives. Developing detailed project plans, including schedules, resource allocation, and budgets. Managing cross-functional teams, fostering a collaborative environment, and ensuring clear communication among stakeholders. Identifying potential risks and implementing appropriate mitigation strategies. Monitoring project progress, making data-driven decisions, and adjusting plans as needed to meet deadlines and maintain quality. Conducting post-project evaluations to measure success and identify areas for improvement.",
        )
        project1_webdev = ProjectRole.objects.create(
            project=project1,
            user=User.objects.get(email="user1@example.com"),
            name="Web Developer",
            description="Developing and maintaining the front-end of the web application. Working closely with the UI/UX designer to implement designs and ensure a smooth user experience. Ensuring the technical feasibility of UI/UX designs. Optimizing application for maximum speed and scalability. Collaborating with other team members and stakeholders.",
        )
        project1_uxui = ProjectRole.objects.create(
            project=project1,
            user=User.objects.get(email="user2@example.com"),
            name="UI/UX Designer",
            description="Designing and implementing the user interface of the web application. Working closely with the web developer to implement designs and ensure a smooth user experience. Conducting user research and testing to inform design decisions. Creating wireframes, prototypes, and mockups to effectively communicate interaction and design ideas. Collaborating with other team members and stakeholders.",
        )
        project1_marketing = ProjectRole.objects.create(
            project=project1,
            user=User.objects.get(email="user3@example.com"),
            name="Marketing Specialist",
            description="Developing and implementing marketing strategies to promote the web application. Conducting market research to identify opportunities for growth. Creating and managing content for the web application. Managing social media accounts and creating social media campaigns. Collaborating with other team members and stakeholders.",
        )
        ProjectRoleReview.objects.create(
            role=project1_pm,
            reviewer_role=project1_webdev,
            text="Great project manager. Very organized and always on top of things.",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_pm,
            reviewer_role=project1_uxui,
            text="I don't think I've ever worked with a better project manager. ",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_pm,
            reviewer_role=project1_marketing,
            text="She has some problems with communication.",
            rating=4,
        )
        ProjectRoleReview.objects.create(
            role=project1_webdev,
            reviewer_role=project1_pm,
            text="Great web developer. Very organized and always on top of things. ",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_webdev,
            reviewer_role=project1_uxui,
            text="I don't think I've ever worked with a better web developer. ",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_webdev,
            reviewer_role=project1_marketing,
            text="He has some problems with communication.",
            rating=3,
        )
        ProjectRoleReview.objects.create(
            role=project1_uxui,
            reviewer_role=project1_pm,
            text="Great UI/UX designer. Very organized and always on top of things.",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_uxui,
            reviewer_role=project1_webdev,
            text="I don't think I've ever worked with a better UI/UX designer.",
            rating=5,
        )
        ProjectRoleReview.objects.create(
            role=project1_uxui,
            reviewer_role=project1_marketing,
            text="Good UI/UX designer.",
            rating=4,
        )

        project2 = Project.objects.create(
            name="E-Commerce App",
            description="E-Commerce App is a web application that allows users to buy and sell products online. "
            "The app also allows users to create their own online stores and manage their inventory.",
            location="Remote",
            ended=False,
            responsible_user=User.objects.get(email="user2@example.com"),
        )
        project2_pm = ProjectRole.objects.create(
            project=project2,
            user=User.objects.get(email="admin@example.com"),
            name="Project Manager",
            description="Directing project development from initiation to closure. Establishing project objectives, schedules, and resource allocation. Leading cross-functional teams, promoting clear communication, and mitigating risks. Monitoring progress and adjusting plans to meet deadlines and maintain quality. Analyzing project outcomes for continuous improvement.",
        )
        project2_webdev = ProjectRole.objects.create(
            project=project2,
            user=None,
            name="Web Developer",
            description="Designing and developing web applications using modern technologies. Collaborating with designers to create user-friendly interfaces. Ensuring optimal performance and responsiveness. Adapting to project requirements and implementing updates. Staying current with industry trends for continuous growth.",
        )
        project2_uxui = ProjectRole.objects.create(
            project=project2,
            user=None,
            name="UI/UX Designer",
            description="Creating intuitive and visually appealing designs for digital platforms. Collaborating with developers for seamless integration. Utilizing design tools to produce graphics and prototypes. Conducting user research and usability testing to inform design decisions. Keeping up with industry trends for continuous improvement.",
        )
