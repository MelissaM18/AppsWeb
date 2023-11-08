from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=30, default="Nombre del equipo")
    players = models.CharField(max_length=60, default="No total de jugadores")
    director = models.CharField(max_length=30, default="Director a cargo")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.team_name

class Stadium(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    stadium_name = models.CharField(max_length=50, default="Nombre del estadio")
    location = models.CharField(max_length=50, default="Direccion del estadio")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.stadium_name

class City(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20, default="Nombre de la ciudad")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.city_name
