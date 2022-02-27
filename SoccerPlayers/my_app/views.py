from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Players, Teams, Positions
from .serializers import PlayersSerializer, TeamsSerializer


def login_page(request):
    form = AuthenticationForm()
    return render(request, 'main.html', {"form": form})


def get_team(request):
    all_teams = Teams.objects.all()
    return render(request, 'all_teams.html', {'teams': all_teams})


def get_all_players(request, team_players):
    all_players = Players.objects.filter(team=team_players).values()
    return render(request, 'all_players.html', {'all_players': all_players})


class PlayersView(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TeamsView(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PositionsView(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
