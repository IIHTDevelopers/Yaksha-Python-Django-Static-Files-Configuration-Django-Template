from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command
from django.conf import settings
import logging
from django.contrib.auth import get_user_model


class StaticFilesFunctionalTest(TestCase):
    
    def test_static_file_loading(self):
        test_obj = TestUtils()
        """Test if static files are loaded correctly in production"""
        try:
            # Trigger a request that loads the static files
            response = self.client.get(reverse('home')) 

            # Ensure the correct response status
            self.assertEqual(response.status_code, 200)
            # Ensure that the CSS file is being loaded correctly
            self.assertContains(response, '/static/css/style')  # Ensure CSS file reference is present
            test_obj.yakshaAssert("TestStaticFilesLoading", True, "functional")
            print("TestStaticFilesLoading = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestStaticFilesLoading", False, "functional")
            print(f"TestStaticFilesLoading = Failed")
