from django.contrib import admin
from projects.models import Project, ProjectMember, ProjectTag, ProjectMemberReview


class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember
    extra = 1


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectMemberInline,
        ProjectTagInline,
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMemberReview)
