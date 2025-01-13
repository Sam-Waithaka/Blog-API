from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = 'Test title',
            body = 'Test body content'
        )


    def test_post_model(self):
        post = self.post
        self.assertEqual(post.title, 'Test title')
        self.assertEqual(post.body, 'Test body content')
        self.assertEqual(post.author, self.user)
        self.assertEqual(str(post), 'Test title')
        self.assertTrue(post.created_at)
        self.assertTrue(post.updated_at)
        self.assertEqual(post.created_at, post.updated_at)
