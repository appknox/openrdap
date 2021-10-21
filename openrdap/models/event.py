from dataclasses import dataclass
from datetime import datetime

from openrdap.utils import get_iso_format_date


@dataclass
class Event:
    action: str
    actor: str
    date: datetime

    @classmethod
    def parse(cls, data: dict):
        _date = data.get("eventDate", "")
        return cls(
            action=data.get("eventAction", ""),
            actor=data.get("eventActor", ""),
            date=get_iso_format_date(_date) if _date else None,
        )
