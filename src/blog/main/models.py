from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()


class Post(models.Model):
    """
    Represent a post in the blog.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='posts_images')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    A comment for the post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content