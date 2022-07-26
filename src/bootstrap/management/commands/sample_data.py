import os
from datetime import datetime

import pandas
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Setting
from interests.models import InterestGroup
from members.models import Member
from pages.models import Page
from questions.models import Question, QuestionAnswer, QuestionReply
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
    def __read_csv(file_name):
        file = os.path.join(os.getcwd(), "src", "bootstrap", "management", "presets", file_name)
        data = pandas.read_csv(file)
        data = data.fillna("")

        rows = []

        for _, r in data.iterrows():
            rows.append(r)

        return rows

    def __upload_settings(self):
        current_year = datetime.now().year
        start_year = 2022
        copyright_year = f"{start_year}"
        
        if current_year > start_year:
            copyright_year += f"-{current_year}"            

        for row in self.__read_csv("settings.csv"):
            s = Setting()
            s.name, s.text = tuple(row)

            if s.name == "copyright":
                s.text = f"© {copyright_year}, {s.text}"

            s.save()

    def __upload_members(self):
        for row in self.__read_csv("members.csv"):
            m = Member()
            m.member_name, m.first_name, m.last_name, m.email = tuple(row)
            m.save()

            u = User()
            u.username, u.first_name, u.last_name, u.email = tuple(row)
            u.set_password(f"{u.username}@SOFORT")
            # Must use set_password to pass unencrypted pwd, not user.password=xyz
            u.save()

    def __upload_tags(self):
        for row in self.__read_csv("tags.csv"):
            t = Tag()
            t.name = tuple(row)
            t.save()

    def __upload_interest_groups(self):
        for row in self.__read_csv("interest_groups.csv"):
            i = InterestGroup()
            i.name, i.slug, i.description, i.about, members = tuple(row)
            i.save()

            if len(members) == 0:
                continue

            for m in members.split(";"):
                i.members.add(self.__get_member(m))

    def __upload_pages(self):
        for row in self.__read_csv("pages.csv"):
            p = Page()
            p.title, p.slug, p.intro, p.content, p.show_in_navigation, p.show_in_footer, p.menu_title, authors = \
                tuple(row)
            p.save()

            for a in authors.split(";"):
                p.authors.add(self.__get_member(a))

    def __upload_questions(self):
        questions = []
        answers = []

        for row in self.__read_csv("questions.csv"):
            qt, qi, qr, author, title, text, interest_group = tuple(row)

            if qt == "q":
                q = Question()
                q.author, q.title, q.text, q.interest_group = self.__get_member(author), title, text, \
                    self.__get_interest_group(interest_group)
                q.save()

                questions.append(q.id)
                continue

            if qt == "a":
                a = QuestionAnswer()
                a.question_id, a.author, a.text = questions[int(qr)], self.__get_member(author), text
                a.save()

                answers.append(a.id)
                continue

            r = QuestionReply()
            r.question_answer_id, r.author, r.text = answers[int(qr)], self.__get_member(author), text
            r.save()

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
