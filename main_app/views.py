from django.shortcuts import render, redirect
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

def add_feeding(request, character_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.character_id = character_id
    new_feeding.save()
  return redirect('detail', character_id=character_id)

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['birthday', 'breed', 'description']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'