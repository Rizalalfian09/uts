from rest_framework import serializers
from .models import Pelanggan, Produk, Transaksi

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'
