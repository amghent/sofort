from core.fields import CoreModel, UniqueCharField, MandatoryCharField, UniqueEmailField, DefaultFieldNow, \
    DefaultFieldTrue


class Member(CoreModel):
    member_name = UniqueCharField(max_length=20)
    first_name = MandatoryCharField(max_length=50)
    last_name = MandatoryCharField(max_length=75)
    email = UniqueEmailField()
    created_at = DefaultFieldNow()
    active = DefaultFieldTrue()

    def __str__(self):
        return f"{self.last_name.upper()}, {self.first_name} ({self.member_name})"

