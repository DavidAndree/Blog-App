from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Blog Post"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    body = models.TextField()
    # These 2 dates are special in that they can't be set
    # by user. They are auto-set by the system during
    # creation and updating
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String Method"""
        return self.title

    def get_absolute_url(self):
        """Get absolute url for this instance"""
        return reverse("post_detail", kwargs={"pk": self.pk})
