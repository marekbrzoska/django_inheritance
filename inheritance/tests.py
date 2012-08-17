from django.utils import unittest
import models
from django.db.models import fields


class ParrotsUnitTest(unittest.TestCase):
    def test_parrot_since_maybe_dead(self):
        self.assertEqual(
                type(models.ParrotSinceMaybeDead.died), fields.DateField)

    def test_parrot_maybe_dead_since(self):
        self.assertEqual(
                type(models.ParrotMaybeDeadSince.died), fields.BooleanField)

    def test_parrot_dead_for_reason(self):
        self.assertEqual(
                type(models.ParrotDeadForReason.died), fields.TextField)
