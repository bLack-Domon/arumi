import django_filters
from . models import *


class DataFilter(django_filters.FilterSet):
  class Meta:
    model = Register
    fields = ('nis', 'nama_lengkap', 'gender_santri', 'tempat_kelahiran', 'wilayah')