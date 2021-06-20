from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelaporan(models.Model):
    Kecamatan    = models.CharField(max_length=100)
    Alamat_Rinci = models.TextField()
    Gambar       = models.ImageField(default='default.png', blank=True)
    Pelapor    = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.Kecamatan
