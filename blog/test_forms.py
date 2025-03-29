from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({"body": "Some content"})
        self.assertTrue(
            comment_form.is_valid(),
            "Form should be valid if body includes string"
        )

    def test_form_is_invalid(self):
        comment_form = CommentForm({"body": ""})
        self.assertFalse(
            comment_form.is_valid(), "Form should be invalid if body is empty"
        )
