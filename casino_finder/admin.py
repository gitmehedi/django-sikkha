from django.contrib import admin
from .models import *

# Register your models here.

class CasinoAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(CasinoModel, CasinoAdmin)



