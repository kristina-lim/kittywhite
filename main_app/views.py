from django.shortcuts import render

characters = [
  {
    'name': 'Hello Kitty',
    'species': 'person',
    'description': 'Born in the suburbs of London. She lives with her parents and her twin sister Mimmy who is her bestfriend.',
    'birthday': 'November 1'
  },
  {
    'name': 'Mimmy White',
    'species': 'person',
    'description': 'Born in the suburbs of London. She lives with her parents and her twin sister Kitty who is her bestfriend.',
    'birthday': 'November 1'
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