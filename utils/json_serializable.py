from __future__ import annotations

from typing import List, Optional, Any


class IJsonSerializable:
    @staticmethod
    def __iterate(fields: Any):
        return [
            '.'.join(field.split('.')[1:])
            for field in fields if field.split('.')[1:]
        ]

    @classmethod
    def __unpack(cls, value: IJsonSerializable, fields: List[str], exclude: List[str]):
        if hasattr(getattr(value, 'to_json', None), '__call__'):
            try:
                value.to_json(fields=cls.__iterate(fields), exclude=cls.__iterate(exclude))
            except TypeError:
                return value.to_json()
        return value

    def to_json(self, fields: Optional[List[str]] = None, exclude: Optional[List[str]] = None):
        fields = fields or self.__dict__.keys()
        exclude = exclude or []

        return {
            field: self.__unpack(getattr(self, field), fields, exclude)
            for field in [f.split('.')[0] for f in fields if f]
            if field not in exclude
        }
