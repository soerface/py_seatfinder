from pathlib import Path

from seatfinder.constants import SCRIPT_URL, DATA_DIR, LOCATIONS
import requests

from seatfinder.data_container import DataContainer


class Seatfinder:

    def __init__(self, organization, data_dir=DATA_DIR):
        if organization not in SCRIPT_URL:
            valid_organizations = ', '.join(SCRIPT_URL.keys())
            raise ValueError(
                f'"{organization}" is not a valid organization. Valid organizations are: {valid_organizations}"'
            )

        self._locations = LOCATIONS[organization]
        self._script_url = SCRIPT_URL[organization]

        if data_dir:
            if not data_dir.exists():
                data_dir.mkdir(parents=True)
            self.data = DataContainer(path=Path(data_dir) / organization)
        else:
            self.data = {}

    @property
    def locations(self):
        response = self.data.get('locations')

        if not response:
            response = requests.get(self._script_url, {
                'location': ','.join(self._locations),
                'values': 'location',
            }).json()
            self.data['locations'] = response

        return {k: v[0] if len(v) == 1 else v for k, v in response[0]['location'].items()}
