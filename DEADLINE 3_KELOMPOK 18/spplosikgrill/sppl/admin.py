from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.karyawan)
admin.site.register(models.paket)
admin.site.register(models.jenis_pengiriman)
admin.site.register(models.pelanggan)
admin.site.register(models.pengiriman)
admin.site.register(models.pemesanan)
admin.site.register(models.detail_pemesanan)