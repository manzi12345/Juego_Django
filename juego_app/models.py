from django.db import models

# Create your models here.
# juego_app/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Añade campos adicionales si es necesario

    def __str__(self):
        return self.username




# juego_app/models.py

from django.db import models
from django.conf import settings

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserGame(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - Score: {self.score}"




