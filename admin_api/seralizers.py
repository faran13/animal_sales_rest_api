from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import animal

class animalSeralizer(serializers.ModelSerializer):
    class Meta:
        model = animal
        fields = '__all__'
         
