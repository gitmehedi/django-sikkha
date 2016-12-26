from django.contrib import admin
from auth_module.models import *


class NavigationMenuAdmin(admin.ModelAdmin):
    fields = ['name','slug','level','parent','status']

admin.site.register(NavigationMenu, NavigationMenuAdmin)
