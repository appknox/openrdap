from dataclasses import dataclass

from openrdap.models.entity import Entity
from openrdap.models.event import Event
from openrdap.models.ip_addresses import IpAddresses
from openrdap.models.link import Link
from openrdap.models.remark import Remark


@dataclass
class Nameserver:
    handle: str
    ldh_name: str
    unicode_name: str
    ip_addresses: IpAddresses
    entities: list[Entity]
    status: list[str]
    remarks: list[Remark]
    links: list[Link]
    port43: str
    events: list[Event]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            handle=data.get("handle", ""),
            ldh_name=data.get("ldhName", ""),
            unicode_name=data.get("unicodeName", ""),
            ip_addresses=IpAddresses.parse(data.get("ipAddresses"))
            if data.get("ipAddresses")
            else None,
            entities=[Entity.parse(entity) for entity in data.get("entities", [])],
            status=data.get("status", []),
            remarks=[Remark.parse(remark) for remark in data.get("remarks", [])],
            links=[Link.parse(link) for link in data.get("links", [])],
            port43=data.get("port43", ""),
            events=[Event.parse(event) for event in data.get("events", [])],
        )
