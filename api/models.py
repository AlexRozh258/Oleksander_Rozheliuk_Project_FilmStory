from django.db import models

class ProductionCompany(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime_minutes = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    actor = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.SET_NULL, related_name='films')
    director = models.ForeignKey(Director, null=True, blank=True, on_delete=models.SET_NULL, related_name='films')
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL, related_name='films')
    production_company = models.ForeignKey(ProductionCompany, null=True, blank=True, on_delete=models.SET_NULL, related_name='films')

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=255)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
