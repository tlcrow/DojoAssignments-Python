from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
A_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['first_name']) < 2:
            error['f_name'] = "First name should be more than 2 characters"
        if not A_REGEX.match(postData['first_name']):
            error['first_name'] = "First name should only contain letters"
        if len(postData['last_name']) < 2:
            error['l_name'] = "Last name should be more than 2 characters"
        if not A_REGEX.match(postData['last_name']):
            error['last_name'] = "Last name should only contain letters"
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = "Email must be valid"
        if len(postData['password']) < 8:
            error['password'] = "Password must be more than 8 characters"
        if postData['password'] != postData['confirm_password']:
            error['password'] = "Password and confirm password must match"
        return error
    def login_validator(self, postData):
        error = {}
        if not User.objects.filter(email = postData['email']):
            error['loginemail'] = "Incorrect Email"
        if not bcrypt.checkpw(postData['password'].encode('utf8'), User.objects.get(email=postData['email']).password.encode('utf8')):
            error['loginpassword'] = "Incorrect Password"
        return error

class User(models.Model):       
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

