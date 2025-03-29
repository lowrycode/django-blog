from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Jim',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid_when_name_field_is_empty(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when name field is empty")

    def test_form_is_invalid_when_email_field_is_empty(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Joe',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when email field is empty")

    def test_form_is_invalid_when_message_field_is_empty(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Joe',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when message field is empty")
