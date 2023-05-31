from django.test import TestCase

# Create your tests here.
from .models import Video

class VideoModelTestCase(TestCase):
    # this method shoudl be named as setUp
    def setUp(self):
        Video.objects.create(title='This is my title')


    # to run the test method should start with test_
    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
      

    def test_created_count(self):
        qs=Video.objects.all()
        self.assertEqual(qs.count(),1)