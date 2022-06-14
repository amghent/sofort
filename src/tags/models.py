from core.fields import CoreModel, UniqueCharField


class Tag(CoreModel):
    name = UniqueCharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
