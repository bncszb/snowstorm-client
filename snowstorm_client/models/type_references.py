# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from snowstorm_client.models.concept_mini import ConceptMini
from typing import Optional, Set
from typing_extensions import Self

class TypeReferences(BaseModel):
    """
    TypeReferences
    """ # noqa: E501
    reference_type: Optional[ConceptMini] = Field(default=None, alias="referenceType")
    referencing_concepts: Optional[List[ConceptMini]] = Field(default=None, alias="referencingConcepts")
    __properties: ClassVar[List[str]] = ["referenceType", "referencingConcepts"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TypeReferences from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of reference_type
        if self.reference_type:
            _dict['referenceType'] = self.reference_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in referencing_concepts (list)
        _items = []
        if self.referencing_concepts:
            for _item_referencing_concepts in self.referencing_concepts:
                if _item_referencing_concepts:
                    _items.append(_item_referencing_concepts.to_dict())
            _dict['referencingConcepts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TypeReferences from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referenceType": ConceptMini.from_dict(obj["referenceType"]) if obj.get("referenceType") is not None else None,
            "referencingConcepts": [ConceptMini.from_dict(_item) for _item in obj["referencingConcepts"]] if obj.get("referencingConcepts") is not None else None
        })
        return _obj


