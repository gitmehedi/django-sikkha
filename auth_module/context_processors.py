from collections import defaultdict

from . import models

def navigation_menu(request):
    menus = models.NavigationMenu.objects.all()
    # menu_list= defaultdict(dict)
    # menu_id=0
    # for menu in menus:
    #     if menu.level==0 and menu.status:
    #
    #         menu_list[menu_id]['name']= menu.name
    #         menu_list[menu_id]['slug'] = menu.slug
    #         sub_menu_id = 0
    #         for sub_menu in menu.navigationmenu_set.all():
    #
    #             menu_list[menu_id]['submenu'][sub_menu_id]['name'] = 2
    #             menu_list[menu_id]['submenu'][sub_menu_id]['slug'] = 2
    #             sub_menu_id = sub_menu_id + 1
    #         menu_id = menu_id + 1
    #
    # print menu_list

    return {
        'menus': menus
    }