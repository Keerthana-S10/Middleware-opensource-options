from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hotel.views import cust


class TestUrls(SimpleTestCase):

    def test_custLogin_url_is_resolves(self):
        url = reverse('custLogin')
        self.assertEquals(resolve(url).func, custLogin)

   