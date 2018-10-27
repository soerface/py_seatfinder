import unittest
from seatfinder.timeseries_container import TimeseriesContainer
import json
import pandas as pd


class TestTimeseriesContainer(unittest.TestCase):

    def setUp(self):
        with open('./seatfinder_data/Kassel/seatestimate_2018-10-25.json') as f:
            data = json.load(f)[0]['seatestimate']
        self.container = TimeseriesContainer(data)

    def test_to_dataframe(self):
        df = self.container.to_dataframe()
        self.assertEqual(pd.DataFrame, type(df))
        self.assertEqual(['free_seats', 'occupied_seats'], list(df.columns))
