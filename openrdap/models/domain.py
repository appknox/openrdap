from dataclasses import dataclass

from openrdap.models.entity import Entity
from openrdap.models.event import Event
from openrdap.models.link import Link
from openrdap.models.nameserver import Nameserver
from openrdap.models.network import Network
from openrdap.models.public_id import PublicId
from openrdap.models.remark import Remark
from openrdap.models.secure_dns import SecureDNS


@dataclass
class Domain:
    handle: str
    ldh_name: str
    unicode_name: str
    port43: str
    links: list[Link]
    events: list[Event]
    status: list[str]
    entities: list[Entity]
    remarks: list[Remark]
    secure_dns: SecureDNS
    nameservers: list[Nameserver]
    network: Network
    public_ids: list[PublicId]
    notices: list[Remark]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            handle=data.get("handle", ""),
            ldh_name=data.get("ldhName", ""),
            unicode_name=data.get("unicodeName", ""),
            port43=data.get("port43", ""),
            links=[Link.parse(link) for link in data.get("links", [])],
            events=[Event.parse(event) for event in data.get("events", [])],
            status=data.get("status", []),
            entities=[Entity.parse(entity) for entity in data.get("entities", [])],
            remarks=[Remark.parse(remark) for remark in data.get("remarks", [])],
            secure_dns=SecureDNS.parse(data.get("secureDNS")),
            nameservers=[Nameserver.parse(ns) for ns in data.get("nameservers", [])],
            network=Network.parse(data.get("netowrk")) if data.get("network") else None,
            public_ids=[PublicId.parse(pid) for pid in data.get("publicIds", [])],
            notices=[Remark.parse(notice) for notice in data.get("notices", [])],
        )
