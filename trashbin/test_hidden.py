import unittest
from realized import StaticSort

class TestStaticSortMethod1 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([]), [])
    def test_duplicate_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_1(self):
        self.assertEqual(self.sorter.sort_method_1([1]), [1])

class TestStaticSortMethod2 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([]), [])
    def test_duplicate_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_2(self):
        self.assertEqual(self.sorter.sort_method_2([1]), [1])

class TestStaticSortMethod3 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([]), [])
    def test_duplicate_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_3(self):
        self.assertEqual(self.sorter.sort_method_3([1]), [1])

class TestStaticSortMethod4 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([]), [])
    def test_duplicate_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_4(self):
        self.assertEqual(self.sorter.sort_method_4([1]), [1])

class TestStaticSortMethod5 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([]), [])
    def test_duplicate_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_5(self):
        self.assertEqual(self.sorter.sort_method_5([1]), [1])

class TestStaticSortMethod6 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([]), [])
    def test_duplicate_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_6(self):
        self.assertEqual(self.sorter.sort_method_6([1]), [1])

class TestStaticSortMethod7 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([]), [])
    def test_duplicate_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_7(self):
        self.assertEqual(self.sorter.sort_method_7([1]), [1])

class TestStaticSortMethod8 (unittest.TestCase):
    def setUp(self):
        self.sorter = StaticSort()
    def test_sorted_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([1,2,3]),[1,2,3])
    def test_unsorted_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([3, 2, 1]), [1, 2, 3])
    def test_null_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([]), [])
    def test_duplicate_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([3, 2, 1, 3]), [1, 2, 3, 3])
    def test_negative_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([1, -2, 3]), [-2, 1, 3])
    def test_one_number_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([1, 1, 1]), [1, 1, 1])
    def test_only_one_sort_method_8(self):
        self.assertEqual(self.sorter.sort_method_8([1]), [1])

