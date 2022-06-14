from django.db.models import ManyToManyField

from core.models import CoreModel, UniqueCharField, MandatoryTextField, MandatoryCharField
from members.models import Member


class InterestGroup(CoreModel):
    name = UniqueCharField(max_length=30)
    slug = UniqueCharField(max_length=30)
    description = MandatoryCharField(max_length=150)
    welcome = MandatoryTextField()

    members = ManyToManyField(Member)

    def __str__(self):
        return f"{self.name} ({self.slug})"
