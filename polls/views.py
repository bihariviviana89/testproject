
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader, RequestContext

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list, })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
