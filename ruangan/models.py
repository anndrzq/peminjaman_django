from django.db import models
from django.contrib.auth.models import User


class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    stok = models.IntegerField()
    deskripsi = models.TextField(null=True)
    foto = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_barang


class Pinjambarang(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    tgl_mulai = models.DateField()
    tgl_selsai = models.DateField()
    lokasi_barang = models.TextField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.qty
