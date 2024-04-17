from django.urls import path
from . import views

app_name = 'studify'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new flashcard
    path('new_flashcard/', views.new_flashcard, name='new_flashcard'),  
    # URL for editing a flashcard
    path('edit_flashcard/<int:flashcard_id>/', views.edit_flashcard, name='edit_flashcard'),
    # URL for deleting a flashcard
    path('delete_flashcard/<int:flashcard_id>/', views.delete_flashcard, name='delete_flashcard'),
]
