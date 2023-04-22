from django.views.generic import DetailView, ListView

from projects.models import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_projects"] = Project.objects.exclude(
            id=self.object.id
        ).order_by("?")[:3]
        return context


class ProjectListView(ListView):
    model = Project
