# Generated by Django 3.1.1 on 2020-09-25 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('goal_name', models.CharField(max_length=100)),
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(max_length=100)),
                ('moved_by', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eguaosaelsonscrumy.goalstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('moved_from', models.CharField(max_length=100)),
                ('moved_to', models.CharField(max_length=100)),
                ('time_of_action', models.DateTimeField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eguaosaelsonscrumy.scrumygoals')),
            ],
        ),
    ]
