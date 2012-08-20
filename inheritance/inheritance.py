from django.db import models


def inherit(*classes, **fixed_fields):
    '''
    Given some classes makes another class just like normal Python would.
    Fields can be overriden, normal python mro applies.
    Moreover some field can be overriden by supplying them as keyword arguments
    - they are highest prioroty - just like they were implemented in inheriting
    class.

    Result of this function is a normal django model, with Fields that cannot be
    overriden in sublasses any more and which names cannot clash in two parent
    classes.
    '''
    ConstructionModel = type('NewModel', classes, {})

    class NewModel(models.Model, ConstructionModel):
        # models.Model allows creation of django model
        # ConstructionModel gives us all methods defined in parent classes
        class Meta:
            abstract = True

    # for every class in hierarchy
    # ordered by python's method resoultion order
    for c in ConstructionModel.mro():
        # inspect all fields of that class
        for field_name, field in c.__dict__.iteritems():
            # to find models.Field instances
            if (
                isinstance(field, models.Field)
                # that are not settled yet
                and not field_name in fixed_fields
                ):
                fixed_fields[field_name] = field
    # when all Fields are extracted settle them for the class
    for k, v in fixed_fields.iteritems():
        setattr(NewModel, k, v)
        NewModel.add_to_class(k, v)
    return NewModel
