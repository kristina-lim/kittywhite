from django.contrib import admin
from .models import Character, Feeding, Hobby

# Register your models here.
admin.site.register(Character)
admin.site.register(Feeding)
admin.site.register(Hobby)
