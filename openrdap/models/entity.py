from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from openrdap.exceptions import InvalidObjectExcption
import openrdap.models
from openrdap.models.event import Event
from openrdap.models.public_id import PublicId
from openrdap.models.remark import Remark


@dataclass
class Language:
    lang: str
    preference: str

    @classmethod
    def parse(cls, data: list):
        return cls(lang=data[3], preference=data[1].get("pref", ""))


@dataclass
class Telephone:
    tel: str = ""
    ext: str = ""
    tel_type: list[str] = field(default_factory=list)
    pref: str = ""

    @classmethod
    def parse(cls, data: list):
        prop_params = data[1]
        uri_split = data[3].split(";")
        return cls(
            tel=uri_split[0],
            ext=uri_split[1] if len(uri_split) == 2 else "",
            tel_type=prop_params.get("type", []),
            pref=prop_params.get("pref", ""),
        )


@dataclass
class Contact:
    version: str = ""
    fn: str = ""
    kind: str = ""
    languages: list[str] = field(default_factory=list)
    org: str = ""
    title: str = ""
    role: str = ""
    address: str = ""
    telephone: list[Telephone] = field(default_factory=list)
    email: str = ""

    @classmethod
    def parse(cls, vcard: list):
        contact = cls()
        for record in vcard:
            property = record[0]
            value = record[3]
            if property == "version":
                contact.version = value
            if property == "fn":
                contact.fn = value
            if property == "kind":
                contact.kind = value
            if property == "lang":
                contact.languages.append(Language.parse(record))
            if property == "org":
                contact.org = value
            if property == "title":
                contact.title = value
            if property == "role":
                contact.role = value
            if property == "adr":
                contact.address = "\n".join(value)
            if property == "tel":
                contact.telephone.append(Telephone.parse(record))
            if property == "email":
                contact.email = value
        return contact


@dataclass
class Entity:
    handle: str
    vcard_array: list[Contact]
    roles: list[str]
    public_ids: list[PublicId]
    entities: list[Entity]
    remarks: list[Remark]
    status: list[str]
    as_event_actor: list[Event]
    port43: str
    networks: list[openrdap.models.Network]
    autnums: list[openrdap.models.Autnum]

    @classmethod
    def _parse_vcards(cls, vcard_array: list) -> list[Contact]:
        contacts = []
        if not vcard_array:
            return []
        cls._validate_vcard_array(vcard_array)

        for vcard in vcard_array[1:]:
            cls._validate_vcard(vcard)
            contact = Contact.parse(vcard)
            contacts.append(contact)
        return contacts

    @classmethod
    def _validate_vcard_array(cls, vcard_array: list):
        if len(vcard_array) < 2:
            raise InvalidObjectExcption(
                "Invalid vcardArray. It should have at least 2 elements."
            )
        if vcard_array[0] != "vcard":
            raise InvalidObjectExcption(
                "Invalid vcardArray. First element should be string with value vcard ."
            )
        if not isinstance(vcard_array[1], list):
            raise InvalidObjectExcption(
                "Invalid vcardArray. Second element should be of type list."
            )

    @classmethod
    def _validate_vcard(cls, vcard: list):
        for record in vcard:
            if not isinstance(record, list):
                raise InvalidObjectExcption("vcard data must be list")
            if len(record) != 4:
                raise InvalidObjectExcption("vcard data list must contain 4 elements")

    @classmethod
    def parse(cls, data: dict):
        vcards = cls._parse_vcards(data.get("vcardArray", []))

        return cls(
            handle=data.get("hande", ""),
            vcard_array=vcards,
            roles=data.get("roles", []),
            public_ids=[PublicId.parse(p_id) for p_id in data.get("publicIds", [])],
            entities=[Entity.parse(entity) for entity in data.get("entities", [])],
            remarks=[Remark.parse(remark) for remark in data.get("remarks", [])],
            status=data.get("status", []),
            as_event_actor=[
                Event.parse(event) for event in data.get("asEventActor", [])
            ],
            port43=data.get("port43", ""),
            networks=[
                openrdap.models.Network.parse(network)
                for network in data.get("networks", [])
            ],
            autnums=[
                openrdap.models.Autnum.parse(aut_num)
                for aut_num in data.get("autnums", [])
            ],
        )
