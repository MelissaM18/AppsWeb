from django.contrib import admin

# Register your models here.

from .models import Team, Stadium, Player

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "venue",
        "team_name",
        "players",
        "director",
    ]

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = [
        "team",
        "city",
        "stadium_name",
        "capacity",
    ]

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "team",
        "player_name",
        "number",
        "position"
    ]