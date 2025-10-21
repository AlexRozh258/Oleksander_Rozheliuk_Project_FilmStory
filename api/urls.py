from django.urls import path
from api import views

urlpatterns = [
    path('films/', views.FilmListCreateAPIView.as_view(), name='film-list'),
    path('films/<int:pk>/', views.FilmDetailAPIView.as_view(), name='film-detail'),
]
