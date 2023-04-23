from django.views.generic import TemplateView

from projects.models import Project
from users.models import User


class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["project_list"] = Project.objects.all()[:6]
        context["user_list"] = User.objects.exclude(is_staff=True)[:6]
        return context
