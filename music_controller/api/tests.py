from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Room



class CreateRoomTest(APITestCase):
    def test_create_room(self):
        """
        Ensure we can create a new account object.
        """
        data = {'guest_can_pause': True, 'votes_to_skip': 2}
        response = self.client.post('/api/create-room', data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().guest_can_pause, True)


# Create your tests here.
