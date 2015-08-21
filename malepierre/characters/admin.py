from django.contrib import admin

from .models import Character

@admin.register(Character)
class UserAdmin(admin.ModelAdmin):
    pass
