from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(Title="Matcha Boba Flan", Price=5.99, Inventory=20)
        self.assertEqual(item.Title, "Matcha Boba Flan")
        self.assertEqual(item.Price, 5.99)
        self.assertEqual(item.Inventory, 20)