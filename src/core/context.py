from core.models import Setting
from pages.models import Page


def get_meta(**kwargs):
    meta = {}
    
    for k in kwargs:
        meta[k] = kwargs[k]

    return meta

def get_navigation_menu():
    return list(Page.objects.filter(show_in_navigation=True))


def get_settings():
    settings_data = Setting.objects.all()
    settings = {}

    for setting in settings_data:
        settings[setting.name] = setting.text

    return settings
