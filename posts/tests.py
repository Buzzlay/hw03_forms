from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Post

User = get_user_model()


class StaticURLTests(TestCase):
    # Метод класса должен быть декорирован

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='DimaBuslaev')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)
        cls.unauthorized_client = Client()

    def test_homepage(self):
        response = StaticURLTests.unauthorized_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_force_login(self):
        user = User.objects.create_user(username='Natalia')
        StaticURLTests.unauthorized_client.force_login(user)
        response = StaticURLTests.unauthorized_client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_new_post(self):
        current_posts_count = Post.objects.count()
        response = StaticURLTests.authorized_client.post(
            '/new/',
            {'text': 'Это текст публикации'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), current_posts_count + 1)

    def test_unauthorized_user_newpage(self):
        response = StaticURLTests.unauthorized_client.get('/new/', follow=False)
        self.assertRedirects(
            response,
            '/auth/login/?next=/new/',
            status_code=302,
            target_status_code=200
        )
