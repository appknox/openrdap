from dataclasses import dataclass
from openrdap.exceptions import RequirdPropertyException


@dataclass
class Link:
    value: str
    href: str
    hreflang: list[str]
    title: str
    media: str
    link_type: str
    rel: str

    @classmethod
    def parse(cls, data: dict):
        href = data.get("href", "")
        if not href:
            raise RequirdPropertyException("link", "href")
        return cls(
            value=data.get("value", ""),
            href=href,
            hreflang=data.get("hreflang", []),
            title=data.get("title", ""),
            media=data.get("media", ""),
            link_type=data.get("type", ""),
            rel=data.get("rel", ""),
        )
