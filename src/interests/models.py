from core.models import CoreModel, UniqueCharField, MandatoryTextField, MandatoryCharField


class InterestGroup(CoreModel):
    name = UniqueCharField(max_length=30)
    slug = UniqueCharField(max_length=30)
    description = MandatoryCharField(max_length=150)
    welcome = MandatoryTextField()

    def __str__(self):
        return f"{self.name} ({self.slug}) - <{self.id}>"
