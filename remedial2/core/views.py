from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .models import Team, Stadium, Player
from .forms import TeamForm, UpdateTeamForm, StadiumForm, UpdateStadiumForm, PlayerForm, UpdatePlayerForm

# Create your views here.

### T E A M ###
  
# list
class ListTeam(generic.View):
    template_name = "core/team/list_team.html"
    context = {}

    def get(self, request, *args, **kwargs):
        #lleva s
        teams = Team.objects.filter(status=True)
        self.context = {
            "teams": teams
        }
        return render(request, self.template_name, self.context)

# detail
class DetailTeam(generic.View):
    template_name = "core/team/detail_team.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        team = Team.objects.get(pk=pk)
        self.context = {
            "team": team
        }
        return render(request, self.template_name, self.context)
    
# create
class CreateTeam(generic.CreateView):
    template_name = "core/team/create_team.html"
    context = {}
    form_class = TeamForm
    success_url = reverse_lazy("core:list_team")

# update
class UpdateTeam(generic.UpdateView):
    template_name = "core/team/update_team.html"
    model = Team
    form_class = UpdateTeamForm
    success_url = reverse_lazy("core:list_team")

# delete
class DeleteTeam(generic.DeleteView):
    template_name = "core/team/delete_team.html"
    model = Team
    success_url = reverse_lazy("core:list_team")

#-------------------------------------------------------------------------#

### S T A D I U M ###
class ListStadium(generic.View):
    template_name = "core/stadium/list_stadium.html"
    context = {}

    def get(self, request, *args, **kwargs):
        stadiums = Stadium.objects.filter(status=True)
        self.context = {
            "stadiums": stadiums
        }
        return render(request, self.template_name, self.context)
    
# detail
class DetailStadium(generic.View):
    template_name = "core/stadium/detail_stadium.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        stadium = Stadium.objects.get(pk=pk)
        self.context = {
            "stadium": stadium
        }
        return render(request, self.template_name, self.context)
    
# create
class CreateStadium(generic.CreateView):
    template_name = "core/stadium/create_stadium.html"
    context = {}
    form_class = StadiumForm
    success_url = reverse_lazy("core:list_stadium")

# update
class UpdateStadium(generic.UpdateView):
    template_name = "core/stadium/update_stadium.html"
    model = Stadium
    form_class = UpdateStadiumForm
    success_url = reverse_lazy("core:list_stadium")

# delete
class DeleteStadium(generic.DeleteView):
    template_name = "core/stadium/delete_stadium.html"
    model = Stadium
    success_url = reverse_lazy("core:list_stadium")

#-------------------------------------------------------------------------#

### P L A Y E R ###

# list
class ListPlayer(generic.View):
    template_name = "core/player/list_player.html"
    context = {}

    def get(self, request, *args, **kwargs):
        #lleva s
        players = Player.objects.filter(status=True)
        self.context = {
            "players": players
        }
        return render(request, self.template_name, self.context)

# detail
class DetailPlayer(generic.View):
    template_name = "core/player/detail_player.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        player = Player.objects.get(pk=pk)
        self.context = {
            "player": player
        }
        return render(request, self.template_name, self.context)
    
# create
class CreatePlayer(generic.CreateView):
    template_name = "core/player/create_player.html"
    context = {}
    form_class = PlayerForm
    success_url = reverse_lazy("core:list_player")

# update
class UpdatePlayer(generic.UpdateView):
    template_name = "core/player/update_player.html"
    model = Player
    form_class = UpdatePlayerForm
    success_url = reverse_lazy("core:list_player")

# delete
class DeletePlayer(generic.DeleteView):
    template_name = "core/player/delete_player.html"
    model = Player
    success_url = reverse_lazy("core:list_player")