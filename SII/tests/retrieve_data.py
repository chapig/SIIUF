import unittest

from SII import lookup_uf_month_year, lookup_uf_date, YearError, MonthError, DayError, InvalidDateError


class TestSII(unittest.TestCase):

    def test_lookup_uf_month_year(self):
        # Test valid input
        self.assertIsNotNone(lookup_uf_month_year(month='Enero', year=2022))
        self.assertIsNotNone(lookup_uf_month_year(month=2, year=2022))
        self.assertIsNotNone(lookup_uf_month_year(month='Mayo', year=2020, day=15))
        # Test invalid input
        self.assertRaises(YearError, lookup_uf_month_year, month='Enero', year=1999)
        self.assertRaises(MonthError, lookup_uf_month_year, month='InvalidMonth', year=2022)
        self.assertRaises(DayError, lookup_uf_month_year, month=5, year=2022, day='InvalidDay')

    def test_lookup_uf_date(self):
        # Test valid input
        self.assertIsNotNone(lookup_uf_date('20-04-2023'))
        self.assertEqual(len(lookup_uf_date('20-04-2023')), 1)
        # Test invalid input
        self.assertRaises(InvalidDateError, lookup_uf_date, '20/04/2020')


if __name__ == '__main__':
    unittest.main()
