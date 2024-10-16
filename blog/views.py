from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

    def get_initial(self):
        """Get initial form data"""
        # Get the result of calling the parent method
        initial_data = super().get_initial()
        # Add the author so it is the requests user
        initial_data["author"] = self.request.user
        # Return the data.
        return initial_data


class BlogUpdateView(UpdateView):
    """Blog Post Delete View"""

    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    """Blog  Post Delete View"""

    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
