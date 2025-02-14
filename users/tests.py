from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterAPITestCase(APITestCase):

    def setUp(self):
        self.register_url = "/users/signup/"
        self.valid_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "password": "passw2009"
        }

        self.invalid_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "password": "short"
        }

    def test_register_success(self):
        response = self.client.post(self.register_url, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "You have successfully register")
        self.assertEqual(response.data["data"]["username"], "testuser")

    def test_register_existing_username(self):
        User.objects.create(username="testuser", password="alone12#")
        response = self.client.post(self.register_url, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("A user with that username already exists.", response.data["username"])

