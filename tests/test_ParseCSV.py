from unittest import TestCase

from top.scorers.ParseCSV import ParseCsv


class TestParseCsv(TestCase):
    def test_empty_csv(self):
        csv_file = "EmptyTest.csv"
        data = ParseCsv(csv_file, True).parse_csv()
        self.assertIsNone(data)

    def test_onlyHeader_csv(self):
        csv_file = "OnlyHeaderTest.csv"
        data = ParseCsv(csv_file, True).parse_csv()
        self.assertIsNone(data)

    def test_scores(self):
        csv_file = "ScoreTest.csv"
        data = ParseCsv(csv_file, True)
        data.parse_csv()
        self.assertEqual(data.getMaxScore(), 100)