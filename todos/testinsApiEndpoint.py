
from rest_framework.test import APITestCase, APIRequestFactory
from .views import *

#Testing the view for API endpoint
class ViewTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        #listCreate view
        self.view1 = TodoLists.as_view()
        self.uri = 'task/'

    def test_listCreateView(self):
        resquestToUri = self.factory.get(self.uri)
        responseFromTheEndpoint = self.view1(resquestToUri)
        self.assertEqual(responseFromTheEndpoint.status_code, 200 ,msg= 'Expected code 200, but got {0}'.format(responseFromTheEndpoint.status_code))

   
