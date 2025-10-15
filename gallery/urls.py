from django.urls import path
from .views import HomePage, AboutPage

urlpatterns = [
    path("", HomePage.as_view(template_name="index.html"), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
]