from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='index'),
  path('characters/<int:character_id>/', views.characters_detail, name='detail'),
  path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
  path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
  path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
  path('characters/<int:character_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('characters/<int:character_id>/add_photo/', views.add_photo, name='add_photo'),
  path('characters/<int:character_id>/assoc_hobby/<int:hobby_id>/', views.assoc_hobby, name='assoc_hobby'),
  path('characters/<int:character_id>/unassoc_hobby/<int:hobby_id>/', views.unassoc_hobby, name='unassoc_hobby'),
  path('hobbies/', views.HobbyList.as_view(), name='hobbies_index'),
  path('hobbies/<int:pk>/', views.HobbyDetail.as_view(), name='hobbies_detail'),
  path('hobbies/create/', views.HobbyCreate.as_view(), name='hobbies_create'),
  path('hobbies/<int:pk>/update/', views.HobbyUpdate.as_view(), name='hobbies_update'),
  path('hobbies/<int:pk>/delete/', views.HobbyDelete.as_view(), name='hobbies_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]