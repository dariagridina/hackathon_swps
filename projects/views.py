from django.views.generic import DetailView, ListView

from projects.models import Project, ProjectRole
from django.db.models import Q


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_projects"] = (
            Project.objects.filter(category=self.object.category)
            .exclude(id=self.object.id)
            .order_by("?")[:3]
        )
        context["open_positions"] = ProjectRole.objects.filter(
            project=self.object, user__isnull=True
        )
        return context


class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        qs = Project.objects.filter(name__isnull=False)
        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category=category)
        location = self.request.GET.get("location")
        if location:
            qs = qs.filter(location=location)
        name = self.request.GET.get("name")
        if name:
            qs = qs.filter(Q(name__icontains=name))
        return qs.distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = list(
            Project.objects.all()
            .values_list("category", flat=True)
            .order_by("category")
            .distinct()
        )
        context["locations"] = list(
            Project.objects.all()
            .values_list("location", flat=True)
            .order_by("location")
            .distinct()
        )
        return context
