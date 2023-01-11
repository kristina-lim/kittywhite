from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from .forms import FeedingForm

# Define the home view
def home(request):
  # Include a .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html', {
    'characters': characters
  })

def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  feeding_form = FeedingForm()
  return render(request, 'characters/detail.html', {
    'character': character,
    'feeding_form': feeding_form
  })

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['birthday', 'breed', 'description']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'