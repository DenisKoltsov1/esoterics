from django.test import TestCase
from .models import News
from userapp.models import MyUser


class TestViews(TestCase):

    # 1. Страница отвечает
    # 2. На страницу передаются нужные данные
    # 3. На странице есть кнопка search

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_category_list_auth(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)  

        username = 'auth_user'
        password = 'admin123456'
        email = 'auth@user.com'
        user = MyUser.objects.create_user(
            username = 'auth_user',
            email = 'auth@user.com',
            password = 'admin123456',
        )

        self.client.login(username = username, password = password)
        response = self.client.get('/news/news-detail/1')
        self.assertEqual(response.status_code, 301)