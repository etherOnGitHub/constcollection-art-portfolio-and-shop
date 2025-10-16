from django.urls import path, include
from . import views
from .views import HomePage, AboutPage

urlpatterns = [
    path("", HomePage.as_view(template_name="index.html"), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path('summernote/', include('django_summernote.urls')),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:slug>/', views.artwork_detail, name='artwork_detail'),
    path('buy/<int:art_id>/', views.create_checkout_session, name='create_checkout_session'),
]