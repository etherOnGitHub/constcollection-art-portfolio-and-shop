from django.urls import path, include
from . import views
from .views import HomePage, AboutPage, ArtworkListView, ArtworkCreateView, ArtworkDetailView, ArtworkUpdateView, ArtworkDeleteView

urlpatterns = [
    path("", HomePage.as_view(template_name="index.html"), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path('summernote/', include('django_summernote.urls')),
    #public views
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:slug>/', views.artwork_detail, name='artwork_detail'),

    # Superuser CRUD views for frontend
    path('manage/artworks/', ArtworkListView.as_view(), name='artwork_list'),
    path('manage/artworks/add/', ArtworkCreateView.as_view(), name='artwork_create'),
    path('manage/artworks/<int:pk>/', ArtworkDetailView.as_view(), name='artwork_detail_superuser'),
    path('manage/artworks/<int:pk>/edit/', ArtworkUpdateView.as_view(), name='artwork_update'),
    path('manage/artworks/<int:pk>/delete/', ArtworkDeleteView.as_view(), name='artwork_delete'),
]