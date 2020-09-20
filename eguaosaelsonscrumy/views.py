from django.shortcuts import render
from django.http import HttpResponse
from .models import GoalStatus, ScrumyGoals, ScrumyHistory

# Create your views here.

def index(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)
