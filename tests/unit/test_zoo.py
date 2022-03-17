from unittest import TestCase

from zoo import Zoo


class TestZoo(TestCase):
    def setUp(self) -> None:
        self.zoo = Zoo()
        self.zoo.create()

    def test_show_all(self):
        expected = "Bowwow~\nMeow~"
        actual = self.zoo.show_all()
        self.assertEqual(expected, actual)
