import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Hobby, Photo
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
  fields = ['name', 'gender', 'birthday', 'breed', 'description']

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

def assoc_hobby(request, character_id, hobby_id):
  Character.objects.get(id=character_id).hobbies.add(hobby_id)
  return redirect('detail', character_id=character_id)

def unassoc_hobby(request, character_id, hobby_id):
  Character.objects.get(id=character_id).hobbies.remove(hobby_id)
  return redirect('detail', character_id=character_id)

def add_photo(request, character_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, character_id=character_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', character_id=character_id)