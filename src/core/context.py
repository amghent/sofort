###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


class Context:
    def __init__(self, request, **kwargs) -> None:
        from members.context import Context as MemberContext

        user = request.user
        member = None

        if user is not None:
            member = MemberContext().get_member_from_username(user=user)

        self.context = {
            "user": user,
            "member": member,
            "settings": self.__get_settings(),
            "meta": self.__get_meta(**kwargs),  # Do not pass as named parameters (kwargs=kwargs)
            "navigation_menu": self.__get_navigation_menu(),
        }

    def get(self) -> dict:
        return self.context

    @staticmethod
    def __get_meta(**kwargs):
        meta = {}

        for k in kwargs:
            meta[k] = kwargs[k]

        return meta

    @staticmethod
    def __get_navigation_menu() -> list:
        from pages.models import Page

        return list(Page.objects.filter(show_in_navigation=True))

    @staticmethod
    def __get_settings() -> dict:
        from core.models import Setting

        settings_data = Setting.objects.all()
        settings = {}

        for setting in settings_data:
            settings[setting.name] = setting.text

        return settings
