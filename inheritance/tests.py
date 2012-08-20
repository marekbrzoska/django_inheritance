from django.test import SimpleTestCase
from django.db.models import fields
from django.forms import ValidationError
import models


class ParrotsUnitTest(SimpleTestCase):
    def test_parrot_since_maybe_dead(self):
        self.assertEqual(
                type(models.ParrotSinceMaybeDead.died), fields.DateField)

    def test_parrot_maybe_dead_since(self):
        self.assertEqual(
                type(models.ParrotMaybeDeadSince.died), fields.BooleanField)

    def test_parrot_dead_for_reason(self):
        self.assertEqual(
                type(models.ParrotDeadForReason.died), fields.TextField)

    def test_parrot_since_maybe_dead_instance_improper_died_field(self):
        with self.assertRaises(ValidationError):
            parrot = models.ParrotSinceMaybeDead.objects.create(died = True) # died is a DateField

    def test_parrot_maybe_dead_since_instance_proper_default_died_field_value(self):
        parrot = models.ParrotMaybeDeadSince.objects.create()
        self.assertEqual(type(parrot.died), type(False))

    def test_parrot_dead_for_reason_instance_proper_default_died_field_value(self):
        parrot = models.ParrotDeadForReason.objects.create()
        self.assertEqual(type(parrot.died), type(''))
