from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.user_model = get_user_model()

        self.admin_user = self.user_model(
            email="mauricio.fagundes@gmail.com",
            username="mauricio",
            first_name="Maurício",
            last_name="Fagundes",
            is_admin=True,
        )
        self.admin_user.set_password("1234")
        self.admin_user.save()

        self.non_admin = self.user_model(
            email="user@user.com",
            username="user",
            is_admin=False,
        )
        self.non_admin.set_password("user")
        self.non_admin.save()

    def test_user_creation(self):
        """Test if user is created"""
        self.assertTrue(self.user_model.objects.exists())

    def test_admin_user_login(self):
        credentials = {"email": self.admin_user.email, "password": "1234"}
        # user can login
        response = self.client.login(**credentials)
        self.assertTrue(response)
        # user can access admin
        admin_resp = self.client.post("/admin/", **credentials)
        self.assertEqual(200, admin_resp.status_code)

    def test_non_admin_login(self):
        """Non admin can login but cant access admin"""
        credentials = {"email": self.non_admin.email, "password": "user"}
        # user can login
        response = self.client.login(**credentials)
        self.assertTrue(response)
        # but can't access admin
        admin_resp = self.client.post("/admin", **credentials)
        self.assertEqual(301, admin_resp.status_code)
