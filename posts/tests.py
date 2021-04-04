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


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image= Image(name = 'musical', caption ='experience', likes ='2')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)



class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comment= Comment(name = 'musical', body ='experience', email ='os@gmail.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))()


    def test_save_method(self):
        self.comment.save_comment()
        comment  = Comment.objects.all()
        self.assertTrue(len(comment)>0)


