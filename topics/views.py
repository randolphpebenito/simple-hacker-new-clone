from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateTopicForm
from .topics import Topic

#Global Variable topics
topics = []

def paginate_list(list_obj, page_req_var):
    paginator = Paginator(list_obj, 3)
    try:
        pl = paginator.page(page_req_var)
    except PageNotAnInteger:
        pl = paginator.page(1)
    except EmptyPage:
        pl = paginator.page(paginator.num_pages)
    return pl

def home(request):
    global topics
    sorted_items = sorted(topics, key=lambda o: o.total_vote_count)
    topic_list = paginate_list(sorted_items, request.GET.get('page'))
    return render(request, "topics.html", {'topics': topic_list})

def create_topic(request):
    global topics
    if request.method == 'POST':
        form = CreateTopicForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            t = Topic(topic=form.cleaned_data['topic'])
            topics.append(t)
            return HttpResponseRedirect('/topic/all/')
    else:
        form = CreateTopicForm()
    return render(request, "create_topic.html", {'form': form })

