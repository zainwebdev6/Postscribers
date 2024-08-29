from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):   #2
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:   #2
        ordering = ('-date_created',)

    def comment_count(self):  #6
        return self.comment_set.all().count()

    def comments(self):  #6
        return self.comment_set.all()

    def __str__(self):  #2
        return self.title


class Comment(models.Model):  #6
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content