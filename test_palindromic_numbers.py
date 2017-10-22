import unittest
import palindromic_numbers as pn

class PalindromicNumbersTestCase(unittest.TestCase):
    first_twenty = ["1, 2",
                    "2, 3",
                    "3, 2",
                    "4, 3",
                    "5, 2",
                    "6, 5",
                    "7, 2",
                    "8, 3",
                    "9, 2",
                    "10, 3",
                    "11, 10",
                    "12, 5",
                    "13, 3",
                    "14, 6",
                    "15, 2",
                    "16, 3",
                    "17, 2",
                    "18, 5",
                    "19, 18",
                    "20, 3"
                    ]

    def test_find_smallest_palindromic_base(self):
        for i in range(1, 21):
            self.assertEqual(pn.find_smallest_palindromic_base(i), self.first_twenty[i-1])

if __name__ == '__main__':
    unittest.main()