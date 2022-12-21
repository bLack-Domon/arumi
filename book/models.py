from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

# Database Master to Register_DB

class Agama(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural ="Agama"

class Status_Anak(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural ="Status Anak"

class Bahasa(models.Model):
    language = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural ="Bahasa Sehari-hari"

class Wilayah(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    nama_wilayah = models.CharField(max_length=200, blank=True, null=True)
    nama_kepala = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama_wilayah

    class Meta:
        verbose_name_plural ="Daftar Wilayah PP. Jalaluddin Ar-Rumi"

class Kelas(models.Model):
    tingkat = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tingkat

    class Meta:
        verbose_name_plural ="Jenjang Kelas Pendidikan Santri"

class Pendidikan(models.Model):
    jenjang = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.jenjang

    class Meta:
        verbose_name_plural ="Pendidikan Orang Tua"

class Penghasilan(models.Model):
    bulanan = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.bulanan

    class Meta:
        verbose_name_plural ="Penghasilan Orang Tua"

# EndDatabase Master to Register_DB


# Santri Register
class Register(models.Model):
    JENIS_KELAMIN=(
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    )

    STATUS_SANTRI=(
        ('Aktif', 'Aktif'),
        ('Lulus', 'Lulus'),
    )

    # Biodata Santri
    nis = models.CharField(max_length=200, blank=True, null=True)

    nama_lengkap = models.CharField(max_length=300, blank=True, null=True)

    nama_panggilan = models.CharField(max_length=50, blank=True, null=True)
    
    gender_santri = models.CharField(max_length=200, blank=True, null=True, choices=JENIS_KELAMIN)
    
    nik = models.CharField(max_length=250, blank=True, null=True)
    
    tempat_kelahiran = models.CharField(max_length=100, blank=True, null=True)
    
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    alamat = models.CharField(max_length=350, blank=True, null=True)

    agama = models.ForeignKey("Agama", null=True, on_delete=models.SET_NULL)
    
    anak_ke = models.IntegerField(blank=True, null=True)
    
    saudara_kandung = models.IntegerField(blank=True, null=True)
    
    saudara_tiri = models.IntegerField(blank=True, null=True)
    
    saudara_angkat = models.IntegerField(blank=True, null=True)
    
    status_anak = models.ForeignKey("Status_Anak", null=True, on_delete=models.SET_NULL)
    
    bahasa = models.ForeignKey("Bahasa", blank=True, null=True, on_delete=models.SET_NULL)
    
    tinggi_badan = models.IntegerField(null=True, blank=True)
    
    berat_badan = models.IntegerField(null=True, blank=True)
    
    golongan_darah = models.CharField(max_length=50, blank=True, null=True)

    status_santri = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_SANTRI)

    tgl_berhenti = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    # No Telp Orang Tua
    telp = models.CharField(max_length=200, blank=True, null=True)

    wilayah = models.ForeignKey("Wilayah", null=True, on_delete=models.SET_NULL)

    # Nama Pondok/Lembaga
    PINDAH_PONDOK=(
        ('Lulus', 'Lulus'),
        ('Mutasi', 'Mutasi'),
    )

    asal_sekolah = models.CharField(max_length=250, blank=True, null=True)
    
    alamat_sekolah = models.CharField(max_length=250, blank=True, null=True)
    
    keterangan_sekolah = models.CharField(max_length=50, null=True, blank=True, choices=PINDAH_PONDOK)
    
    tanggal_mondok = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    kelas = models.ForeignKey("Kelas", null=True, on_delete=models.SET_NULL)

    masuk_lembaga = models.CharField(max_length=250, blank=True, null=True)
    
    alamat_lembaga = models.CharField(max_length=250, blank=True, null=True)

    # Identitas Orang Tua
    PENDIDIKAN=(
        ('Tidak Sekolah', 'Tidak Sekolah'),
        ('Putus SD', 'Putus SD'),
        ('SD Sederajat', 'SD Sederajat'),
        ('SMP Sederajat', 'SMP Sederajat'),
        ('SMA Sederajat', 'SMA Sederajat'),
        ('Sarjana', 'Sarjana'),
    )

    PENGHASILAN=(
        ('Kurang dari Rp. 1.000.000', 'Kurang dari Rp. 1.000.000'),
        ('Rp. 1.000.000 - Rp. 2.000.000', 'Rp. 1.000.000 - Rp. 2.000.000'),
        ('Lebih dari Rp. 2.000.000', 'Lebih dari Rp. 2.000.000'),
    )

    RIWAYAT=(
        ('Masih Hidup', 'Masih Hidup'),
        ('Meninggal Dunia', 'Meninggal Dunia'),
    )

    # Biodata Ayah
    ayah = models.CharField(max_length=250, blank=True, null=True)
    
    tempat_kelahiran_ayah = models.CharField(max_length=100, blank=True, null=True)
    
    tgl_lahir_ayah = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    pekerjaan_ayah = models.CharField(max_length=250, blank=True, null=True)
    # pendidikan_ayah = models.ForeignKey("Pendidikan", related_name="jenjang", null=True, on_delete=models.SET_NULL)
    pendidikan_ayah = models.CharField(max_length=200, blank=True, null=True, choices=PENDIDIKAN)
    # penghasilan_ayah = models.ForeignKey("Penghasilan", null=True, on_delete=models.SET_NULL)
    penghasilan_ayah = models.CharField(max_length=200, blank=True, null=True, choices=PENGHASILAN)
    
    riwayat_ayah = models.CharField(max_length=200, blank=True, null=True, choices=RIWAYAT)

    # Biodata Ibu
    ibu = models.CharField(max_length=250, blank=True, null=True)
    
    tempat_kelahiran_ibu = models.CharField(max_length=100, blank=True, null=True)
    
    tgl_lahir_ibu = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    pekerjaan_ibu = models.CharField(max_length=250, blank=True, null=True)
    # pendidikan_ibu = models.ForeignKey("Pendidikan", related_name="jenjang", null=True, on_delete=models.SET_NULL)
    pendidikan_ibu = models.CharField(max_length=200, blank=True, null=True, choices=PENDIDIKAN)
    # penghasilan_ibu = models.ForeignKey("Penghasilan", null=True, on_delete=models.SET_NULL)
    penghasilan_ibu = models.CharField(max_length=200, blank=True, null=True, choices=PENGHASILAN)
    
    riwayat_ibu = models.CharField(max_length=200, blank=True, null=True, choices=RIWAYAT)
    
    # Wali Santri
    wali = models.CharField(max_length=250, blank=True, null=True)
    
    tempat_kelahiran_wali = models.CharField(max_length=100, blank=True, null=True)
    
    tgl_lahir_wali = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    pekerjaan_wali = models.CharField(max_length=250, blank=True, null=True)
    # pendidikan_wali = models.ForeignKey("Pendidikan", related_name="jenjang", null=True, on_delete=models.SET_NULL)
    pendidikan_wali = models.CharField(max_length=200, blank=True, null=True, choices=PENDIDIKAN)
    # penghasilan_wali = models.ForeignKey("Penghasilan", null=True, on_delete=models.SET_NULL)
    penghasilan_wali = models.CharField(max_length=200, blank=True, null=True, choices=PENGHASILAN)
    
    riwayat_wali = models.CharField(max_length=200, blank=True, null=True, choices=RIWAYAT)

    profile_pic = models.ImageField(default='tanpa.png', blank=True)

    def save(self):
        super().save()
        
        img = Image.open(self.profile_pic.path)

        if img.height > 471 or img.width > 701:
            new_img = (471,701)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)

    def __str__(self):
        if self.nama_lengkap is not None:
            return self.nama_lengkap
        return "Data Kosong"
    
    class Meta:
        verbose_name_plural ="Data Santri"

# EndSantri Register
