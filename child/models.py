from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Contact(models.Model):
    """A person we can get in touch with about program(s)"""
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.email)


class Organization(models.Model):
    """Organizations sponsor programs, e.g. Harvard or BU"""
    name = models.CharField(max_length=200, unique=True)
    site = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=12)
    def __str__(self):
        return "{} ({})".format(self.name, self.site)


class Program(models.Model):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()

    age_group = models.CharField(max_length=40)
    topic = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=200)
    location = models.CharField(max_length=50)

    date = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)

    volunteer_app = models.CharField(max_length=50, blank=True)
    volunteer_app_deadline = models.CharField(max_length=50, blank=True)
    volunteer_time = models.CharField(max_length=100, blank=True)

    student_app = models.CharField(max_length=50, blank=True)
    student_app_deadline = models.CharField(max_length=50, blank=True)

    nomination = models.CharField(max_length=50, blank=True)
    nomination_deadline = models.CharField(max_length=50, blank=True)

    cost = models.CharField(max_length=50)

    scholarship_app = models.CharField(max_length=50, blank=True)
    scholarship_app_deadline = models.CharField(max_length=50, blank=True)

    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

    donations_accepted = models.BooleanField()
    donations_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
