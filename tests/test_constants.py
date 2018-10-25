import logging
import unittest
from seatfinder.constants import BASE_URL, LOCATIONS
from urllib import request


class TestConstants(unittest.TestCase):

    def test_base_url(self):
        for k, v in BASE_URL.items():
            logging.info(f'Testing BASE_URL of {k} ({v})')
            request.urlopen(v)

    def test_consistent_organizations(self):
        self.assertEqual(BASE_URL.keys(), LOCATIONS.keys())
