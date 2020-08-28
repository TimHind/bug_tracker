from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

class Ticket(models.Model):
    NEW = 'new'
    INPROGRESS = 'inprogress'
    COMPLETE = 'complete'
    INVALID = 'invalid'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (INPROGRESS, 'Inprogress'),
        (COMPLETE, 'Complete'),
        (INVALID, 'Invalid'),
    ]
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    filedby = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=80, choices=STATUS_CHOICES, default=NEW)
    assignedto = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='assigned')
    completedby = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='completed')

    def __str__(self):
        return self.title