from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *

# Register your models here.

# Data Master
admin.site.register(Agama)
admin.site.register(Bahasa)
admin.site.register(Status_Anak)
admin.site.register(Kelas)
admin.site.register(Pendidikan)
admin.site.register(Penghasilan)

# Data Register
# NB: rule for editing django-admin
@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
  list_display = ("id", "nis", "nama_lengkap", "gender_santri", "wilayah")
  pass

@admin.register(Wilayah)
class WilayahAdmin(ImportExportModelAdmin):
  list_display = ("id", "nama_wilayah")
  pass