from core.fields import *


class Setting(CoreModel):
    name = UniqueCharField(max_length=50)
    text = MandatoryTextField()

    def __str__(self):
        return f"{self.name}"
