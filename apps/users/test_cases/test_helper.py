from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'password': self.fake.email(),
            'first_name': self.fake.name(),
            'last_name': self.fake.name(),
            'phone_number': "0200000000",
            'address': "within_accra",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
