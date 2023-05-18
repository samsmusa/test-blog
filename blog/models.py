from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    short_intro = models.CharField(max_length=500, null=True, blank=True)
    star = models.IntegerField(null=False)

    def __str__(self):
        return self.title if self.title else 'no title'
