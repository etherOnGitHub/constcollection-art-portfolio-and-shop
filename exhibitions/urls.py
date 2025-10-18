from django.urls import path
from . import views

urlpatterns = [
    path('exhibitions/', views.exhibition_list, name='exhibition_list'),
    path('exhibitions/<int:pk>/', views.exhibition_detail, name='exhibition_detail'),
    path('exhibitions/<int:pk>/edit/', views.edit_exhibition, name='edit_exhibition'),
    path('exhibitions/create/', views.create_exhibition, name='create_exhibition'),
    path('exhibitions/<int:pk>/delete/', views.delete_exhibition, name='delete_exhibition'),
]
