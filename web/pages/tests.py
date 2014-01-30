from django.test import TestCase
from django.core.urlresolvers import reverse

class TestPages(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
