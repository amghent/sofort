from members.models import Member


class Context:
    @staticmethod
    def get_member_from_username(username: str) -> Member:
        member = None

        if username != "":
            try:
                member = Member.objects.get(member_name=username.strip().lower())
            except Member.DoesNotExist:
                pass

        return member
