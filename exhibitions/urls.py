from django.urls import path
from . import views

urlpatterns = [
    path('exhibitions/', views.exhibition_list, name='exhibition_list'),
    path('exhibitions/<int:pk>/', views.exhibition_detail, name='exhibition_detail'),
]
