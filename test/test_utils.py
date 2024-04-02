import unittest
from support.utils import gb_to_tb
from support.utils import kb_to_mb
from support.utils import mb_to_gb


class TestMbToGb(unittest.TestCase):
    def test_normal_conversion(self):
        result = mb_to_gb(1000)
        self.assertEqual(result, 1)

    def test_zero_mb(self):
        result = mb_to_gb(0)
        self.assertEqual(result, 0)

    def test_decimal_result(self):
        result = mb_to_gb(1500)
        self.assertEqual(result, 1.5)

    def test_large_number(self):
        result = mb_to_gb(2000000)
        self.assertEqual(result, 2000)

    def test_minimum_non_zero(self):
        result = mb_to_gb(1)
        self.assertEqual(result, 0.001)

    def test_negative_value(self):
        result = mb_to_gb(-1)
        self.assertEqual(result, -0.001)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            mb_to_gb("1000")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            mb_to_gb(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            mb_to_gb([1000])

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            mb_to_gb({'mb': 1000})


class TestKbToMb(unittest.TestCase):
    def test_1_kb_to_mb(self):
        result = kb_to_mb(1000)
        self.assertEqual(result, 1)

    def test_1_5_kb_to_mb(self):
        result = kb_to_mb(1500)
        self.assertEqual(result, 1.5)

    def test_2_kb_to_mb(self):
        result = kb_to_mb(2000)
        self.assertEqual(result, 2)

    def test_50_kb_to_mb(self):
        result = kb_to_mb(50000)
        self.assertEqual(result, 50)

    def test_100_kb_to_mb(self):
        result = kb_to_mb(100000)
        self.assertEqual(result, 100)

    def test_zero_kb_to_mb(self):
        result = kb_to_mb(0)
        self.assertEqual(result, 0)

    def test_minimal_positive_kb_to_mb(self):
        result = kb_to_mb(1)
        self.assertEqual(result, 0.001)

    def test_minimal_negative_kb_to_mb(self):
        result = kb_to_mb(-1)
        self.assertEqual(result, -0.001)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            kb_to_mb('a')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            kb_to_mb(None)
            
class TestGbToTb(unittest.TestCase):
    def test_convert_1000_gb_to_tb(self):
        result = gb_to_tb(1000)
        self.assertEqual(result, 1)

    def test_convert_500_gb_to_tb(self):
        result = gb_to_tb(500)
        self.assertEqual(result, 0.5)

    def test_convert_0_gb_to_tb(self):
        result = gb_to_tb(0)
        self.assertEqual(result, 0)

    def test_convert_1024_gb_to_tb(self):
        result = gb_to_tb(1024)
        self.assertEqual(result, 1.024)

    def test_convert_negative_gb_to_tb(self):
        result = gb_to_tb(-1)
        self.assertEqual(result, -0.001)

    def test_convert_large_gb_to_tb(self):
        result = gb_to_tb(1e6)
        self.assertEqual(result, 1000)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            gb_to_tb("1000")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            gb_to_tb(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            gb_to_tb([1000])

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            gb_to_tb({'gb': 1000})
