import os
from django.core.wsgi import get_wsgi_application
from django.test import TestCase
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings.local")
application = get_wsgi_application()

from lettings.models import Letting, Address




class LettingsTests(TestCase):

    def setUp(self):
        self.true_adress = Address.objects.create(
            number=1, street="street_adress", city="test",
            state="test", zip_code=11111, country_iso_code="FR")
        self.true_letting = Letting.objects.create(
            title="title_letting", address=self.true_adress)
        self.url_index = reverse("lettings:index")
        self.url_lettings = reverse("lettings:letting", args=[self.true_letting.id])

    def test_happy_url_index(self):
        response = self.client.get(self.url_index)
        self.assertContains(
            response, "Lettings", status_code=200)

    def test_happy_display_lettings_list(self):
        response = self.client.get(self.url_index)
        self.assertContains(
            response, text="title_letting", count=1, status_code=200)

    def test_happy_display_lettings_info(self):
        response = self.client.get(self.url_lettings)
        self.assertContains(
            response, text="street_adress", count=1, status_code=200)
