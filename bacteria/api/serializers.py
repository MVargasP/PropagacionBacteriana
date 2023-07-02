from rest_framework import serializers
from bacteria.models import BacterialStrain

class BacterialStrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BacterialStrain
        fields = ['id', 'maturation_period', 'life_expectancy', 'reproduction_rate']
