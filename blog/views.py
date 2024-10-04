from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """Blog List View"""

    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    """Blog Post Detail View"""

    model = Post
    template_name = "post_detail.html"
