from dataclasses import dataclass, field
from typing import List, Optional, ClassVar
from typing import ClassVar, Type

import marshmallow_dataclass
import marshmallow.validate
from marshmallow import Schema
from typing_extensions import Type


@dataclass
class Tables:
    # field metadata is used to instantiate the marshmallow field
    status: str
    tableNames: List[str]
    toto: bool
    Schema: ClassVar[Type[Schema]] = Schema

    def __str__(self):
        """ The string representation."""
        return str(self.status) + ", " + str(self.tableNames)


@dataclass
class Building():
    # field metadata is used to instantiate the marshmallow field
    height: float
    name: str

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return str(self.height) + ", " + str(self.name)

@dataclass
class City():
    name: Optional[str]
    buildings: List[Building]
    is_high: bool

    class Meta:
        ordered = True

    def get_name(self):
        return self.name

    def __str__(self):
        """ The string representation."""
        return str(self.name) + ", " + str(self.buildings) + "," + str(self.is_high)

f = open("C:\\test\\json_test.txt","r")
jsonString = f.read()
f.close()
print()
print(jsonString)

CitySchema = marshmallow_dataclass.class_schema(City )

# city = CitySchema().load(
#     {"name": "Paris", "buildings": [{"name": "Eiffel Tower", "height": 324}], "is_high": False}
# )
city : City = CitySchema().loads(jsonString)

# => City(name='Paris', buildings=[Building(height=324.0, name='Eiffel Tower')])
print(city.get_name())

# city_dict = CitySchema().dump(city)
# # => {'name': 'Paris', 'buildings': [{'name': 'Eiffel Tower', 'height': 324.0}]}
# print(city_dict)

# TablesSchema = marshmallow_dataclass.class_schema(Tables)
#
# f = open("C:\\test\\table_names_json.txt","r")
# jsonString = f.read()
# f.close()
# print()
# print(jsonString)
#
# tables =  TablesSchema().load(
#     {"status": "OK", "tableNames": ["banned_usernames", "customer"] }
# )
# print(tables)
#
# #string = "{\"status\": \"OK\", \"tableNames\": [\"banned_usernames\", \"customer\"] }"
# tables =  TablesSchema().loads(jsonString)
# print(tables)