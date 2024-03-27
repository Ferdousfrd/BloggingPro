from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author'        : 'CoreyMS',
        'title'         : 'Blog Post 1',
        'content'       : 'First Post Content',
        'date_posted'   : 'March 27, 2024'
    },
    {
        'author'        : 'Jane Doe',
        'title'         : 'Blog Post 2',
        'content'       : 'Second Post Content',
        'date_posted'   : 'March 27, 2024'
    }
]

# Create your views here.
def home_view(request):
    return render(request, "blog/home_view.html", {
        "post_content" : posts,
        "title" : "Blogs"
    })

def about_view(request):
    return render(request, "blog/about.html", {
        "message" : "it works",
        "title": "About"
    })