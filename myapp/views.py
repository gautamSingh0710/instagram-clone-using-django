from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import JsonResponse,Http404
from .models import Post
from .forms import PostForm
from django.conf import settings
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'myapp/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'myapp/login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.all()
    return render(request, 'myapp/dashboard.html', {'posts': posts})

def message(request):
    return render(request,"myapp/message.html")
def profile(request):
    return render(request,"myapp/profile.html")
def search(request):
    return render(request,"myapp/search.html")
def music(request):
    return render(request,"myapp/music.html", {
        'MEDIA_URL': settings.MEDIA_URL})
def reels(request):
    return render(request, "myapp/reels.html", {
        'MEDIA_URL': settings.MEDIA_URL})
# def create_post(request):
#     return render(request,"myapp/create_post.html")

def logout_view(request):
    logout(request)
    return redirect('login')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'likes_count': post.likes.count(), 'liked': liked})
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Set the current user as the post's user
            post.save()
            return redirect('dashboard')  # Redirect to dashboard after post creation
        else:
            print("Form is invalid", form.errors)
    else:
        form = PostForm()

    return render(request, 'myapp/create_post.html', {'form': form})
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        if post.image:
            post.image.delete()  # Image file ko media se delete karo
        post.delete()            # Pura post (caption + record) database se delete
        return redirect('dashboard')  # Ya koi bhi page jahan redirect karna hai

    return redirect('dashboard')

