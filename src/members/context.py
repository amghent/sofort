from django.contrib.auth.models import User

from members.models import Member


class Context:
    @staticmethod
    def get_member_from_username(user: User) -> Member:
        member = None

        print(user)
        if user is not None:
            try:
                member = Member.objects.get(member_name=user.username.strip().lower())
            except Member.DoesNotExist:
                pass

        return member
