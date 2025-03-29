from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestBlogViews(TestCase):

    def setUp(self):
        self.about = About(title="Joe Bloggs", content="Sample content")
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Sample content", response.content)
        self.assertIsInstance(
            response.context["collaborate_form"], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for posting a collaboration request"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            "name": "Joe",
            "email": "test@test.com",
            "message": "My message",
        }
        response = self.client.post(reverse("about"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! "
            b"I endeavour to respond within 2 working days.",
            response.content,
        )
