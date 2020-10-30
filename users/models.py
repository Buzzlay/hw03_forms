from django.db import models
from posts.models import Group


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    is_answered = models.BooleanField(default=False)


class NewPost(models.Model):
    group = models.ForeignKey(Group,
                              related_name="new_group_posts",
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True
                              )
    text = models.TextField()
