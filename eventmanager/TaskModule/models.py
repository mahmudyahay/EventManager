from django.db import models
from Account.models import *

# Create your models here.

class TaskTable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
    loction = models.CharField(max_length=50)
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    status_choice = [('Upcoming', 'Upcoming'), ('Canceled', 'Canceled'), ('Completed', 'Completed')]
    status = models.CharField(choices=status_choice, max_length=20, default='Upcoming')