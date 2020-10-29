from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    is_answered = models.BooleanField(default=False)


class NewPost(models.Model):
    group = models.CharField(max_length=40)
    text = models.TextField()