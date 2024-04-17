from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Represents a topic for a flashcard set."""
    title = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the topic."""
        return self.title

class Flashcard(models.Model):
    """Represents a flashcard containing information for learning."""
    front_text = models.CharField(max_length=200)
    back_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """Return a string representation of the flashcard."""
        return self.front_text