from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Ideas(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    goal = models.TextField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    idea = models.ForeignKey(Ideas, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
