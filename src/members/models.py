###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
# (except CoreModel which cannot be imported inline because of the inheritance)
###

from core.fields import CoreModel


class Member(CoreModel):
    from core.fields import UniqueCharField, MandatoryCharField, UniqueEmailField, DefaultFieldNow, DefaultFieldTrue
    
    member_name = UniqueCharField(max_length=20)
    first_name = MandatoryCharField(max_length=50)
    last_name = MandatoryCharField(max_length=75)
    email = UniqueEmailField()
    created_at = DefaultFieldNow()
    active = DefaultFieldTrue()

    @property
    def display_name(self):
        return f"{self.last_name.upper()}, {self.first_name} ({self.member_name})"

    @property
    def initials(self):
        return "".join(x[0].upper() for x in f"{self.first_name} {self.last_name}".split())

    def __str__(self):
        return f"{self.last_name.upper()}, {self.first_name} ({self.member_name})"

