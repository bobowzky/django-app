from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.animes, name='anime_list'),
    path('seznam/<int:pk>', views.AnimeDetailView.as_view(), name='anime_detail'),
]
