from django.contrib import admin
from .models import Character, Feeding, Hobby, Photo

# Register your models here.
admin.site.register(Character)
admin.site.register(Feeding)
admin.site.register(Hobby)
admin.site.register(Photo)
