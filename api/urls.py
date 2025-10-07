from django.urls import path
from .views import (
    FilmListCreateAPIView, FilmDetailAPIView,
    ActorListCreateAPIView, ActorDetailAPIView,
    DirectorListCreateAPIView, DirectorDetailAPIView,
    ProductionCompanyListCreateAPIView, ProductionCompanyDetailAPIView,
)

urlpatterns = [
    path('films/', FilmListCreateAPIView.as_view(), name='film-list'),
    path('films/<int:pk>/', FilmDetailAPIView.as_view(), name='film-detail'),

    path('actors/', ActorListCreateAPIView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),

    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),

    path('production-companies/', ProductionCompanyListCreateAPIView.as_view(), name='pc-list'),
    path('production-companies/<int:pk>/', ProductionCompanyDetailAPIView.as_view(), name='pc-detail'),
]
