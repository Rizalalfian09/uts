# di dalam file views.py di dalam aplikasi penjualan

from rest_framework import generics
from .models import Pelanggan, Produk, Transaksi
from .serializers import PelangganSerializer, ProdukSerializer, TransaksiSerializer

class PelangganList(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class TransaksiList(generics.ListCreateAPIView):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
