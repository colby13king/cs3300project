from django.db import models
from django.conf import settings

# Create your models here.

class AppUser(models.Model):
    #List of choices for level of experience
    EXPERIENCE = ( 
    ('Beginner', 'Little/no expereince using Apple Devices'),
    ('Intermedaite', 'Some experience using Apple Devices'),
    ('Experienced', 'Lots of experience using Apple Devices'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    experience = models.CharField(max_length=200, choices=EXPERIENCE, blank = True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("AppUser_detail", args={"pk": self.pk})
    


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Question_detail", args={"pk": self.pk})