from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.animes, name='anime_list'),
    path('autori/', views.autori, name='autor_list'),
    path('seznam/<int:pk>', views.AnimeDetailView.as_view(), name='anime_detail'),
    path('autori/<int:pk>', views.AutorDetailView.as_view(), name='autor_detail'),
]
