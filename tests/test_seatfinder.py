import unittest
from seatfinder import Seatfinder
from seatfinder.constants import LOCATIONS
from pathlib import Path
import shutil


class TestSeatfinder(unittest.TestCase):

    def setUp(self):
        self.seatfinder_ks = Seatfinder('Kassel', '/tmp/seatfinder_test')

    def test_init(self):
        with self.assertRaises(ValueError):
            Seatfinder('Buxdehude')

        Seatfinder('Kassel')
        self.assertTrue((Path.home() / '.seatfinder/data').exists())

        tmp_path = Path('/tmp/seatfinder_test_init')
        if tmp_path.exists():
            shutil.rmtree(str(tmp_path), ignore_errors=True)

        self.assertFalse(tmp_path.exists())
        Seatfinder('Kassel', data_dir=tmp_path)
        self.assertTrue(tmp_path.exists())

    def test_location(self):
        sf = self.seatfinder_ks
        self.assertEqual(set(sf.locations.keys()), set(LOCATIONS['Kassel']))
        self.assertIn('available_seats', sf.locations['LeoOG'])
        self.assertIn('building', sf.locations['LeoOG'])
        self.assertIn('geo_coordinates', sf.locations['LeoOG'])
        self.assertIn('level', sf.locations['LeoOG'])
        self.assertIn('long_name', sf.locations['LeoOG'])
        self.assertIn('name', sf.locations['LeoOG'])
        self.assertIn('opening_hours', sf.locations['LeoOG'])
        self.assertIn('room', sf.locations['LeoOG'])
        self.assertIn('sub_locations', sf.locations['LeoOG'])
        self.assertIn('super_location', sf.locations['LeoOG'])
        self.assertIn('timestamp', sf.locations['LeoOG'])
        self.assertIn('url', sf.locations['LeoOG'])