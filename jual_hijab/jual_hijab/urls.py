# di dalam file urls.py di dalam proyek jual_hijab

from django.urls import path, include

urlpatterns = [
    path('api/', include('penjualan.urls')),
]
