import unittest
from pathlib import Path
from datetime import datetime, timedelta
from seatfinder import Seatfinder


class TestTimeseriesLoader(unittest.TestCase):

    def setUp(self):
        self.seatfinder = Seatfinder('Kassel', data_dir='./tests/seatfinder_data/')

    def test_single_date(self):
        expected = {
            'free_seats': 123,
            'location_name': 'LeoEG',
            'occupied_seats': 9,
            'timestamp': {
                'date': '2018-09-20 08:39:56.000000',
                'timezone': 'Europe/Berlin',
                'timezone_type': 3
            }
        }
        self.assertEqual(expected, self.seatfinder.manual_count['2018-09-20']['LeoEG'][0])

    def test_slice(self):
        expected1 = {
            'free_seats': 123,
            'location_name': 'LeoEG',
            'occupied_seats': 9,
            'timestamp': {
                'date': '2018-09-20 08:39:56.000000',
                'timezone': 'Europe/Berlin',
                'timezone_type': 3
            }
        }
        expected2 = {
            'free_seats': 105,
            'location_name': 'LeoEG',
            'occupied_seats': 27,
            'timestamp': {
                'date': '2018-10-19 10:38:29.000000',
                'timezone': 'Europe/Berlin',
                'timezone_type': 3
            }
        }
        result = self.seatfinder.manual_count['2018-09-20':'2018-10-20']['LeoEG']
        self.assertEqual(expected1, result[0])
        self.assertEqual(expected2, result[-1])

    def test_no_save_today_and_future(self):
        data_dir = Path('./tests/seatfinder_data/')
        yesterday = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')
        today = datetime.now().strftime('%Y-%m-%d')
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        self.seatfinder.seat_estimate[yesterday:tomorrow]
        self.assertTrue((data_dir / 'Kassel' / f'seatestimate_{yesterday}.json').exists())
        self.assertFalse((data_dir / 'Kassel' / f'seatestimate_{today}.json').exists())
        self.assertFalse((data_dir / 'Kassel' / f'seatestimate_{tomorrow}.json').exists())

        del self.seatfinder.seat_estimate[yesterday]