from django.test import TestCase, RequestFactory
from restaurant.models import Menu, Booking
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import AnonymousUser

class MenuViewSetTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Matcha Boba Flan", Price=5.99, Inventory=20)
        Menu.objects.create(Title="Mango Pomelo", Price=6.59, Inventory=10)
        self.factory = RequestFactory()

    def test_getall(self):
        request = self.factory.get("menu/items")
        request.user = AnonymousUser()
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.status_code, 200)