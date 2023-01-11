from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='index'),
  path('characters/<int:character_id>/', views.characters_detail, name='detail'),
  path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),

]