from django import forms

from .models import Team, Stadium, Player

# T E A M
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "venue",
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "venue": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }
    
class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "venue",
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "venue": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

#-----------------------------------------------------------------------------------------------------------------#

# S T A D I U M
class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "team",
            "stadium_name",
            "city",
            "capacity",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "city": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"number", "class":"form-control"})
        }

class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "team",
            "stadium_name",
            "city",
            "capacity",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "city": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"number", "class":"form-control"})
        }

# ------------------------------------------------------------------------------------------------------------------#

# P L A Y E R
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
            "position",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
            "position": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }

class UpdatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
            "position",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
            "position": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
        }
