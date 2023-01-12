from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Hobby
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
  id_list = character.hobbies.all().values_list('id')
  hobbies_character_doesnt_have = Hobby.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'characters/detail.html', {
    'character': character,
    'feeding_form': feeding_form,
    'hobbies': hobbies_character_doesnt_have
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

class HobbyList(ListView):
  model = Hobby

class HobbyDetail(DetailView):
  model = Hobby

class HobbyCreate(CreateView):
  model = Hobby
  fields = '__all__'

class HobbyUpdate(UpdateView):
  model = Hobby
  fields = ['name', 'color']

class HobbyDelete(DeleteView):
  model = Hobby
  success_url = '/hobbies'