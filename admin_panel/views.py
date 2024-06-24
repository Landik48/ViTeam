from django.shortcuts import render,redirect
from django.http import HttpResponse
import os, time
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .writer import excel_pers, excel_team
from django.contrib.auth import login, logout

def admin_aut(request):
    data = {'flag': 'False'}
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username = username)            
        if user.exists():     
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                login(request, user)
                return redirect('main')
            else: 
                data = {'flag': 'True'}
        else: 
            data = {'flag': 'True'}
    return render(request, 'login.html', data)

def admin_panel(request):
    data = {'flag': 'None'}   
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get("logout"):
                logout(request)
                return redirect("login")
            elif request.POST.get("send"):
                lst_load = ['personal', 'team']
                for i in lst_load:
                    uploaded_file = request.FILES[i]
                    save_path = 'xlsx_files/'+os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
                    with open(save_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                            data = {'flag': 'True'}
                    if i == 'personal':
                        excel_pers(save_path)
                    elif i == 'team': 
                        excel_team(save_path)
        return render(request, 'panel.html', data)
    else: 
        return HttpResponse("<h1>Вы не зарегистрированы</h1>")
