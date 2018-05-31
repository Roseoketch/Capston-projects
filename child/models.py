from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class organization(models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    description =  models.TextField()
    category = models.ManyToManyField(categories)
    email = models.EmailField()
    time_uploaded = models.DateTimeField(auto_now_add=True,null=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='profile/',blank=True,null=True)


    def __str__(self):
        return self.name

    def save_organization(self):
        self.save()

    def delete_organization(self):
        self.delete()

    @classmethod
    def search_organization(cls,search_term):
        organization = cls.objects.filter(name__icontains=search_term)
        return organization
