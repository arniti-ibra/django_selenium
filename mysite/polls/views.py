from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
"""The render() function takes the request object as its first argument, 
a template name as its second argument and a dictionary as its optional third argument."""

from .models import Question, Choice
# Create your views here.

def index(request):
    """Gives a list of the last 5 questions [:5] ordered by publish date (-pub_date)"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list,})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """now draws from a html template"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """updated because our template now has from element. Gets choices via POST, counts your choice as a vote and saves change to the database.
    Then returns HttpResponseRedirect to prevent data being posted twice."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))