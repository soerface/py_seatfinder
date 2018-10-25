from datetime import datetime, timedelta
from typing import Union, TYPE_CHECKING
import requests
import pandas as pd

if TYPE_CHECKING:
    from seatfinder import Seatfinder


class TimeseriesLoader:

    def __init__(self, value, seatfinder: 'Seatfinder'):
        self._value = value
        self._seatfinder = seatfinder

    def __getitem__(self, item: Union[datetime, str, slice]):
        if type(item) == slice:
            start, stop, step = item.start, item.stop, item.step
            if start is None:
                raise ValueError("Can't slice from beginning, need to pass a startdate")
            if stop is None:
                stop = datetime.now()
        else:
            start = item
            stop = None
            step = None
        if type(start) != datetime:
            start = datetime.strptime(start, '%Y-%m-%d')
        if not stop:
            return self._request(start)
        if type(stop) != datetime:
            stop = datetime.strptime(stop, '%Y-%m-%d')
        date = start
        result = {}
        while date < stop:
            response = self._request(date)
            for k, v in response.items():
                if k not in result:
                    result[k] = v
                else:
                    result[k].extend(v)
            date += timedelta(days=step or 1)
        return result

    def _request(self, date: datetime):
        after = date.strftime('%Y-%m-%d')
        date_before = date + timedelta(days=1)
        before = date_before.strftime('%Y-%m-%d')

        key = f'{self._value}_{after}'
        response = self._seatfinder._data.get(key)

        if not response:
            response = requests.get(self._seatfinder._script_url, {
                'values': self._value,
                'location': ','.join(self._seatfinder._locations),
                'after': after,
                'before': before,
            }).json()
            if datetime.strptime(after, '%Y-%m-%d') < datetime.now():
                # Never safe the current day or the future, since the response will still change
                self._seatfinder._data[key] = response
        return response[0][self._value]
