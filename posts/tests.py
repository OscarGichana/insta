from django.test import TestCase

from .models import Image,Profile,Comment
# # Create your tests here.

7
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(first_name = 'James', last_name ='Muriuki', bio ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)




