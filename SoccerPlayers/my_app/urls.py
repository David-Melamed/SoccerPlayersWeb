from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'my_app'

router = routers.DefaultRouter()
router.register('players', views.PlayersView)
router.register('teams', views.TeamsView)
router.register('positions', views.PositionsView)

urlpatterns = [
      path('', views.login_page, name='homepage'),
      path('api/', include(router.urls)),
      path('main/', views.get_team, name='main'),
      path('main/<team_players>/', views.get_all_players, name='all_players')
]
