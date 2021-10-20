from dataclasses import dataclass

from openrdap.models.link import Link


@dataclass
class Remark:
    title: str
    description: list[str]
    links: list[Link]

    @classmethod
    def parse(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            description=data.get("description", []),
            links=[Link.parse(link) for link in data.get("links", [])],
        )
