from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Players, Teams
from .serializers import PlayersSerializer, TeamsSerializer



def get_team(request):
    all_teams = Teams.objects.all()
    print(all_teams)
    return render(request, 'all_teams.html', {'teams': all_teams})


def get_all_players(request, team_players):
    all_players = Players.objects.filter(team=team_players).values()
    print(all_players)
    return render(request, 'all_players.html', {'all_players': all_players})


class PlayersView(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TeamsView(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#

