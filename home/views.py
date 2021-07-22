from django.shortcuts import render , redirect

# Create your views here.

from .form import *
from django.contrib.auth import logout
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import DetailView

from .models import BlogModel,Profile

class ContactListView(ListView):
    paginate_by = 2
    model = BlogModel

class PostDetailView(DetailView):
    model = BlogModel
    blog_obj = BlogModel.objects
    template_name = 'blog_detail.html'

def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    blogs = BlogModel.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(blogs, 3) # Show 25 contacts per page.
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request , 'home.html' ,{ 'users': users })

def login_view(request):
    return render(request , 'login1.html',{"name":"index"})

def blog_detail(request , slug):
    context = {}
    
    
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
        
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)


def see_blog(request):
    context = {}
    
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
        count= len(blog_objs)
        context['count'] = count
        user = request.user
        context['user'] = user
        
        
    except Exception as e: 
        print(e)
    
    
    return render(request , 'see_blog.html' ,context)



def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)


def blog_update(request , slug):
    context = {}
    try:
        
        
        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
        
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'update_blog.html' , context)

def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        print(blog_obj.user)
        
        
        
        if blog_obj.user == request.user:
            print("hola" )
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/see-blog/')


def  register_view(request):
    return render(request , 'login1.html')



def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')


