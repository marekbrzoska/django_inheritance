from inheritance import inherit
from django.db import models


class SomeBaseClass(object):
    @classmethod
    def classmethod(cls):
        return 'class method result'

    def method(self):
        return 'method result'


class DeadSince(SomeBaseClass):
    died = models.DateField()


class MaybeStillAlive(SomeBaseClass):
    died = models.BooleanField()


class DeadForYears(SomeBaseClass):
    died = models.IntegerField()


class DeadForYearsParrot(inherit(DeadForYears)):
    pass


class DeadModel(models.Model):
    died = models.URLField()


class ParrotSinceMaybeDead(inherit(
    DeadSince,
    MaybeStillAlive)):
    pass


class ParrotMaybeDeadSince(inherit(
    MaybeStillAlive,
    DeadSince)):
    pass


class ParrotDeadForReason(inherit(
    MaybeStillAlive,
    died=models.TextField())):
    pass
