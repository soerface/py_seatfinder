import unittest
import json
from pathlib import Path

from seatfinder.data_container import DataContainer


class TestDataContainer(unittest.TestCase):

    def setUp(self):
        self.path = Path('/tmp/seatfinder_data_container_test')
        self.data = DataContainer(self.path)

    def test_setitem(self):
        self.data['lel'] = 42
        self.assertTrue((self.path / 'lel.json').exists())

    def test_getitem(self):
        test_object = {'some': 52, 'data': 99}
        with open(self.path / 'getitem_test.json', 'w') as f:
            json.dump(test_object, f)

        self.assertEqual(test_object, self.data['getitem_test'])

    def test_delitem(self):
        self.data['top'] = 42
        self.data['kek'] = 42
        self.assertTrue((self.path / 'top.json').exists())
        self.assertTrue((self.path / 'kek.json').exists())
        del self.data['top']
        self.data.pop('kek')
        self.assertFalse((self.path / 'top.json').exists())
        self.assertFalse((self.path / 'kek.json').exists())

    def test_contains(self):
        test_object = {'some': 52, 'data': 99}
        with open(self.path / 'contains_test.json', 'w') as f:
            json.dump(test_object, f)

        self.assertIn('contains_test', self.data)
        self.assertNotIn('no_such_contains_test', self.data)
