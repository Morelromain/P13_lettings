import os
from django.core.wsgi import get_wsgi_application
from django.test import TestCase
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings.local")
application = get_wsgi_application()

from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesTests(TestCase):

    def setUp(self):
        self.true_user = User.objects.create(
            username="user_1")
        self.true_profile = Profile.objects.create(
            favorite_city="city_1", user=self.true_user)
        self.url_index = reverse("profiles:index")
        self.url_profiles = reverse(
            "profiles:profile", args=[self.true_profile.user.username])

    def test_happy_url_index(self):
        response = self.client.get(self.url_index)
        self.assertContains(
            response, "Profiles", status_code=200)

    def test_happy_display_profiles_list(self):
        response = self.client.get(self.url_index)
        self.assertContains(
            response, text="user_1", count=2, status_code=200)

    def test_happy_display_profiles_info(self):
        response = self.client.get(self.url_profiles)
        self.assertContains(
            response, text="city_1", count=1, status_code=200)
