from django.views.generic import TemplateView

from projects.models import Project
from users.models import User


class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        context["user_list"] = User.objects.exclude(is_staff=True)
        return context
