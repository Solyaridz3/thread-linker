import email
from email.policy import default
from email.utils import localtime
from statistics import mode
from time import timezone
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, bio, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned staff to True")
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned superuser to True")

        return self.create_user(email, username, first_name, bio, password, **other_fields)

    def create_user(self, email, username, first_name, bio, password, **other_fields):

        if not email:
            raise ValueError("You must provide an email.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, bio=bio,
                           **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200, null=True, verbose_name="Имя")
    username = models.CharField(
        max_length=50, null=True, verbose_name="Никнейм", unique=True)
    email = models.EmailField(null=True, unique=True)
    bio = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(null=True, default="avatar.svg", blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','username','bio']

    def __str__(self):
        return self.username


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
