from django.db import models
from django.urls import reverse #NEW

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    ) #NEW
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): #NEW
        return reverse("post_detail", kwargs={"pk": self.pk})
