from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Molecule

class MoleculeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ['id', 'LSN', 'sdf']

