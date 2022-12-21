from import_export import resources
from . models import *

class RegisterResource(resources.ModelResource):
  class Meta:
    model = Register