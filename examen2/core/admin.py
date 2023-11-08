from django.contrib import admin

# Register your models here.

from .models import Team, Stadium, City

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "team_name",
        "players",
        "director",
    ]

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = [
        "stadium_name",
        "location",
        "team",
    ]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        "city_name",
        "team",
    ]
