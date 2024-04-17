from django.contrib import admin

# Register your models here.
from .models import Flashcard, Topic
admin.site.register(Flashcard)
admin.site.register(Topic)