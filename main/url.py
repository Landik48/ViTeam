from django.urls import path
from . import views

urlpatterns =[
    path('', views.main_page),
    path('score_personals/', views.scores_personal),
    path("score_teams/", views.scores_team),
    path("contests/", views.contests),
]