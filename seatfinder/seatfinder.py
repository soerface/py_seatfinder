from seatfinder.constants import BASE_URL, DATA_DIR, LOCATIONS


class Seatfinder():

    def __init__(self, organization, data_dir=DATA_DIR):
        if organization not in BASE_URL:
            valid_organizations = ', '.join(BASE_URL.keys())
            raise ValueError(
                f'"{organization}" is not a valid organization. Valid organizations are: {valid_organizations}"')

        if not data_dir.exists():
            data_dir.mkdir(parents=True)

        self.locations = self._fetch_locations(LOCATIONS[organization])

    def _fetch_locations(self, locations):
        pass
