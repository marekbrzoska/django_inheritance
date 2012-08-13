from inheritance import inherit
from django.db import models


class ColouredObject(object):
    colour = models.CharField(max_length=10)
    born = models.DateField()

    @classmethod
    def x(cls):
        return 'x'

    def y(self):
        return 'y'


class LivingObject(object):
    colour = models.CharField(max_length=12)
    born = models.DateTimeField()


class Rabbit(inherit(
    ColouredObject,
    LivingObject)):
    pass


class Parrot(inherit(
    LivingObject,
    ColouredObject,
    colour=models.CharField(max_length=13))):
    pass
