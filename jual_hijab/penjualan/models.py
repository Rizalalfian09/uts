from django.db import models

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Transaksi(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateField()

    def __str__(self):
        return f"Transaksi oleh {self.pelanggan} pada {self.tanggal}"
