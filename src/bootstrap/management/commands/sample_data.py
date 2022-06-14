from django.core.management.base import BaseCommand

from core.models import Setting
from interests.models import InterestGroup
from members.models import Member
from pages.models import Page
from tags.models import Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.__upload_settings()
        self.__upload_members()
        self.__upload_tags()
        self.__upload_interest_groups()
        self.__upload_pages()

        print("sample data created")

    @staticmethod
    def __upload_settings():
        Setting(name="application_title", text="Welcome at SOFORT").save()

        Setting(name="welcome_text", text="Welcome at Arcelor Mittal's SOFORT. This tool provides a common place to "
                                          "ask your questions about your domain of expertise.").save()
        Setting(name="important_message", text="This tool is under construction ...").save()

    @staticmethod
    def __upload_members():
        sidviny = Member()

        sidviny.member_name = "sidviny"
        sidviny.first_name = "Yves"
        sidviny.last_name = "Vindevogel"
        sidviny.email = "yves.vindevogel.external@arcelormittal.com"

        sidviny.save()

    @staticmethod
    def __upload_tags():
        Tag(name="pandas").save()
        Tag(name="numpy").save()
        Tag(name="vsc").save()
        Tag(name="dap").save()
        Tag(name="dex").save()

    def __upload_interest_groups(self):
        py_group = InterestGroup()

        py_group.name = "AM Python"
        py_group.slug = "python"
        py_group.description = "AM Python group working around data science."
        py_group.welcome = "Welcome to the AM Python Interest Group. " \
                           "This group is all about data science, Jupyter notebooks, Pandas, Numpy, Plotly, ..."

        py_group.save()

        py_group.members.add(self.__get_member("sidviny"))

    def __upload_pages(self):
        about = Page()

        about.title = "About SOFORT"
        about.slug = "about"

        about.content = "SOFORT is a tool written in Python and Django"

        about.show_in_navigation = True
        about.show_in_footer = False
        about.menu_title = "About"

        about.save()

        about.authors.add(self.__get_member("sidviny"))

        faq = Page()

        faq.title = "Frequently Asked Questions"
        faq.slug = "faq"

        faq.intro = "Please read these first"
        faq.content = "This is the faq page"

        faq.show_in_navigation = True
        faq.show_in_footer = False
        faq.menu_title = "FAQ"

        faq.save()

        faq.authors.add(self.__get_member("sidviny"))

    @staticmethod
    def __get_member(member_name: str) -> Member:
        member = Member.objects.get(member_name=member_name)
        assert member is not None

        return member
