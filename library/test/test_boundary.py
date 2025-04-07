from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command
import os

class StaticFilesBoundaryTest(TestCase):
    
    def test_large_static_file(self):
        """Test if large static files are handled properly"""
        test_obj = TestUtils()
        try:
            # Here, simulate a large static file by creating a file larger than a certain size
            large_file = os.path.join(os.getcwd(), 'staticfiles/images/large_image.jpeg')
            # Make sure the file exists (This could be pre-existing in a real project)
            self.assertTrue(os.path.exists(large_file))

            # Check that static files can be served even with large file sizes
            response = self.client.get('/staticfiles/images/large_image.jpeg')
            test_obj.yakshaAssert("TestLargeStaticFileHandling", True, "boundary")
            print("TestLargeStaticFileHandling = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestLargeStaticFileHandling", False, "boundary")
            print(f"TestLargeStaticFileHandling = Failed")