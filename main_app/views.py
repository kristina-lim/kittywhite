from django.shortcuts import render

characters = [
  {
    'name': 'Hello Kitty',
    'gender': 'female',
    'birthday': 'November 1',
    'species': 'Cat',
    'description': 'Born in the suburbs of London. She lives with her parents and her twin sister Mimmy who is her bestfriend.',
  },
  {
    'name': 'Mimmy White',
    'gender': 'female',
    'birthday': 'November 1',
    'species': 'Cat',
    'description': 'Born in the suburbs of London. She lives with her parents and her twin sister Kitty who is her bestfriend.',
  },
]

# Define the home view
def home(request):
  # Include a .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  return render(request, 'characters/index.html', {
    'characters': characters
  })