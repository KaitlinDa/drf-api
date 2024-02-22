from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Drf_api


class Drf_apiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_drf = Drf_api.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_drf.save()

    def test_drf_model(self):
        drf_api = Drf_api.objects.get(id=1)
        actual_owner = str(drf_api.owner)
        actual_name = str(drf_api.name)
        actual_description = str(drf_api.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_drf_api_list(self):
        url = reverse("drf_api_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf_apis = response.data
        self.assertEqual(len(drf_apis), 1)
        self.assertEqual(response.data[0]["name"], "rake")

    def test_get_drf_api_by_id(self):
        url = reverse("drf_api_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf_api = response.data
        self.assertEqual(drf_api["name"], "rake")

    def test_create_drf_api(self):
        url = reverse("drf_api_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        drf_apis = Drf_api.objects.all()
        self.assertEqual(len(drf_apis), 2)
        self.assertEqual(Drf_api.objects.get(id=2).name, "spoon")

    def test_update_drf_api(self):
        url = reverse("drf_api_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf_api = Drf_api.objects.get(id=1)
        self.assertEqual(drf_api.name, data["name"])
        self.assertEqual(drf_api.owner.id, data["owner"])
        self.assertEqual(drf_api.description, data["description"])

    def test_delete_drf_api(self):
        url = reverse("drf_api_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        drf_apis = Drf_api.objects.all()
        self.assertEqual(len(drf_apis), 0)