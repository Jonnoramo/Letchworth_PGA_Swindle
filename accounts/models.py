# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

        

class User(AbstractUser):
	

    # Custom attribute added to user class
	
	
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    user_profile_picture = models.ImageField('user_profile_picture', upload_to='static/images/profiles/', null=True, blank=True)
    city = models.CharField(max_length=40, default='')
    handicap = models.CharField(max_length=2, default='')
    objects = AccountUserManager()
    playing = models.CharField(max_length=3, default='')
    membership_id = models.CharField(max_length=40, default='')
    date_joined = models.DateTimeField(default=timezone.now)
