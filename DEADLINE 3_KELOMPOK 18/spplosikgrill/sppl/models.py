from django.db import models

# Create your models here.
class karyawan(models.Model):
    id_karyawan = models.AutoField(primary_key=True)
    nama_karyawan_kurir = models.CharField(max_length=50)
    no_hp_karyawan_kurir = models.IntegerField(max_length=30)

    def __str__(self):
        return str (self.nama_karyawan_kurir)

 
class jenis_pengiriman(models.Model):
    id_jenis_pengiriman = models.AutoField(primary_key=True)
    nama_jenis_pengiriman = models.CharField(max_length=50)
    tarif_pengiriman = models.IntegerField(max_length=30)

    def __str__(self):
        return str (self.nama_jenis_pengiriman)
    
class paket(models.Model):
    id_paket = models.AutoField(primary_key=True)
    jenis_paket = models.CharField(max_length=50)
    Jumlah_paket = models.IntegerField(max_length=5)
    harga_paket = models.PositiveIntegerField()

    def __str__(self):
        return str (self.jenis_paket)


class pelanggan(models.Model):
    id_pelanggan = models.AutoField(primary_key=True)
    nama_pelanggan = models.CharField(max_length=50)
    alamat = models.CharField(max_length=250)
    no_hp_pelanggan = models.IntegerField(max_length=30)

    def __str__(self):
        return str (self.nama_pelanggan)
    
class pengiriman(models.Model):
    id_pengiriman = models.AutoField(primary_key=True)
    id_karyawan = models.ForeignKey(karyawan, on_delete=models.CASCADE)
    id_jenis_pengiriman = models.ForeignKey(jenis_pengiriman, on_delete=models.CASCADE)
    tanggal_pengiriman = models.DateField()
    tanggal_pengembalian = models.DateField()

    def __str__(self):
        return "{} - {}".format (self.id_jenis_pengiriman,self.id_karyawan)
    
class pemesanan(models.Model):
    id_pemesanan = models.AutoField(primary_key=True)
    id_karyawan = models.ForeignKey(karyawan, on_delete=models.CASCADE)
    id_pengiriman = models.ForeignKey(pengiriman, on_delete=models.CASCADE)
    id_pelanggan = models.ForeignKey(pelanggan, on_delete=models.CASCADE)
   
    def __str__(self):
        return "{}-{}-{}".format (self.id_karyawan,self.id_pengiriman,self.id_pelanggan)
    
class detail_pemesanan(models.Model):
    id_detail_pemesanan = models.AutoField(primary_key=True)
    id_pemesanan = models.ForeignKey(pemesanan, on_delete=models.CASCADE)
    id_paket = models.ForeignKey(paket, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format (self.id_pemesanan,self.id_paket)
