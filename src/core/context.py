from django.urls import reverse

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###

def get_meta(**kwargs):
    meta = {}
    
    for k in kwargs:
        meta[k] = kwargs[k]

    return meta

def get_navigation_menu():
    from pages.models import Page

    return list(Page.objects.filter(show_in_navigation=True))


def get_settings():
    from core.models import Setting
    
    settings_data = Setting.objects.all()
    settings = {}

    for setting in settings_data:
        settings[setting.name] = setting.text

    return settings
