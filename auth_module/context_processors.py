from . import models

def navigation_menu(request):
    return {
        'menus': models.NavigationMenu.objects.get_active()
    }