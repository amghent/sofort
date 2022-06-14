from django.db.models import ManyToManyField

from core.fields import UniqueCharField, CoreModel, MandatoryTextField, DefaultFieldFalse, OptionalCharField, \
    DefaultFieldNow, OptionalTimestampField
from members.models import Member


class Page(CoreModel):
    title = UniqueCharField(max_length=250)
    slug = UniqueCharField(max_length=50)

    intro = MandatoryTextField()
    content = MandatoryTextField()

    show_in_navigation = DefaultFieldFalse()
    show_in_footer = DefaultFieldFalse()
    menu_title = OptionalCharField(max_length=20)

    authors = ManyToManyField(Member)
    created_at = DefaultFieldNow()
    last_updated_at = OptionalTimestampField()

    def __str__(self):
        return f"{self.title} ({self.slug})"

