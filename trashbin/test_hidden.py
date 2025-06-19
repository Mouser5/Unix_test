import unittest
from hidden import StaticSort

class BaseTestClass(unittest.TestCase):
    sort_method = None

    def setUp(self):
        if self.sort_method is None:
            self.skipTest("Base test class – no sort method defined")
        self.sorter = StaticSort()

    def get_sort_function(self):
        return self.sort_method

    def test_sorted_sort_method(self):
        self.assertEqual(self.get_sort_function()([1, 2, 3]), [1, 2, 3])

    def test_unsorted_sort_method(self):
        self.assertEqual(self.get_sort_function()([3, 2, 1]), [1, 2, 3])

    def test_null_sort_method(self):
        self.assertEqual(self.get_sort_function()([]), [])

    def test_duplicate_sort_method(self):
        self.assertEqual(self.get_sort_function()([3, 2, 1, 3]), [1, 2, 3, 3])

    def test_negative_sort_method(self):
        self.assertEqual(self.get_sort_function()([1, -2, 3]), [-2, 1, 3])

    def test_one_number_sort_method(self):
        self.assertEqual(self.get_sort_function()([1, 1, 1]), [1, 1, 1])

    def test_only_one_sort_method(self):
        self.assertEqual(self.get_sort_function()([1]), [1])

    # def test_not_int_sort_method(self):
    #     self.assertEqual(self.get_sort_function()(['132']),"Error")

    # def test_list_of_string_sort_method(self):
    #     self.assertEqual(self.get_sort_function()(['3','2','1']),"Error")

class TestStaticSortMethod1(BaseTestClass):
    sort_method = StaticSort.sort_method_1

# class TestStaticSortMethod2(BaseTestClass):
#     sort_method = StaticSort.sort_method_2
#
# class TestStaticSortMethod3(BaseTestClass):
#     sort_method = StaticSort.sort_method_3
#
# class TestStaticSortMethod4(BaseTestClass):
#      sort_method = StaticSort.sort_method_4
# #
# class TestStaticSortMethod5(BaseTestClass):
#     sort_method = StaticSort.sort_method_5
#
# class TestStaticSortMethod6(BaseTestClass):
#     sort_method = StaticSort.sort_method_6
#
# class TestStaticSortMethod7(BaseTestClass):
#     sort_method = StaticSort.sort_method_7
#
# class TestStaticSortMethod8(BaseTestClass):
#     sort_method = StaticSort.sort_method_8
