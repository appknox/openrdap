from dataclasses import dataclass
from openrdap.models.link import Link
from openrdap.models.event import Event


@dataclass
class DsData:
    key_tag: int
    algorithm: int
    digest: str
    digest_type: int
    events: list[Event]
    links: list[Link]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            key_tag=data.get("keyTag", -1),
            algorithm=data.get("algorithm", -1),
            digest=data.get("digest", ""),
            digest_type=data.get("digestType", -1),
            events=[Event.parse(event) for event in data.get("events", [])],
            links=[Link.parse(link) for link in data.get("links", [])],
        )


@dataclass
class KeyData:
    flags: int
    protocol: int
    public_key: str
    algorithm: int
    events: list[Event]
    links: list[Link]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            flags=data.get("flags", -1),
            protocol=data.get("protocol", -1),
            public_key=data.get("publicKey", ""),
            algorithm=data.get("algorithm", -1),
            events=[Event.parse(event) for event in data.get("events", [])],
            links=[Link.parse(link) for link in data.get("links", [])],
        )


@dataclass
class SecureDNS:
    zone_signed: bool
    delegation_signed: bool
    max_sig_life: int
    ds_data: list[DsData]
    key_data: list[KeyData]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            zone_signed=data.get("zoneSigned", False),
            delegation_signed=data.get("delegationSigned", False),
            max_sig_life=data.get("maxSigLife", -1),
            ds_data=[DsData.parse(ds_data) for ds_data in data.get("dsData", [])],
            key_data=[KeyData.parse(ds_data) for ds_data in data.get("keyData", [])],
        )
