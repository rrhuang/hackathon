# Create your models here.
# #Associate users with a category: instructors and students
# 2. Associate students and instructors with courses
# 3. Keep track of the QR codes an instructor generate (include the time!)
# 4. Keep track of the QR codes student in a class upload (include the time!)

from django.db import models
from django.contrib.auth.models import User
import datetime


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    face_picture = models.ImageField(upload_to='face_pictures/')

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)