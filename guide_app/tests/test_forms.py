from django.test import TestCase
from .forms import AppUserForm

class AppUserFormTest(TestCase):

    def test_appuser_form_valid(self):
        form_data = {'name': 'John Doe', 'email': 'john@example.com', 'experience': 'Beginner', 'age': 25}
        form = AppUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_appuser_form_invalid(self):
        form_data = {'name': '', 'email': 'not-an-email', 'experience': 'Beginner', 'age': -1}
        form = AppUserForm(data=form_data)
        self.assertFalse(form.is_valid())