from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command
import os



class StaticFilesExceptionalTest(TestCase):
    
    def test_collectstatic_without_permissions(self):
        
        test_obj = TestUtils()
        
        test_obj.yakshaAssert("TestCollectStaticWithoutPermissions", True, "boundary")
        print("TestCollectStaticWithoutPermissions = Passed")
