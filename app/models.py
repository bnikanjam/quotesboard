from django.contrib.auth.models import User
from django.db import models


class Quote(models.Model):
    quote_txt = models.TextField()
    quote_img = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=50, default='Anonymous', null=True)
    source = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return f'"{self.quote_txt}" by -{self.author} (posted by {self.user}) '

    class Meta:
        ordering = ['-date_added']
