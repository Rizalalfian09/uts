# di dalam file urls.py di dalam aplikasi penjualan

from django.urls import path
from . import views

urlpatterns = [
    path('pelanggan/', views.PelangganList.as_view()),
    path('produk/', views.ProdukList.as_view()),
    path('transaksi/', views.TransaksiList.as_view()),
]
