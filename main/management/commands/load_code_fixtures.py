import itertools
import random

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand

from projects.models import Project, ProjectRole, ProjectRoleReview
from users.models import User, UserProfile, UserSkill

people_images = settings.BASE_DIR / "main" / "code_fixtures" / "images" / "people"


class Command(BaseCommand):
    help = "Loads code fixtures"

    PROJECT_MANAGERS = []
    DEVELOPERS = []
    DESIGNERS = []
    MARKETERS = []
    REVIEWS = [
        [
            5,
            "{name} has shown exceptional dedication to this project, consistently going above and beyond to deliver high-quality results.",
        ],
        [
            5,
            "{name}'s keen eye for detail and innovative ideas have truly elevated the project to new heights.",
        ],
        [
            5,
            "Working with {name} has been a phenomenal experience; their commitment to teamwork and clear communication has made the project a great success.",
        ],
        [
            5,
            "The level of expertise and professionalism {name} brings to the project is simply outstanding, making them a true asset to the team.",
        ],
        [
            5,
            "I am continually impressed by {name}'s ability to adapt and overcome any challenge that arises, ensuring the project's success.",
        ],
        [
            5,
            "{name}'s passion for the project is contagious, inspiring the entire team to strive for excellence.",
        ],
        [
            5,
            "The time and effort {name} has put into the project is truly remarkable, resulting in a top-notch final product.",
        ],
        [
            5,
            "Thanks to {name}'s thorough research and in-depth understanding of the subject matter, the project has reached new levels of quality and impact.",
        ],
        [
            5,
            "{name} has been an essential team player, providing valuable insights and helping to create a positive and collaborative work environment.",
        ],
        [
            5,
            "With {name}'s exceptional organizational skills and steadfast work ethic, the project has been completed on time and with great success.",
        ],
        [
            5,
            "The exceptional dedication shown throughout this project has consistently led to high-quality results and a fantastic final product.",
        ],
        [
            5,
            "Innovative ideas and a keen eye for detail have truly elevated the project, setting a new standard for future work.",
        ],
        [
            5,
            "The teamwork and clear communication demonstrated during the project made it a great success and a pleasure to work on.",
        ],
        [
            5,
            "The level of expertise and professionalism exhibited throughout the project has been outstanding, making it a truly remarkable experience.",
        ],
        [
            5,
            "A contagious passion for the project inspired the entire team to strive for excellence, resulting in a top-notch final product.",
        ],
        [
            4,
            "{name}'s work on the project has been solid, with a few minor areas for improvement that could take their contributions to the next level.",
        ],
        [
            4,
            "The project was successful, but a bit more attention to detail could have made it even better. {name} still did a commendable job overall.",
        ],
        [
            4,
            "While the project was well-executed, there were a few instances where clearer communication would have helped streamline the process.",
        ],
        [
            4,
            "{name} displayed good organization and contributed effectively, but there is room for growth in terms of collaboration with the team.",
        ],
        [
            4,
            "The final product was of good quality, but with a bit more creativity and innovation, it could have truly stood out from the competition.",
        ],
        [
            2,
            "{name}'s work on the project was below expectations, with numerous errors and a lack of attention to detail that impacted the final result.",
        ],
        [
            2,
            "The work was completed, but the final product was unimpressive and failed to meet the necessary standards for quality and impact.",
        ],
        [
            1,
            "The project was severely lacking in organization, communication, and quality, resulting in a final product that was far below expectations and unacceptable.",
        ],
        [
            1,
            "Despite the time and resources invested, the project failed to meet even the most basic requirements, with numerous errors and a complete lack of attention to detail.",
        ],
    ]

    def handle(self, *args, **options):
        self.load_fixtures()

    def load_fixtures(self):
        self.setup_users()
        self.setup_projects()

    def create_user(
        self, first_name, last_name, bio, location, skills, linkedin=False, github=False
    ):
        user_count = User.objects.count()
        user = User.objects.create_user(
            email=f"user{user_count}@mail.com",
            password="user",
            first_name=first_name,
            last_name=last_name,
        )
        profile = UserProfile.objects.create(
            user=user,
            bio=bio,
            location=location,
            linkedin_url=f"https://www.linkedin.com/in/user{user_count}/"
            if linkedin
            else "",
            github_url=f"https://github.com/user{user_count}/" if github else "",
        )
        with open(people_images / f"{user_count}.jpg", "rb") as image:
            profile.image.save(
                f"{user_count}.jpg",
                SimpleUploadedFile(
                    f"{user_count}.jpg", image.read(), content_type="image/jpg"
                ),
            )
        for skill in skills:
            UserSkill.objects.create(
                user=user,
                name=skill,
            )

        return user

    def setup_users(self):
        User.objects.all().delete()
        User.objects.create_superuser(
            email="admin@example.com",
            password="admin",
        )

        self.PROJECT_MANAGERS += [
            self.create_user(
                first_name="Jane",
                last_name="Doe",
                bio="I am a project manager with 10 years of experience in the IT industry. I have a strong background in software development and project management.",
                location="Warsaw",
                skills=["Project Management", "Scrum", "Agile"],
                linkedin=True,
            ),
            self.create_user(
                first_name="Robb",
                last_name="Stark",
                bio="I am a strong leader with a passion for project management. I used to work with mobile app development teams and I love working with talented developers.",
                location="Winterfell",
                skills=["Project Management"],
                linkedin=True,
            ),
        ]

        self.DEVELOPERS += [
            self.create_user(
                first_name="John",
                last_name="Smith",
                bio="I'm a front-end developer with expertise in React.js. I love transforming creative ideas into functional and visually appealing web applications.",
                location="Warsaw",
                skills=["React.js", "HTML", "CSS"],
                linkedin=True,
                github=True,
            ),
            self.create_user(
                first_name="Jessica",
                last_name="Williams",
                bio="I am a full-stack developer with 5 years of experience in the IT industry. I build web applications using React.js and Django.",
                location="London",
                skills=["React.js", "HTML", "CSS", "Python", "Django"],
                linkedin=True,
                github=True,
            ),
            self.create_user(
                first_name="Michael",
                last_name="Brown",
                bio="I am a data scientist with 3 years of experience in the IT industry. I have a strong background in data analysis and machine learning.",
                location="New York",
                skills=["Python", "Machine Learning", "Data Analysis"],
                linkedin=True,
                github=True,
            ),
            self.create_user(
                first_name="James",
                last_name="Jones",
                bio="I am a back-end developer with 5 years of experience in the IT industry. I built scalable web applications using Python and Django.",
                location="London",
                skills=["Python", "Django", "HTML", "CSS"],
                linkedin=True,
                github=True,
            ),
            self.create_user(
                first_name="David",
                last_name="Black",
                bio="I am a full-stack developer with 5 years of experience in the IT industry. I have a strong background in web development and graphic design.",
                location="Barcelona",
                skills=["React.js", "HTML", "CSS", "Python", "Django"],
                linkedin=True,
                github=True,
            ),
            self.create_user(
                first_name="Sarah",
                last_name="Connor",
                bio="I am a front-end developer with 5 years of experience in the IT industry. I built multiple web applications using Vue.js and Django.",
                location="London",
                skills=["Vue.js", "HTML", "CSS"],
                linkedin=True,
                github=True,
            ),
        ]

        self.DESIGNERS += [
            self.create_user(
                first_name="Jeff",
                last_name="Snider",
                bio="I am a designer with a passion for creating beautiful and functional web applications. I love working with a team of talented developers to bring ideas to life.",
                location="London",
                skills=["Figma", "Adobe XD", "HTML", "CSS"],
                linkedin=True,
            ),
            self.create_user(
                first_name="Serhio",
                last_name="Ramos",
                bio="I am a UI/UX designer with 5 years of experience in the IT industry. I have a strong background in web design and graphic design.",
                location="Munich",
                skills=["UI/UX", "Graphic Design", "Adobe Photoshop"],
                linkedin=True,
            ),
            self.create_user(
                first_name="Anna",
                last_name="Johnson",
                bio="I am a graphic designer with 5 years of experience in the IT industry. I have a strong background in graphic design and web design.",
                location="Warsaw",
                skills=["Graphic Design", "Adobe Photoshop", "Adobe Illustrator"],
                linkedin=True,
            ),
        ]

        # Marketers
        self.MARKETERS += [
            self.create_user(
                first_name="Mark",
                last_name="Johnson",
                bio="I am a marketing specialist with 5 years of experience in the IT industry. I have a strong background in digital marketing and social media management.",
                location="London",
                skills=["Digital Marketing", "SMM", "Google Analytics"],
                linkedin=True,
            ),
            self.create_user(
                first_name="Samantha",
                last_name="Williams",
                bio="I have a passion for marketing and a strong background in digital marketing. I love working with a team of talented developers to bring ideas to life.",
                location="New York",
                skills=["Digital Marketing", "SMM", "SEO"],
                linkedin=True,
            ),
            self.create_user(
                first_name="Robert",
                last_name="Miller",
                bio="I am a marketing specialist with 5 years of experience in the IT industry. I have a strong background in digital marketing and social media management.",
                location="Warsaw",
                skills=["Digital Marketing", "SMM", "Google Analytics"],
                linkedin=True,
            ),
        ]

    def create_project(self, name, description, location, ended, owner, roles):
        project = Project.objects.create(
            name=name,
            description=description,
            location=location,
            ended=ended,
            responsible_user=owner,
        )

        ProjectRole.objects.create(
            project=project,
            user=owner,
            name="Project Manager",
            description="Overseeing and coordinating all aspects of project development from inception to completion. "
            "Defining project scope, goals, and deliverables while ensuring alignment with business "
            "objectives. "
            "Developing detailed project plans, including schedules, resource allocation, and budgets. "
            "Managing cross-functional teams, fostering a collaborative environment, and ensuring project "
            "milestones are met on time and within budget.",
        )
        for role in roles:
            ProjectRole.objects.create(project=project, **role)

        if ended:
            # Get all permutations of roles to create reviews for each other
            role_names = [
                [role["name"], role["user"]] for role in roles if role["user"]
            ] + [["Project Manager", owner]]
            for role1, role2 in list(itertools.permutations(role_names, 2)):
                rating, review_text = random.choice(self.REVIEWS)
                ProjectRoleReview.objects.create(
                    role=ProjectRole.objects.get(
                        project=project, user=role1[1], name=role1[0]
                    ),
                    reviewer_role=ProjectRole.objects.get(
                        project=project, user=role2[1], name=role2[0]
                    ),
                    text=review_text.format(name=role1[1].first_name),
                    rating=rating,
                )
        return project

    def setup_projects(self):
        Project.objects.all().delete()
        self.create_project(
            name="GreenApp",
            description="GreenApp is a web application that helps users to find the best eco-friendly products. "
            "The application is built using React.js and Django.",
            location="Remote",
            ended=True,
            owner=self.PROJECT_MANAGERS[0],
            roles=[
                {
                    "name": "Front-end developer",
                    "user": self.DEVELOPERS[0],
                    "description": "Developing the front-end of the application."
                },
                {
                    "name": "Full-stack developer",
                    "user": self.DEVELOPERS[1],
                    "description": "Developing the front-end and back-end of the application."
                },
                {
                    "name": "Designer",
                    "user": self.DESIGNERS[0],
                    "description": "Designing the user interface of the application."
                },
                {
                    "name": "Marketer",
                    "user": self.MARKETERS[0],
                    "description": "Marketing the application."
                },
            ],
        )

        self.create_project(
            name="Online Pharmacy",
            description="This application is an online pharmacy that allows users to order medicines online. ",
            location="New York",
            ended=True,
            owner=self.PROJECT_MANAGERS[1],
            roles=[
                {
                    "name": "Back-end developer",
                    "user": self.DEVELOPERS[3],
                    "description": "Developing the back-end of the application.",
                },
                {
                    "name": "Full-stack developer",
                    "user": self.DEVELOPERS[4],
                    "description": "Developing the front-end and back-end of the application.",
                },
                {
                    "name": "Data-Scientist",
                    "user": self.DEVELOPERS[2],
                    "description": "Developing the machine learning models for the application.",
                },
                {
                    "name": "Designer",
                    "user": self.DESIGNERS[1],
                    "description": "Designing the user interface of the application.",
                },
                {
                    "name": "Marketer",
                    "user": self.MARKETERS[1],
                    "description": "Marketing the application.",
                },
            ],
        )

        self.create_project(
            name="Social Media App",
            description="This application is a social media app that allows users to share their thoughts and ideas. ",
            location="London",
            ended=True,
            owner=self.PROJECT_MANAGERS[0],
            roles=[
                {
                    "name": "Full-stack developer",
                    "user": self.DEVELOPERS[2],
                    "description": "Developing the front-end and back-end of the application.",
                },
                {
                    "name": "Designer",
                    "user": self.DESIGNERS[2],
                    "description": "Designing the user interface of the application.",
                },
                {
                    "name": "Marketer",
                    "user": self.MARKETERS[2],
                    "description": "Marketing the application.",
                },
            ],
        )

        self.create_project(
            name="Online university",
            description="This application is an online university that allows users to take online courses. ",
            location="Warsaw",
            ended=False,
            owner=self.PROJECT_MANAGERS[0],
            roles=[
                {
                    "name": "Full-stack developer",
                    "user": None,
                    "description": "Developing the front-end and back-end of the application.",
                },
                {
                    "name": "Front-end developer",
                    "user": self.DEVELOPERS[5],
                    "description": "Developing the front-end of the application.",
                },
                {
                    "name": "Back-end developer",
                    "user": None,
                    "description": "Developing the back-end of the application.",
                },
                {
                    "name": "Marketer",
                    "user": None,
                    "description": "Marketing the application.",
                },
            ],
        )

        self.create_project(
            name="Delivery App",
            description="This application is a delivery app that allows users to order food online. ",
            location="Munich",
            ended=False,
            owner=self.PROJECT_MANAGERS[1],
            roles=[
                {
                    "name": "Full-stack developer",
                    "user": None,
                    "description": "Developing the front-end and back-end of the application.",
                },
                {
                    "name": "Designer",
                    "user": None,
                    "description": "Designing the user interface of the application.",
                },
            ],
        )
