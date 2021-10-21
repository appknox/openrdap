from dataclasses import dataclass
from openrdap.models.event import Event
from openrdap.models.link import Link
from openrdap.models.remark import Remark

from openrdap.models.entity import Entity


@dataclass
class Network:
    handle: str
    start_address: str
    end_address: str
    ip_version: str
    name: str
    network_type: str
    country: str
    parent_handle: str
    status: list[str]
    entites: list[Entity]
    remarks: list[Remark]
    links: list[Link]
    port43: str
    events: list[Event]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            handle=data.get("handle", ""),
            start_address=data.get("startAddress", ""),
            end_address=data.get("endAddress", ""),
            ip_version=data.get("ipVersion", ""),
            name=data.get("name", ""),
            network_type=data.get("type", ""),
            country=data.get("country", ""),
            parent_handle=data.get("parentHandle", ""),
            status=data.get("status", []),
            entities=[Entity.parse(entity) for entity in data.get("entities", [])],
            remarks=[Remark.parse(remark) for remark in data.get("remarks", [])],
            links=[Link.parse(link) for link in data.get("links", [])],
            port43=data.get("port43", ""),
            events=[Event.parse(event) for event in data.get("events", [])],
        )
