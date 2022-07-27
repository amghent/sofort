###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
# (except CoreModel which cannot be imported inline because of the inheritance)
###

from core.fields import CoreModel


class Tag(CoreModel):
    from core.fields import UniqueCharField
    
    name = UniqueCharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
