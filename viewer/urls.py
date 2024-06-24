from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('models/', admin.site.urls),
    path('', include('main.url')),
    path('', include('admin_panel.url')),
]
