from rest_framework import serializers

from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ('creation_date',)