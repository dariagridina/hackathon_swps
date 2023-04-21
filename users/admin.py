from django.contrib import admin

from users.models import User, UserProfile, UserSkill


class UserSkillInline(admin.TabularInline):
    model = UserSkill
    extra = 1


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1
    min_num = 1
    max_num = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserProfileInline,
        UserSkillInline,
    ]


admin.site.register(User, UserAdmin)
