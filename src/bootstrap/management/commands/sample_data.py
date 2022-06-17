from datetime import datetime
from django.core.management.base import BaseCommand

from core.models import Setting
from interests.models import InterestGroup
from members.models import Member
from pages.models import Page
from questions.models import Question, QuestionAnswer
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
        self.__upload_questions()

        print("sample data created")

    @staticmethod
    def __upload_settings():
        current_year = datetime.now().year
        start_year = 2022
        copyright_year = f"{start_year}"
        
        if current_year > start_year:
            copyright_year += f"-{current_year}"            
        
        Setting(name="application_name", text="SOFORT").save()
        Setting(name="application_long_name", text="SOftware FORum Tool").save()
        Setting(name="application_title", text="Welcome at SOFORT").save()
        Setting(name="authors", text="Yves Vindevogel").save()
        Setting(name="copyright", text=f"© { copyright_year }, Arcelor Mittal Ghent").save()

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
        py_group.about = "Welcome to the AM Python Interest Group. " \
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
        
        under_construction = Page()

        under_construction.title = "Under Construction"
        under_construction.slug = "under_construction"

        under_construction.intro = ""
        under_construction.content = "This tool is still being developed and this page is not yet finished"

        under_construction.show_in_navigation = False
        under_construction.show_in_footer = False

        under_construction.save()

        under_construction.authors.add(self.__get_member("sidviny"))

    def __upload_questions(self):
        q1 = Question()

        q1.author = self.__get_member("sidviny")
        q1.title = "Why is SOFORT written in Python ?"
        q1.text = "I was wondering why SOFORT is written in Python, and Django ?"
        q1.interest_group = self.__get_interest_group("python")

        q1.save()

        a1 = QuestionAnswer()

        a1.question = q1
        a1.author = self.__get_member("sidviny")
        a1.text = "It was written in Python because Python is the best programming language at this moment."

        a1.save()

        a2 = QuestionAnswer()

        a2.question = q1
        a2.author = self.__get_member("sidviny")
        a2.text = "It was written in Python because Python is the best programming language at this moment."

        a2.save()

    @staticmethod
    def __get_member(member_name: str) -> Member:
        member = Member.objects.get(member_name=member_name)
        assert member is not None

        return member

    @staticmethod
    def __get_interest_group(slug: str) -> InterestGroup:
        ig = InterestGroup.objects.get(slug=slug)
        assert ig is not None

        return ig
