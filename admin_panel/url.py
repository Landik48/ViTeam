from django.urls import path
from . import views

urlpatterns =[
    path('loader/', views.admin_aut, name="login"),
    path('loader/main', views.admin_panel, name='main'),
]