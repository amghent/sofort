###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###

class Context:
    def __init__(self, **kwargs):
        self.context = {
            "settings": self.__get_settings(),
            "load": {
                "sidebar": True,
                "datatables": True,
                "editor": True
            },
            "meta": self.__get_meta(**kwargs),  # Do not pass as named parameters (kwargs=kwargs)
            "navigation_menu": self.__get_navigation_menu(),
        }

    def get(self):
        return self.context

    @staticmethod
    def __get_meta(**kwargs):
        meta = {}

        for k in kwargs:
            meta[k] = kwargs[k]

        return meta

    @staticmethod
    def __get_navigation_menu():
        from pages.models import Page

        return list(Page.objects.filter(show_in_navigation=True))

    @staticmethod
    def __get_settings():
        from core.models import Setting

        settings_data = Setting.objects.all()
        settings = {}

        for setting in settings_data:
            settings[setting.name] = setting.text

        return settings
