import unittest
from seatfinder import Seatfinder
from pathlib import Path


class TestSeatfinder(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Seatfinder('Buxdehude')

        seatfinder = Seatfinder('Kassel')
        assert (Path.home() / '.seatfinder/data').exists()
