from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    action: str
    actor: str
    date: datetime

    @classmethod
    def parse(cls, data: dict):
        _date = data.get("eventDate", "")
        if "+" in _date:
            # FIXME: ISO DATE should be validated
            _date = _date.split("+")[0]
        return cls(
            action=data.get("eventAction", ""),
            actor=data.get("eventActor", ""),
            date=datetime.fromisoformat(_date) if _date else None,
        )
