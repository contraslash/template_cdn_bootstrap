import importlib
from operator import and_
from functools import reduce

from django.conf import LazySettings

settings = LazySettings()


def menus(request):
    menu_list = list()
    for app in settings.INSTALLED_APPS:
        app_label = app.split(".")[-1]
        app_menus = get_menu_from_conf_file(app)
        if app_menus is not None:
            for app_menu in app_menus:
                visible_menu_for_user = app_menu.copy()
                visibles_submenus = list()
                permissions = app_menu.get("permissions", list())
                if (
                        (isinstance(permissions, bool) and permissions) or
                        (isinstance(permissions, list) and reduce(and_, (request.user.has_perm(f"{app_label}.{x}") for x in permissions)))
                ) or request.user.is_staff:
                    for submenu in app_menu.get("sub_menus", list()):
                        permissions = submenu.get("permissions", list())
                        if (
                                (isinstance(permissions, bool) and permissions) or
                                (isinstance(permissions, list) and reduce(and_, (request.user.has_perm(f"{app_label}.{x}") for x in permissions)))
                        ) or request.user.is_staff:
                            visibles_submenus.append(submenu)
                    if visibles_submenus:
                        visible_menu_for_user["sub_menus"] = visibles_submenus
                    menu_list.append(visible_menu_for_user)
    return {
        "menus": menu_list
    }


def get_menu_from_conf_file(module_name):
    try:
        conf_module = importlib.import_module(f"{module_name}.conf")
        return conf_module.MENUS
    except (ModuleNotFoundError, AttributeError) as e:
        return
