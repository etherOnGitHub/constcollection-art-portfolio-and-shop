from django.urls import path
from .views import HomePage

urlpatterns = [
    path("", HomePage.as_view(template_name="index.html"), name="home"),
]