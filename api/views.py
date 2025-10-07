from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Film, Actor, Director, Genre, ProductionCompany
from .serializers import FilmSerializer, ActorSerializer, DirectorSerializer, GenreSerializer, ProductionCompanySerializer


class FilmListCreateAPIView(APIView):
    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetailAPIView(APIView):
    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    def put(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorListCreateAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetailAPIView(APIView):
    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        if Film.objects.filter(actor=actor).exists():
            return Response(
                {"error": "Cannot delete actor. There are films linked to this actor."},
                status=status.HTTP_400_BAD_REQUEST
            )
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DirectorListCreateAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorDetailAPIView(APIView):
    def get(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        if Film.objects.filter(director=director).exists():
            return Response(
                {"error": "Cannot delete director. There are films linked to this director."},
                status=status.HTTP_400_BAD_REQUEST
            )
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreListCreateAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailAPIView(APIView):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductionCompanyListCreateAPIView(APIView):
    def get(self, request):
        companies = ProductionCompany.objects.all()
        serializer = ProductionCompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductionCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductionCompanyDetailAPIView(APIView):
    def get(self, request, pk):
        company = get_object_or_404(ProductionCompany, pk=pk)
        serializer = ProductionCompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = get_object_or_404(ProductionCompany, pk=pk)
        serializer = ProductionCompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_object_or_404(ProductionCompany, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
