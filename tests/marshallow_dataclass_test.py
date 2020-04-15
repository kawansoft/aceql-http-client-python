from dataclasses import dataclass, field
from typing import List, Optional

import marshmallow_dataclass
import marshmallow.validate

@dataclass
class Tables:
    # field metadata is used to instantiate the marshmallow field
    status: str
    tableNames: List[str]

    def __str__(self):
        """ The string representation."""
        return str(self.status) + ", " + str(self.tableNames)

@dataclass
class Building:
    # field metadata is used to instantiate the marshmallow field
    height: float
    name: str

    def __str__(self):
        """ The string representation."""
        return str(self.height) + ", " + str(self.name)

@dataclass
class City:
    name: Optional[str]
    buildings: List[Building]

    def __str__(self):
        """ The string representation."""
        return str(self.name) + ", " + str(self.buildings)


CitySchema = marshmallow_dataclass.class_schema(City)

city = CitySchema().load(
    {"name": "Paris", "buildings": [{"name": "Eiffel Tower", "height": 324}]}
)
# => City(name='Paris', buildings=[Building(height=324.0, name='Eiffel Tower')])
print(city)

city_dict = CitySchema().dump(city)
# => {'name': 'Paris', 'buildings': [{'name': 'Eiffel Tower', 'height': 324.0}]}
print(city_dict)

TablesSchema = marshmallow_dataclass.class_schema(Tables)

f = open("C:\\test\\table_names_json.txt","r")
jsonString = f.read()
f.close()
print()
print(jsonString)

tables =  TablesSchema().load(
    {"status": "OK", "tableNames": ["banned_usernames", "customer"] }
)
print(tables)

#string = "{\"status\": \"OK\", \"tableNames\": [\"banned_usernames\", \"customer\"] }"
tables =  TablesSchema().loads(jsonString)
print(tables)