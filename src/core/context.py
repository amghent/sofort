from core.models import Setting
from pages.models import Page
from sofort import globals


def get_meta():
    return {
        "application_name": globals.APPLICATION_NAME,
        "application_long_name": globals.APPLICATION_LONG_NAME,
        "authors": "Yves Vindevogel",
        "copyright": globals.COPYRIGHT
    }


def get_navigation_menu():
    return list(Page.objects.filter(show_in_navigation=True))


def get_settings():
    settings_data = Setting.objects.all()
    settings = {}

    for setting in settings_data:
        settings[setting.name] = setting.text

    return settings
