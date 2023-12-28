from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=20, blank=True)
    isi_post = models.EmailField(default='azizah@web.com')

    def __str__(self) :
        return f"{self.judul}"
    
class Daftar(models.Model):
    nama_daftar = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.nama_daftar}"