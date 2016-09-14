from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf.urls import url
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .forms import ForumForm, CommentForm, UserForm
from .models import Forum, Comment


# Create your views here.
def index(request):
	all_forums = Forum.objects.all()
	return render(request, 'forum/index.html', {'all_forums': all_forums})

def detail(request, forum_id):
	forum = get_object_or_404(Forum, pk=forum_id)
	form = CommentForm(request.POST or None, request.FILES or None)
	return render(request, 'forum/detail.html', {'forum':forum, 'form':form})

def create_forum(request):
    if not request.user.is_authenticated():
        return render(request, 'forum/login.html', {'error_message': 'You must login or register to make a new forum'})
    else:
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.save()
            return render(request, 'forum/detail.html', {'forum': forum})
        context = {
            "form": form,
            }
    return render(request, 'forum/create_forum.html', context)

def create_comment(request, forum_id):
    if not request.user.is_authenticated():
        return render(request, 'forum/login.html', {'error_message': 'You must login or register to post comments'})
    else:
        form = CommentForm(request.POST or None, request.FILES or None)
        forum = get_object_or_404(Forum, pk=forum_id)
        if form.is_valid():
            forum_comments = forum.comment_set.all()    
            comment = form.save(commit=False)
            comment.forum = forum
            comment.user = request.user
            comment.save()
            return render(request, 'forum/detail.html', {'forum': forum})
        context = {
            'forum': forum,
            'form': form,
        }
    return render(request, 'forum/create_comment.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_forums = Forum.objects.all()
                return render(request, 'forum/index.html', {'all_forums': all_forums})
            else:
                return render(request, 'forum/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'forum/login.html', {'error_message': 'Invalid login'})
    return render(request, 'forum/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'forum/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_forums = Forum.objects.all()
                return render(request, 'forum/index.html', {'all_forums': all_forums})
    context = {
        "form": form,
    }
    return render(request, 'forum/register.html', context)


