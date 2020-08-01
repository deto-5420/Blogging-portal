from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.
from .forms import Postform
from .models import post
from accounts.models import profile
def post_list(request):
    posts=post.objects.all().order_by('id')
    page_obj=Paginator(posts,5)
    Context={
        'post_list': posts,
        'page_obj': page_obj,
    }
    return render(request,"posts/posts_list.html",Context)
class PostListView(ListView):
     model = post
     template_name = 'posts/posts_list.html'  
     
     context_object_name = 'post_list'
     ordering = ['-date_posted']
# we can also use class views 
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin#it is for replacement of decorators for class based views
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']


# class PostDetailView(DetailView):
#     model = Post
    

# #class PostCreateView(LoginRequiredMixin, CreateView):
#      model = Post
#      fields = ['title', 'content'] #<model>_form.html
#  #it has default obejct named object which can iterate instead for creating context list    
#
#      def form_valid(self, form):
#          form.instance.author = self.request.user
#          return super().form_valid(form)
@login_required
def post_detail(request,post_id):
    posts=post.objects.get(id=post_id)
    context={
        'post1':posts
    }
    return render(request,"posts/post_detail.html",context) 

def post_create(request):
    form=Postform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context={
        'form':form,
        'form_type':'create'
      
    }
    return render(request,"posts/post_create.html",context) 
@login_required
def post_update(request,post_id):
    posts=post.objects.get(id=post_id)
    if posts.author == request.user :
            form=Postform(request.POST or None,instance=posts)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/posts')
            context={
              'form':form,
              'form_type':'update'
            }
            return render(request,"posts/post_create.html",context) 
    else:
        messages.success(request,f'only authors can update their posts')
        return HttpResponseRedirect('/posts')

def post_delete(request,post_id):
    posts=post.objects.get(id=post_id)
    if posts.author == request.user :
       posts.delete()
       return HttpResponseRedirect('/posts')
    else:
        messages.success(request,f'only authors can update their posts')
        return HttpResponseRedirect('/posts')