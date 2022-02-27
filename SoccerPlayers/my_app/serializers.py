from rest_framework import serializers
from .models import Players, Teams


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['first_name', 'last_name', 'start_date', 'role', 'salary', 'team', 'url']


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['city', 'country', 'start_date', 'League', 'coach_name', 'url']


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['role', 'position']