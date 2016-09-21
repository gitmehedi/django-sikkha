from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from . import models

# Create your views here.

def index(request):
    lists = models.Question.objects.order_by()[:5]
    return render(request,'polls/index.html',{'lists':lists})

def details(request,question_id):
    question = get_object_or_404(models.Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def vote(request,question_id):
    p=get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, models.Choice.DoesNotExist):
        return render(request,'polls/details.html',{
            'question':p,
            'error_message': 'You didn\'t select a choice',
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request,question_id):
    question = get_object_or_404(models.Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})


def poll(request):
    return HttpResponse("Hi this is the poll page")
