from django import forms
from .models import Topic, Flashcard

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class FlashcardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.all()

    class Meta:
        model = Flashcard
        fields = ['front_text', 'back_text', 'topic']
