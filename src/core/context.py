###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def get_default_context(**kwargs):
    context = {
        "settings": __get_settings(),
        "load": {
            "sidebar": True,
            "datatables": True,
            "editor": True
        },
        "meta": __get_meta(kwargs=kwargs),
        "navigation_menu": __get_navigation_menu(),
        "layout": __get_layout()
    }
    
    return context
    
    
def __get_meta(**kwargs):
    meta = {}
    
    for k in kwargs:
        meta[k] = kwargs[k]

    return meta


def __get_navigation_menu():
    from pages.models import Page

    return list(Page.objects.filter(show_in_navigation=True))


def __get_settings():
    from core.models import Setting
    
    settings_data = Setting.objects.all()
    settings = {}

    for setting in settings_data:
        settings[setting.name] = setting.text

    return settings

def __get_layout():
    from core.layout import Layout
    
    return Layout()