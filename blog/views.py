from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class BlogListView(ListView):
    """Blog List View"""

    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    """Blog Post Detail View"""

    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    """Blog Post Create View"""

    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
