==================
Django inheritance
==================

---------
W-what???
---------

Django doesn't allow normal python style inheritance. You cannot override fields
in subclasses, you cannot rely on python MRO when inheriting from two classes
that both define field named X. We wanted that, so we created this utility.

-----
Usage
-----

You create you classes but you don't make them inherit from django.db.models.Model.
Consider them *abstract*. You can inherit, mix in, anything you would do in Python.
When you finally want to implement concrete class use the inherit function::
    class SomeConcreteClass(inherit(YourAbstractClassA, YourAbstractClassA)):
        # do staff here if you want. If not just pass
        pass
You can also override some fields from the parent classes. Instead of doing it
in the body of the class you do it in *inherit*'s keyword arguments::
    class OtherConcreteClass(inherit(AbstractClass, id=models.TextField())):
        pass
This will override any id field if *AbstractClass*.


That's it.

You cannot inherit from concrete classes (inheriting from class created by
*inherit* function) the same way. After *inherit*-ing they become django models
and django rules apply.

