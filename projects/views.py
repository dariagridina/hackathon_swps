from django.views.generic import DetailView, ListView

from projects.models import Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectListView(ListView):
    model = Project
