from django.contrib import admin

from .models import Character, Career

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass



@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass
