from rest_framework import viewsets

from django.views import generic
from . import models
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = models.Character.objects.all()

class CareerList(generic.ListView):
    queryset = models.Career.objects.all()
    template_name = 'characters/careers/list.html'
