from fb.forms import Post_create_form
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

from notifications.signals import notify





def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username,password1)
        if password1 == password2:
            user = User(username=username,password= password2)
            user.save()
            return redirect('signin')
        else:
            print('password not match')
    return render(request,'signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        u = authenticate(username=username,password=password)
        if u is not None:
            login(request,u)
            return redirect('/')
        else:
            print('oppssssssssssssss')
    return render(request,'signin.html')


def logout_user(request):
    logout(request)
    return redirect('signin')



def home(request):
    story = Story.objects.all()
    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.all()
    profiles = Profile.objects.all()
    form = Post_create_form()

    context = {
        'posts':posts,
        'profile':profile,
        'profiles':profiles,
        'comments':comments,
        'story':story,
        'form':form
        }
    return render(request,'home.html',context)


def post_create(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = Post_create_form(request.POST,request.FILES)
        print(request.POST['title'])
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = profile
            new_form.save()
            return redirect('/')
    return render(request,'home.html')


def like(request):
    pk = request.POST['id']
    
    post = Post.objects.get(id=pk)
    like = False
    for l in post.like.all():
        if l == request.user:
            like = True
    if like:
        post.like.remove(request.user)
    if not like:
        post.like.add(request.user)
        if request.user != post.author:
            notify.send(request.user,recipient=post.author.user,verb='has liked your post')
    total_likes = post.like.all().count()
    return JsonResponse({'ok':total_likes})

def notification(request):
    return render(request,'noti.html')

def add_comment(request,pk):
    if request.method == 'POST':
        ct = request.POST['comment_text']
        pi = Post.objects.get(id=pk)
        user = Profile.objects.get(user=request.user)
        
        new_comment = Comment(title=ct,post=pi,author=user)
        new_comment.save()

        return redirect('/')


def user_profile(request,pk):
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(author=profile)
    print(posts)
    form = Post_create_form()
    if request.method == 'POST':
        form = Post_create_form(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = profile
            new_post.save()
            return redirect('/')
    context = {
        'posts':posts,
        'profile':profile,
        'form':form
    }
    return render(request,'profile.html',context)