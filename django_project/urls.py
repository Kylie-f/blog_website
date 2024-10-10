from django.contrib import admin
from django.urls import path, include #NEW

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), #NEW
    path("accounts/", include("accounts.urls")),
    path("", include("blog.urls")), #NEW
]
