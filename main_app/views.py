from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'

class PlayerUpdate(UpdateView):
  model = Player
  # Let's make it impossible to rename a cat :)
  fields = ['breed', 'description', 'age']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players/'

def home(request):
  return render(request, 'home.html')

def game(request):
  players = Player.objects.all()
  return render(request, 'game.html', { 'players' : players })

def players_index(request):
  players = Player.objects.all()
  return render(request, 'players/index.html', { 'players' : players })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  return render(request, 'players/detail.html', { 'player': player })