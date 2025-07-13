from django.db import models
from django.utils import timezone

# ----------------------
# Project Model
# ----------------------
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name

# ----------------------
# Client Model
# ----------------------
class Client(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

# ----------------------
# Contact Form Submission Model
# ----------------------
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.full_name} - {self.email}"

# ----------------------
# Newsletter Subscriber Model
# ----------------------
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)  
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.email
