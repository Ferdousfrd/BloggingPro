from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
def home_view(request):
    return render(request, "blog/home_view.html", {
        "post_content" : Post.objects.all(),
        "title" : "Blogs"
    })


class PostListView(ListView):
    model = Post
    template_name = 'blog/home_view.html' 
    context_object_name = 'post_content'
    ordering = ['-date_posted']                 #posting is ordered by newest to oldest

class PostDetailView(DetailView):
    model = Post
    


def about_view(request):
    return render(request, "blog/about.html", {
        "message" : "it works",
        "title": "About"
    })