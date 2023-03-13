from django.shortcuts import render
from .forms import PlayerForm
from .models import Player

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = PlayerForm(request.POST)
    if form.is_valid():
      form.save()
  players = Player.objects.all()
  form = PlayerForm()
  return render(request, "home.html", {"form": form, "players":players})
