from django.db import models
from django.contrib.auth import authenticate
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.contrib.auth.models import User

# Create your models here.
status_choices=[
    ('C', 'COMPLETED'),
    ('P', 'PENDING')
]

priority_choices =[
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
]
class TODO(models.Model):
    Title = models.CharField(max_length=50)
    Status = models.CharField(max_length=30, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=priority_choices)