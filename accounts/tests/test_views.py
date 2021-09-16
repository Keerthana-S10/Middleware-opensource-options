from  django.test import TestCase, Client
from django.urls import reverse
from hotel.models import cust
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.cust_url = reverse('custLogin')
        self.cust_url = reverse('custRegister')
        

    def test_cust_GET(self):
        response = self.client.get(self.cust_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'custLogin.html')

    def test_item_GET(self):
        response = self.client.get(self.cust_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'custregister.html')