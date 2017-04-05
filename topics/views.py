from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateTopicForm

topics = []

def home(request):
    global topics
    return render(request, "topics.html", {'topics': topics})

def create_topic(request):
    global topics
    if request.method == 'POST':
        form = CreateTopicForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            topics.append(form.cleaned_data['topic'])
            return HttpResponseRedirect('/topic/all/')
    else:
        form = CreateTopicForm()
    return render(request, "create_topic.html", { 'topics': topics[0], 'form': form })


