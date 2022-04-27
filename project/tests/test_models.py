from django.test import TestCase

class URLTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("hfffh")
        pass

    def test_abaout_page_status_code(self):
        response = self.client.get('index')
        self.assertEquals(response.status_code, 404)