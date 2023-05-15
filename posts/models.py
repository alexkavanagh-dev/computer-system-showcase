from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="showcase_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    main_image = CloudinaryField('image', default='placeholder')
    processor = models.CharField(max_length=100)
    cooler = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=100)
    case = models.CharField(max_length=100)
    power_supply = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    additional_parts = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    featured_post = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured_post', '-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by (self.author)"
