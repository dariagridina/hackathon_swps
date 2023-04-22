from django.urls import path

from projects.views import ProjectDetailView, ProjectListView

urlpatterns = [
    path(
        "",
        ProjectListView.as_view(),
        name="project_list",
    ),
    path(
        "<int:pk>/",
        ProjectDetailView.as_view(),
        name="project_detail",
    ),
]
