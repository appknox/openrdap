from dataclasses import dataclass

from openrdap.models.entity import Entity
from openrdap.models.event import Event
from openrdap.models.link import Link
from openrdap.models.remark import Remark


@dataclass
class Autnum:
    handle: str
    start_autnum: int
    end_autnum: int
    name: str
    autnum_type: str
    status: list[str]
    country: str
    entities: list[Entity]
    remarks: list[Remark]
    links: list[Link]
    port43: str
    events: list[Event]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            handle=data.get("handle", ""),
            start_autnum=data.get("startAutnum", ""),
            end_autnum=data.get("endAutnum", ""),
            name=data.get("name", ""),
            autnum_type=data.get("autnumType", ""),
            status=data.get("status", []),
            country=data.get("country", ""),
            entities=[Entity.parse(entity) for entity in data.get("entities", [])],
            remarks=[Remark.parse(remark) for remark in data.get("remarks", [])],
            links=[Link.parse(link) for link in data.get("links", [])],
            port43=data.get("port43", ""),
            events=[Event.parse(event) for event in data.get("events", [])],
        )
