from collections import MutableMapping
from pathlib import Path
from typing import Iterator, Any, Hashable
import json


class DataContainer(MutableMapping):

    def __init__(self, path: Path):
        self.path = path
        if not self.path.exists():
            self.path.mkdir(parents=True)
        self.storage = dict()

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if key == 'locations':
            location_json = self.path / 'locations.json'
            with open(location_json, 'w') as f:
                json.dump(value, f)
        self.storage[key] = value

    def __delitem__(self, key: Hashable) -> None:
        del self.storage[key]

    def __getitem__(self, key: Hashable) -> Any:
        if key in self.storage:
            return self.storage[key]
        if key == 'locations':
            locations_json = self.path / 'locations.json'
            if locations_json.exists():
                with open(locations_json) as f:
                    return json.load(f)
        raise KeyError

    def __len__(self) -> int:
        return len(self.storage)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.storage)