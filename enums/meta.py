from enum import Enum


class Meta(Enum):
    storage = {
        "0": "NY",
        "1": "LA",
        "2": "IL"
    }
    status = {
        "R": "READY",
        "N": "NOT READY"
    }
    state = {
        "O": "OK",
        "B": "BROKEN",
        "F": "NO FUEL"
    }
    loaded = {
        "Y": "YES",
        "N": "NO"
    }
    departed = {
        "Y": "YES",
        "N": "NO"
    }
