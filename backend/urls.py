from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "users/",
        include("users.urls"),
    ),
    path(
        "projects/",
        include("projects.urls"),
    ),
    path(
        "faq",
        TemplateView.as_view(template_name="main/faq.html"),
        name="faq",
    ),
    path(
        "",
        TemplateView.as_view(template_name="main/home.html"),
        name="home",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
