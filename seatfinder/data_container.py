from collections.abc import MutableMapping
from pathlib import Path
from typing import Iterator, Any, Hashable, Union
import json


class DataContainer(MutableMapping):

    def __init__(self, path: Union[Path, str]):
        self.path = Path(path)
        if not self.path.exists():
            self.path.mkdir(parents=True)
        self._storage = dict()

    def __setitem__(self, key: Hashable, value: Any) -> None:
        location_json = self.path / f'{key}.json'
        with open(location_json, 'w') as f:
            json.dump(value, f)
        self._storage[key] = value

    def __delitem__(self, key: Hashable) -> None:
        del self._storage[key]

    def __getitem__(self, key: Hashable) -> Any:
        if key in self._storage:
            return self._storage[key]
        locations_json = self.path / f'{key}.json'
        if locations_json.exists():
            with open(locations_json) as f:
                self._storage[key] = json.load(f)
                return self._storage[key]
        raise KeyError

    def __len__(self) -> int:
        return len(self._storage)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._storage)

    def __contains__(self, key):
        if key in self._storage:
            return True
        return (self.path / f'{key}.json').exists()
