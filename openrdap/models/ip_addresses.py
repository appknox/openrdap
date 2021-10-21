from dataclasses import dataclass


@dataclass
class IpAddresses:
    v6: list[str]
    v4: list[str]
