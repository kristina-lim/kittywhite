from django.shortcuts import render
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