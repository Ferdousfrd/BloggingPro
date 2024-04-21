from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="home_view"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("about/", views.about_view, name="about_view")
]