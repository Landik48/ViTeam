from django.shortcuts import render
from .models import Users, Teams, Contests

def main_page(request): 
    return render(request, 'home.html')
    
def scores_personal(request):
    users_all = Users.objects.values()
    score = {}
    for i in users_all:
        key = i["name"] + " (" + str(i["team"]) + " Отряд)"
        score[key] = i["scores_personal"]
    sorted_dict = dict(sorted(score.items(), key=lambda item: item[1], reverse=True))
    return render(request, "rating_personal.html", 
    {"scores": sorted_dict})
        
def scores_team(request):
    teams_all = Teams.objects.values()
    score = {}
    for i in teams_all:
        key = str(i["team"]) + " Отряд"
        score[key] = i["scores_team"]
    sorted_dict = dict(sorted(score.items(), key=lambda item: item[1], reverse=True))
    return render(request, "rating_team.html", 
    {"scores": sorted_dict})
    
    
def contests(request):
    contests_all = Contests.objects.values()
    scores = {}
    for i in contests_all:
        scores[i["contest"]] = [i["description"], i['data']]
    return render(request, "conkurs.html", {"scores": scores})