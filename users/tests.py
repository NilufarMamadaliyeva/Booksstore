from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser, Book

class UserRegistrationsTest(TestCase):
    def test_create_user(self):
        response = self.client.post(
            reverse('users:regis'),  
            data={
                'username': 'admin1',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'email': 'email@gmail.com',
                'password': 'shanil'
            }
        )

        self.assertEqual(response.status_code, 200)  

        user = CustomUser.objects.get(username='admin1') 

        self.assertEqual(user.first_name, 'Admin')
        self.assertEqual(user.last_name, 'Adminov')
        self.assertEqual(user.email, 'email@gmail.com')
        self.assertTrue(user.check_password('shanil'))  
        self.assertEqual(user.username, 'admin1')

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:regis'),
            data={
                'first_name': 'Admin',
                'last_name': 'Adminov',
            }
        )

        user_cnt = CustomUser.objects.count()
        self.assertEqual(user_cnt, 0)
        self.assertFormError(response, 'form_name', 'field_name', 'This field is required')  

    def test_email_regis(self):
        response = self.client.post(
            reverse('users:regis'),
            data={
                'username': 'admin13',
                'first_name': 'Admin3',
                'last_name': 'Adminov3',
                'email': 'email@gma-il.com',
                'password': 'shanil'
            }
        )

        user_cnt = CustomUser.objects.count()
        self.assertEqual(user_cnt, 0)
        self.assertFormError(response, 'form_name', 'field_name', 'Enter a valid email address')  


class AuthenticationTests(TestCase):
    def test_user_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword2',
        })
        self.assertEqual(response.status_code, 302)  

    def test_user_login(self):
        User = get_user_model()
        user = User.objects.create_user(username='admin1', password='testpassword')
        response = self.client.post(reverse('login'), {
            'username': 'admin1',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  


class BookTests(TestCase):
    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)  

    def test_book_detail(self):
        book = Book.objects.create(title='Test Book', author='Test Author', content='Book Content')
        response = self.client.get(reverse('book_detail', args=[book.id]))
        self.assertEqual(response.status_code, 200) 


class UserProfileTests(TestCase):
    def test_user_profile_view(self):
        User = get_user_model()
        user = User.objects.create_user(username='admin1', password='testpassword')
        self.client.login(username='admin1', password='testpassword')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200) 
