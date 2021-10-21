from dataclasses import dataclass


@dataclass
class PublicId:
    public_id_type: str
    identifier: str

    @classmethod
    def parse(cls, data: dict):
        return cls(
            public_id_type=data.get("type", ""),
            identifier=data.get("identifier", ""),
        )
