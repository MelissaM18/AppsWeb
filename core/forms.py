from django import forms

from .models import Team, Stadium, City

# T E A M
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "team_name",
            "players",
            "director",
        ]
        widgets = {
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

#-----------------------------------------------------------------------------------------------------------------#

# S T A D I U M
class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "stadium_name",
            "team",
            "location",
        ]
        widgets = {
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "location": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "stadium_name",
            "team",
            "location",
        ]
        widgets = {
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "location": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

# ------------------------------------------------------------------------------------------------------------------#

# C I T Y
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
            "team",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
            "team",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"})
        }