from django.contrib import admin

from .models import Character, Career, Talent

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass



@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    pass
