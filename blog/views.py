from django.shortcuts import render
from .models import Post


# Create your views here.
def home_view(request):
    return render(request, "blog/home_view.html", {
        "post_content" : Post.objects.all(),
        "title" : "Blogs"
    })

def about_view(request):
    return render(request, "blog/about.html", {
        "message" : "it works",
        "title": "About"
    })