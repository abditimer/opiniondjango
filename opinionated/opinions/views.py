from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import logging
logging.basicConfig(level=logging.INFO)

from .models import Opinion

def index(request):
    logging.info('home page requested.')
    latest_question_list = Opinion.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'opinions/index.html', context)

def agree(request, question_id):
    return HttpResponse(f'You have <b>agreed</b> with the opinion: {question_id}')

def disagree(request, question_id):
    return HttpResponse(f'You have <b>disagreed</b> with the opinion: {question_id}')

def vote(request, question_id):
    logging.info('vote view entered.')
    opinion = get_object_or_404(Opinion, pk=question_id)
    try:
        selected_choice = opinion.objects.get(pk=request.POST['vote'])
        logging.info(f'Question sent to vote view -> {opinion.question_text}')
    except (KeyError, Opinion.DoesNotExist):
        return HttpResponse(f'You have an error: {opinion}')
    else:
        selected_choice.score_int += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('opinions:results', args=(opinion.id,))) 

def results(request, question_id):
    opinion = get_object_or_404(Opinion, pk=question_id)
    return render(request, 'opinions/results.html', {'opinion': opinion})