from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Flashcard
from .forms import FlashcardForm, TopicForm  # Import the TopicForm


def index(request):
    """The home page for Studify."""
    return render(request, 'studify/index.html')


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.all()  # Fetch all topics
    context = {'topics': topics}
    return render(request, 'studify/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and its associated flashcards."""
    topic = Topic.objects.get(id=topic_id)  # Fetch the topic by ID
    flashcards = Flashcard.objects.filter(topic=topic)  # Fetch associated flashcards
    context = {'topic': topic, 'flashcards': flashcards}
    return render(request, 'studify/topic.html', context)

@login_required
def new_flashcard(request):
    """Add a new flashcard."""
    if request.method == 'POST':
        form = FlashcardForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            form.save()
            return redirect('studify:topics')  # Redirect to topics page after successful submission
    else:
        form = FlashcardForm()  # Create a blank form

    # Fetch all topics to pass to the template for the dropdown menu
    topics = Topic.objects.all()

    # Render the template with the form and topics in the context
    return render(request, 'studify/new_flashcard.html', {'form': form, 'topics': topics})

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method == 'POST':
        form = TopicForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            form.save()
            return redirect('studify:topics')  # Redirect to topics page after successful submission
    else:
        form = TopicForm()  # Create a blank form

    # Render the template with the form
    return render(request, 'studify/new_topic.html', {'form': form})


@login_required
def edit_flashcard(request, flashcard_id):
    """Edit an existing flashcard."""
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)  # Fetch the flashcard by ID
    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)  # Bind form with POST data and instance of flashcard
        if form.is_valid():
            form.save()
            return redirect('studify:topic', topic_id=flashcard.topic.id)  # Redirect to topic page after successful submission
    else:
        form = FlashcardForm(instance=flashcard)  # Populate form with existing flashcard data

    # Render the template with the form
    return render(request, 'studify/edit_flashcard.html', {'form': form, 'flashcard': flashcard})

@login_required
def delete_flashcard(request, flashcard_id):
    """Delete an existing flashcard."""
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)  # Fetch the flashcard by ID
    if request.method == 'POST':
        flashcard.delete()
        return redirect('studify:topic', topic_id=flashcard.topic.id)  # Redirect to topic page after successful deletion

    # Render the confirmation template
    return render(request, 'studify/delete_flashcard.html', {'flashcard': flashcard})