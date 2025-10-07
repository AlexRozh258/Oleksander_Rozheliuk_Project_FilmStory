from rest_framework import serializers
from .models import Film, Actor, Director, Genre, ProductionCompany


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    release_date = serializers.DateField()
    runtime_minutes = serializers.IntegerField()
    poster_url = serializers.CharField()
    trailer_url = serializers.CharField()
    rating = serializers.FloatField()
    genre = serializers.IntegerField()           
    director = serializers.IntegerField()        
    actor = serializers.IntegerField()           
    production_company = serializers.IntegerField()  


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    bio = serializers.CharField()
    photo_url = serializers.CharField()


class DirectorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    bio = serializers.CharField()
    photo_url = serializers.CharField()


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class ProductionCompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=100)
