from django.contrib import admin

from .models import Character, Career, Talent, Skill, SkillSet, TalentSet

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ('name', )

@admin.register(SkillSet)
class SkillSetAdmin(admin.ModelAdmin):
    search_fields = (
        'skill0__name',
        'skill1__name',
    )

@admin.register(TalentSet)
class TalentSetAdmin(admin.ModelAdmin):
    search_fields = (
        'talent0__name', 
        'talent1__name',
    )

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    pass
