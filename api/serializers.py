from rest_framework import serializers
from api.models import Film, Actor, Director, ProductionCompany

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ProductionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompany
        fields = '__all__'
