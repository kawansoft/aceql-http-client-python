from typing import ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass

@dataclass(order=True) # preserve field order
class Point:
  x:float
  y:float
  Schema: ClassVar[Type[Schema]] = Schema # For the type checker

point = Point.Schema().load({'x':0, 'y':0}) # This line can be statically type checked

