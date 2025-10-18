from django.urls import path
from . import views

urlpatterns = [
    path('exhibitions/', views.ExhibitionListView.as_view(), name='exhibition_list'),
    path('exhibitions/<int:pk>/', views.ExhibitionDetailView.as_view(), name='exhibition_detail'),
]
