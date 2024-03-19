from http import HTTPStatus
from django.urls import reverse
from django.test import TestCase
from abc import ABC

from user_account.models import User


class BaseViewTestCase(ABC, TestCase):
    path_name = None
    template_name = None
    title = None

    def setUp(self):
            self.path = reverse(self.path_name) if self.path_name is not None else None

    def test_get(self):
        if self.path is not None:
            response = self.client.get(self.path)
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertEqual(response.context['title'], self.title)
            self.assertTemplateUsed(response, self.template_name)


class UserRegistrationViewTestCase(BaseViewTestCase):
    path_name = 'user_account:registration'
    template_name = 'user_account/registration/registration.html'
    title = '| Registration'

    def setUp(self):
        super().setUp()
        self.data = {
            'first_name': 'sauberr', 'last_name': 'Birilko',
            'username': 'sauberr', 'email': 'sauberr10@gmail.com',
            'password1': '123456789pP', 'password2': '123456789pP'
        }

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.', html=True)


class UserLoginViewTestCase(BaseViewTestCase):
    path_name = 'user_account:login'
    template_name = 'user_account/login.html'
    title = '| Login'



