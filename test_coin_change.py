import unittest
from coin_change import Change


class TestReturnValue(unittest.TestCase):
    def setUp(self) -> None:
        self.__find_change = Change

    def tearDown(self) -> None:
        del self.__find_change

    def return_min_sum_of_3(self):
        self.assertEqual(
            3, self.__find_change.find_min_change(20, [1, 2, 3, 4, 5]))

    def return_min_sum_of_52030(self):
        self.assertEqual(52030, self.__find_change.find_min_change(
            1040528, [1, 5, 10, 20]))


if __name__ == "__main__":
    unittest.main()
