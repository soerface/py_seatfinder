import pandas as pd
import itertools
from datetime import datetime


class TimeseriesContainer(dict):

    def to_dataframe(self) -> pd.DataFrame:
        values = [
            {
                'free_seats': x['free_seats'],
                'occupied_seats': x['occupied_seats'],
                'location_name': x['location_name'],
                'timestamp': datetime.strptime(x['timestamp']['date'], '%Y-%m-%d %H:%M:%S.%f')
            } for x in itertools.chain(*self.values())]
        df = pd.DataFrame(values)
        df.index = pd.MultiIndex.from_arrays(df[['location_name', 'timestamp']].values.T, names=['location_name', 'timestamp'])
        df = df.drop(columns=['location_name', 'timestamp'])
        return df
