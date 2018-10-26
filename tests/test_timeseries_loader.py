import unittest
from pathlib import Path

from seatfinder import Seatfinder


class TestTimeseriesLoader(unittest.TestCase):

    def setUp(self):
        data_dir = Path('/tmp/seatfinder_timeseries_loader')
        self.seatfinder = Seatfinder('Kassel', data_dir=data_dir)

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
