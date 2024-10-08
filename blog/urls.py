from django.urls import path
from .views import post_list, post_detail #NEW

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),  #NEW
    path("", post_list, name="home"),
]