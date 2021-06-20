from django.db import models

# Create your models here.

class Deskripsi(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField()
    body    = models.TextField()

    def __str__(self):
        return self.title

class Peta(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField()
    body    = models.TextField()
    thumb   = models.ImageField(default='default.png', blank=True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."
#thumbnail
