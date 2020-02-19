from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField(max_length=100)
    project_url = 
    posted_on = models.DateTimeField(auto_now_add=True)
