from django.db import models


class Posts(models.Model):
    poster = models.CharField(max_length=254, null=False, blank=False)
    post_title = models.CharField(max_length=80, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()


class Comment(models.Model):
    user = models.CharField(max_length=254, null=False, blank=False)
    comment_body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.DecimalField(max_digits=6, decimal_places=0)
