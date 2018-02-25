import unittest

from fizzle import dl_distance, dl_ratio, match_list, pick_N, pick_one, substring_search


class TestFizzle(unittest.TestCase):
    def setUp(self):
        self.commonErrors_dict = {
            ('a', 'e'): 0.4,
            ('i', 'y'): 0.3,
            ('m', 'n'): 0.5
        }
        self.commonErrors_list = [('a', 'e', 0.4), ('i', 'y', 0.3), ('m', 'n',
                                                                     0.5)]
        self.misspellings = [
            "Levenshtain", "Levenstein", "Levinstein", "Levistein",
            "Levemshtein"
        ]

    def test_dl_distance(self):
        self.assertEqual(
            dl_distance(
                'dayme', 'dayne', substitutions=self.commonErrors_dict), 0.5)

    def test_dl_ratio(self):
        self.assertEqual(dl_ratio("Levenshtein", "Levenshtein"), 1)

    def test_match_list(self):
        correct_answers = [(1, 'Levenshtain'), (1, 'Levenstein'),
                           (2, 'Levinstein'), (3, 'Levistein'),
                           (1, 'Levemshtein')]

        self.assertEqual(
            list(
                match_list(
                    "Levenshtein",
                    self.misspellings,
                    substitutions=self.commonErrors_dict)), correct_answers)

    def test_pick_N(self):
        top2 = [(1, 'Levemshtein'), (1, 'Levenshtain')]
        self.assertEqual(
            pick_N(
                "Levenshtein",
                self.misspellings,
                2,
                substitutions=self.commonErrors_dict), top2)

    def test_substring_search(self):
        self.assertEqual(
            substring_search("aaaabcegf", "qqqqq aaaaWWbcdefg qqqq"),
            "aaWWbcdef")


if __name__ == '__main__':
    unittest.main()
