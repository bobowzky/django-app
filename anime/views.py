from django.shortcuts import render
from anime.models import Anime
from django.views.generic import DetailView

def index(request):
 animes = Anime.objects.order_by('-hodnoceni')[:3]
 pocet = Anime.objects.all().count()
 context = {
 'animes': animes,
  'pocet': pocet,

 }
 return render(request, 'index.html', context=context)


def animes(request):
 context = {
  'animes': Anime.objects.all(),
 }
 return render(request, 'seznam.html', context=context)


class AnimeDetailView(DetailView):
 model = Anime
 template_name = 'anime/detail.html'
 context_object_name = 'anime'