from django.db import models
from django.utils import timezone

class Post(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)
        def __str__(self):
            return self.title

class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        text = models.TextField()
        date = models.DateTimeField()