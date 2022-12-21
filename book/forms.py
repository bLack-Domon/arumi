from django import forms
from django.forms import ModelForm
from . models import *


class WilayahForm(ModelForm):
    class Meta:
        model = Wilayah
        fields = ('nama_wilayah', 'nama_kepala')

        widgets = {
            'nama_wilayah': forms.TextInput(attrs={
                'required': True,
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Ketikkan Nama Wilayah'
            }),
            'nama_kepala': forms.TextInput(attrs={
                'required': True,
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Ketikkan Nama Kepala'
            })
        }
        labels = {
            "nama_wilayah": "Nama Wilayah",
            "nama_kepala": "Nama Kepala Wilayah",
        }


class AlumniForm(ModelForm):
    class Meta:
        model = Register
        fields = ('tgl_berhenti', 'status_santri')

        widgets = {
            'tgl_berhenti': forms.TextInput(attrs={
                'type': 'date',
                'required':True,
                'class': 'form-control'
                }),
            
            'status_santri': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),
        }




class RegisterForm(ModelForm):
    class Meta:
        model = Register
        # note the extra comma
        fields = '__all__'
        exclude = ('tgl_berhenti',)

        widgets = {
            # biodata santri
            'nis': forms.TextInput(attrs={
                'required': True,
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Ketikkan Nomor Induk Santri'
                }),
            
            'nama_lengkap': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Ketikkan Nama Lengkap',
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),
            
            'nama_panggilan': forms.TextInput(attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nama Panggilan', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),
            
            'gender_santri': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),
            
            'nik': forms.TextInput(attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nomor Induk Keluarga', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'tempat_kelahiran': forms.TextInput(attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan Kota Kelahiran', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),
            
            'tgl_lahir': forms.TextInput(attrs={
                'type': 'date',
                'required':True,
                'class': 'form-control'
                }),
            
            'agama': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),
            
            'anak_ke': forms.TextInput(attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan Urutan Status Diri',
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'saudara_kandung': forms.TextInput(attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan Jumlah Saudara Kandung', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'saudara_tiri': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Jumlah Saudara Tiri', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'saudara_angkat': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Jumlah Saudara Angkat', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'status_anak': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),
            
            'bahasa': forms.Select(attrs={
                'class': 'form-control'
                }),
            
            'tinggi_badan': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Tinggi Badan', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'berat_badan': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Berat Badan', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),
            
            'golongan_darah': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Golongan Darah',
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),

            # Alamat Santri
            'alamat': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Ketikkan Alamat Domisili'
                }),


            # Nama Pondok/Lembaga
            'asal_sekolah': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Asal Sekolah / Pondok'
                }),

            'alamat_sekolah': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Alamat Sekolah / Pondok'
                }),

            'keterangan_sekolah': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),

            'kelas': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),

            'tanggal_mondok': forms.TextInput(attrs={
                'type': 'date', 
                'required':True,
                'class': 'form-control'
                }),

            'masuk_lembaga': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nama Lembaga Formal'
                }),

            'alamat_lembaga': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Alamat Lembaga Formal' 
                }),

            # Identitas Orang Tua
            # Biodata Ayah
            'ayah': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nama Ayah', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),

            'tempat_kelahiran_ayah': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Kota Kelahiran Ayah'
                }),  

            'tgl_lahir_ayah': forms.TextInput(attrs={
                'required':True,
                'type': 'date', 
                'class': 'form-control',
                }),

            'pekerjaan_ayah': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Pekerjaan Ayah', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),  

            'pendidikan_ayah': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),
            
            'penghasilan_ayah': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),
            
            'riwayat_ayah': forms.Select(attrs={
                'required': True,
                'class': 'form-control'
                }),
            
            # Biodata Ibu
            'ibu': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nama Ibu', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),

            'tempat_kelahiran_ibu': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Kota Kelahiran Ibu', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),  

            'tgl_lahir_ibu': forms.TextInput(attrs={
                'required':True,
                'type': 'date', 
                'class': 'form-control'
                }),

            'pekerjaan_ibu': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control', 
                'placeholder': 'Ketikkan Pekerjaan Ibu', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),  

            'pendidikan_ibu': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),
            
            'penghasilan_ibu': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),
            
            'riwayat_ibu': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),

            # Biodata Wali
            'wali': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Nama Wali', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),

            'tempat_kelahiran_wali': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Kota Kelahiran Wali', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),   

            'tgl_lahir_wali': forms.TextInput(attrs={
                'type': 'date', 
                'class': 'form-control'
                }),

            'pekerjaan_wali': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ketikkan Pekerjaan Wali', 
                'onkeypress':"return event.charCode < 48 || event.charCode  >57"
                }),    

            'pendidikan_wali': forms.Select(attrs={
                'class': 'form-control' 
                }),
            
            'penghasilan_wali': forms.Select(attrs={
                'class': 'form-control' 
                }),
            
            'riwayat_wali': forms.Select(attrs={
                'class': 'form-control' 
                }),

            'telp': forms.TextInput(attrs={
                'required':True, 
                'class': 'form-control', 
                'placeholder': 'Ketikkan No. Hp Orang Tua', 
                'onkeypress':"return event.charCode >= 48 && event.charCode <=57"
                }),

            'tgl_berhenti': forms.TextInput(attrs={
                'required':True,
                'type': 'date', 
                'class': 'form-control'
                }),

            'status_santri': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),

            'wilayah': forms.Select(attrs={
                'required': True,
                'class': 'form-control' 
                }),
        }