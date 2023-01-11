from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Character

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
  return render(request, 'characters/detail.html', {
    'character': character
  })

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'