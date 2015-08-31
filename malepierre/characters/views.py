from rest_framework import viewsets

from django.views import generic
from . import models
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = models.Character.objects.all()

class CareerList(generic.ListView):
    queryset = models.Career.objects.all().order_by('code')
    template_name = 'characters/careers/list.html'

class TalentList(generic.ListView):
    queryset = models.Talent.objects.all()
    template_name = 'characters/talents/list.html'

class SkillList(generic.ListView):
    queryset = models.Skill.objects.all()
    template_name = 'characters/skills/list.html'
