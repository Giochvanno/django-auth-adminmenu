from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Game name")
    genre = models.CharField(max_length=50)
    description = models.TextField(verbose_name="about game")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)


    def __str__(self):
        return f"{self.name} - {self.author}"
