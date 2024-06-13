from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from home.models import topic, problem
from django.template import loader

# Create your views here

def topics(request):
    topics = topic.objects.all()

    context = {
        'topics':topics,
    }
    #return redirect('/problems/')
    return render(request, 'topics.html', context)


def problems(request, topic_id):
    topics_p = get_object_or_404(topic, id=topic_id)
    problems_t = topics_p.problems.all()
    context = {
        'topics_p':topics_p,
        'problems_t':problems_t,
    }
    #return redirect('/question/')

    return render(request, 'problems.html', context)
