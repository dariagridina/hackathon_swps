from django.contrib import admin
from projects.models import Project, ProjectRole, ProjectTag, ProjectRoleReview


class ProjectRoleInline(admin.TabularInline):
    model = ProjectRole
    extra = 1


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectRoleInline,
        ProjectTagInline,
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRoleReview)
