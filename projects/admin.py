from django.contrib import admin
from projects.models import Project, ProjectRole, ProjectRoleReview


class ProjectRoleInline(admin.TabularInline):
    model = ProjectRole
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectRoleInline,
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRoleReview)
