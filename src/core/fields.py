import uuid

from django.db import models
from django.utils.timezone import now


###
#   All models must inherit from this model, so they automatically get the ID as UUID
#
class CoreModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class OptionalCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(OptionalCharField, self).__init__(blank=True, null=True, *args, **kwargs)

    class Meta:
        abstract = True


class MandatoryCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(MandatoryCharField, self).__init__(blank=False, null=False, *args, **kwargs)

    class Meta:
        abstract = True


class UniqueCharField(MandatoryCharField):
    def __init__(self, *args, **kwargs):
        if "unique" in kwargs:
            del kwargs["unique"]

        super(UniqueCharField, self).__init__(unique=True, *args, **kwargs)


class MandatoryTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(MandatoryTextField, self).__init__(blank=False, null=False, *args, **kwargs)

    class Meta:
        abstract = True


class OptionalEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(OptionalEmailField, self).__init__(blank=True, null=True, *args, **kwargs)

    class Meta:
        abstract = True


class MandatoryEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(MandatoryEmailField, self).__init__(blank=False, null=False, *args, **kwargs)

    class Meta:
        abstract = True


class UniqueEmailField(MandatoryEmailField):
    def __init__(self, *args, **kwargs):
        if "unique" in kwargs:
            del kwargs["unique"]

        super(UniqueEmailField, self).__init__(unique=True, *args, **kwargs)


class OptionalTimestampField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(OptionalTimestampField, self).__init__(blank=True, null=True, *args, **kwargs)

    class Meta:
        abstract = True


class DefaultFieldNow(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        presets = ["blank", "null", "default"]

        for pre in presets:
            if pre in kwargs:
                del kwargs[pre]

        super(DefaultFieldNow, self).__init__(blank=False, null=False, default=now, *args, **kwargs)

    class Meta:
        abstract = True
