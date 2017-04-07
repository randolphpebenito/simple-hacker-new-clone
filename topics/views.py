#Django Built-In
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

#In-App
from .forms import CreateTopicForm
from .topics import Topic, TopicList

#Global Variable topics
#TODO: Classify TopicList
topics = TopicList()

def paginate_list(list_obj, page_req_var):
    """
        Pagination config
    """
    paginator = Paginator(list_obj, settings.ITEM_LIMIT_PER_PAGE)
    try:
        pl = paginator.page(page_req_var)
    except PageNotAnInteger:
        pl = paginator.page(1)
    except EmptyPage:
        pl = paginator.page(paginator.num_pages)
    return pl

def home(request):
    """
        List all topics sorted by total_vote_score descending (w/ pagination)
    """
    global topics
    sorted_items = topics.sort_by('total_vote_score', reverse=True)
    topic_list = paginate_list(sorted_items, request.GET.get('page'))
    return render(request, "topics.html", {'topics': topic_list})

def create_topic(request):
    """
        Creating a topic via form
    """
    global topics
    if request.method == 'POST':
        form = CreateTopicForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            t = Topic(topic=form.cleaned_data['topic'])
            topics.append(t)
            return redirect('topic:home')
    else:
        form = CreateTopicForm()
    return render(request, "create_topic.html", {'form': form })

def upvote_topic(request, topic_id):
    """
        Upvoting a topic based on topic_id
        returns total_vote_score if topic_id exists
        otherwise 404
    """
    topic_obj = topics.get_obj_by_attr_or_none('topic_id', topic_id)
    if topic_obj is not None:
        topic_obj.upvote(1)
        return HttpResponse(topic_obj.total_vote_score)
    else:
        raise Http404("Topic does not exist")

def downvote_topic(request, topic_id):
    """
        Downvoting a topic based on topic_id
        returns total_vote_score if topic_id exists
        otherwise 404
    """
    topic_obj = topics.get_obj_by_attr_or_none('topic_id', topic_id)
    if topic_obj is not None:
        topic_obj.downvote(1)
        return HttpResponse(topic_obj.total_vote_score)
    else:
        raise Http404("Topic does not exist")
