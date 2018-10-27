import unittest
from seatfinder.timeseries_container import TimeseriesContainer


class TestTimeseriesContainer(unittest.TestCase):

    def setUp(self):
        self.container = TimeseriesContainer()