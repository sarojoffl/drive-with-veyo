from django.db import models
from django.contrib.auth.models import AbstractUser

class Job(models.Model):
    JOB_TYPES = [
        ('Remote', 'Remote'),
        ('Full-time', 'Full-time'),
        ('On-site', 'On-site'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPES)
    description = models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(default="This is a default blog content.")
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Admin")  # Optional: customize per blog

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    referral_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
