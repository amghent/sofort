from django.core.management.base import BaseCommand

from core.models import Setting
from interests.models import InterestGroup


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.__upload_settings()
        self.__upload_interest_groups()

        print("sample data created")

    @staticmethod
    def __upload_settings():
        Setting(name="application_title", text="Welcome at SOFORT").save()

        Setting(name="welcome_text", text="Welcome at Arcelor Mittal's SOFORT. This tool provides a common place to "
                                          "ask your questions about your domain of expertise.").save()
        Setting(name="important_message", text="This tool is under construction ...").save()

    @staticmethod
    def __upload_interest_groups():
        py_group = InterestGroup()

        py_group.name = "AM Python"
        py_group.slug = "python"
        py_group.description = "AM Python group working around data science."
        py_group.welcome = "Welcome to the AM Python Interest Group. " \
                           "This group is all about data science, Jupyter notebooks, Pandas, Numpy, Plotly, ..."

        py_group.save()
