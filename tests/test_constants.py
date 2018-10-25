import logging
import unittest
from seatfinder.constants import SCRIPT_URL, LOCATIONS
import requests


class TestConstants(unittest.TestCase):

    def test_base_url(self):
        for k, v in SCRIPT_URL.items():
            logging.info(f'Testing BASE_URL of {k} ({v})')
            self.assertEqual(200, requests.get(v).status_code)

    def test_consistent_organizations(self):
        self.assertEqual(SCRIPT_URL.keys(), LOCATIONS.keys())
