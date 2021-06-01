from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='Let work hard!')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True)
    completed = models.BooleanField(default= False)
