# python most_active_cookie.py
import unittest

from most_active_cookie import ActiveCookie

class TestActiveCookie(unittest.TestCase):

    def test_date_2018_12_07(self):
        """
        Test on date = '2018-12-07'. 
        One option for most active cookie; 1 most active cookie.
        """
        file_name = 'cookie_log.csv'
        ds = '2018-12-07'
        cur = ActiveCookie(file_name, ds, {})
        ret = cur.main()
        self.assertEqual(ret, ['4sMM2LxV07bPJzwf'])
        self.assertEqual(len(ret), 1)

    def test_date_2018_12_08(self):
        """
        Test on date = '2018-12-08'. 
        Three options for most active cookie; 3 most active cookies.
        """
        file_name = 'cookie_log.csv'
        ds = '2018-12-08'
        cur = ActiveCookie(file_name, ds, {})
        ret = cur.main()
        self.assertEqual(ret, ['4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG', 'SAZuXPGUrfbcn5UA'])
        self.assertEqual(len(ret), 3)

    def test_date_2018_12_09(self):
        """
        Test on date = '2018-12-09'. 
        Four options for most active cookie; 1 most active cookie.
        """
        file_name = 'cookie_log.csv'
        ds = '2018-12-09'
        cur = ActiveCookie(file_name, ds, {})
        ret = cur.main()
        self.assertEqual(ret, ['AtY0laUfhglK3lC7'])
        self.assertEqual(len(ret), 1)

if __name__ == '__main__':
    unittest.main()
