from django.test import TestCase

from .models import KnnList
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

class ModelTestCase(TestCase):
    """ This class defines the test suite for the knnList model.  """

    def setUp(self):
        """ Define the test client and other test variables.  """
        self.knnlist_objectName = "Mustang 78"
        self.knnlist = KnnList(objectName=self.knnlist_objectName)

    def test_model_can_create_a_knnList(self):
        """ Test the knnList model can create a knnList.  """
        old_count = KnnList.objects.count()
        self.knnlist.save()
        new_count = KnnList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """ Test suite for the api views.  """

    def setUp(self):
        """ Define the test client and other test variables.  """
        self.client = APIClient()
        self.knnlist_data = {'objectName' : 'Mustang 78', 'firstDetail': 'negro', 'importantDetail': True}
        self.response = self.client.post(
            reverse('create'),
            self.knnlist_data,
            format = "json"
        )

    def test_api_can_create_a_knnlist(self):
        """ Test the api has knn creation capability """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_knnlist(self):
        """ Test the api can get a given knnlist  """
        knnlist = KnnList.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': knnlist.id}, format = "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, knnlist)

    def test_api_can_update_knnlist(self):
        """ Test the api can update a given knnlist. """
        change_knnlist = {'objectName' : 'BochitoSexy'}
        knnlist = KnnList.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': knnlist.id}),
            change_knnlist, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_knnlist(self):
        """ Test the api can delete a knnlist. """
        knnlist = KnnList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': knnlist.id}),
            format = "json",
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
