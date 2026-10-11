import unittest

from dna_report import build_report


class TestDnaReport(unittest.TestCase):
    def test_example_from_the_task(self):
        expected = (
            "A: 2 (25.0%)\n"
            "C: 2 (25.0%)\n"
            "G: 2 (25.0%)\n"
            "T: 2 (25.0%)\n"
            "Length: 8, GC content: 50.0%"
        )
        self.assertEqual(build_report("ACGTACGT"), expected)

    def test_lowercase_and_mixed_case(self):
        self.assertEqual(build_report("acgtacgt"), build_report("ACGTACGT"))
        self.assertEqual(build_report("AcGtAcGt"), build_report("ACGTACGT"))

    def test_rounds_to_one_decimal(self):
        expected = (
            "A: 1 (33.3%)\n"
            "C: 1 (33.3%)\n"
            "G: 1 (33.3%)\n"
            "T: 0 (0.0%)\n"
            "Length: 3, GC content: 66.7%"
        )
        self.assertEqual(build_report("ACG"), expected)

    def test_no_g_and_no_c(self):
        expected = (
            "A: 3 (60.0%)\n"
            "C: 0 (0.0%)\n"
            "G: 0 (0.0%)\n"
            "T: 2 (40.0%)\n"
            "Length: 5, GC content: 0.0%"
        )
        self.assertEqual(build_report("AATTA"), expected)

    def test_single_base(self):
        expected = (
            "A: 0 (0.0%)\n"
            "C: 0 (0.0%)\n"
            "G: 1 (100.0%)\n"
            "T: 0 (0.0%)\n"
            "Length: 1, GC content: 100.0%"
        )
        self.assertEqual(build_report("g"), expected)

    def test_spaces_around_the_sequence_are_ignored(self):
        self.assertEqual(build_report("  ACGTACGT  "), build_report("ACGTACGT"))

    def test_empty_input_is_rejected(self):
        message = "Error: the sequence is empty. Please type some letters A, C, G or T."
        self.assertEqual(build_report(""), message)
        self.assertEqual(build_report("   "), message)

    def test_other_characters_are_rejected(self):
        message = "Error: the sequence may only contain the letters A, C, G and T."
        self.assertEqual(build_report("ACGU"), message)
        self.assertEqual(build_report("ACG T"), message)
        self.assertEqual(build_report("AC1G"), message)


if __name__ == "__main__":
    unittest.main()  