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
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50,default='SOME STRING')
    last_name = models.CharField(max_length = 50,default='SOME STRING')
    email = models.CharField(max_length=100, default='SOME STRING')
    face_picture = models.ImageField(upload_to='face_pictures/')

class Transaction(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_transactions', on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserProfile, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

import logging
def addUser(first, last, email,face_picture):
    '''addUser creates a new user and saves it to the database, either as a Student or Instructor.
    It does following checks:
    - Checks to see no other instructor with the same email exists
    - Saves the new record
    - Creates a log message
    '''

    #log message
    logging.info('Trying to add a new user ' + str((first, last, email, face_picture)))

    
   
    #Check to see no other student exists with the same email.
    if UserProfile.objects.filter(email=email).count() > 0:
        raise ValueError('Another user with email ' + email + ' exists')
    #Actually create the student
    new_user = UserProfile(first_name = first, last_name = last, email = email, face_picture = face_picture)
    new_user.save()

    #Add finish log entry
    logging.info('Added a new user ' + str((first, last, email)))
    
    