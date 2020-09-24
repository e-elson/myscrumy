from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movegoal/<int:goal_id>', views.move_goal, name='move_goal'),
    path('addgoal', views.add_goal, name='add_goal'),
    path('home', views.home, name='home'),
]
