from django.test import TestCase

# Create your tests here.
class CommentTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 4, username='maureen')

        self.comment= Comment.objects.create(poster= self.user, comment='Pretty baby there' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)