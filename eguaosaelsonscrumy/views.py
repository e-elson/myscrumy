from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import GoalStatus, ScrumyGoals, ScrumyHistory
from django.contrib.auth.models import User

# Create your views here.
random_numbers = []
from random import randint
def get_val():
    val = randint(1000, 9999)
    if val not in random_numbers:
        random_numbers.append(val)
        return val
    else:
        get_val()

def index(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

def move_goal(request,goal_id):
    goal = ScrumyGoals.objects.get(goal_id = goal_id)
    return HttpResponse(goal)

def add_goal(request):
    status = GoalStatus.objects.get(status_name='Weekly Goal')
    user = User.objects.get(username='louis')
    newgoal = ScrumyGoals(goal_name='Keep Learning Django', goal_id=get_val(),
                         created_by='Louis', moved_by='Louis', owner='Louis',
                         goal_status=status, user=user)
    newgoal.save()
    return HttpResponse('New Goal Created')

def home(request):
    eachgoal = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    goal_a = ScrumyGoals.objects.get(goal_name='Learn Django')
    context = {'goal_name': goal_a.goal_name,
               'goal_id': goal_a.goal_id,
               'user': goal_a.user,
               }
    output = ', '.join([e.goal_name for e in eachgoal])
    return render(request, 'eguaosaelsonscrumy/home.html', context)
