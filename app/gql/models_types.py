from graphene import relay, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.db.models.country_model import Country, City, Target, Mission, Targettype


class CountryType(SQLAlchemyObjectType):
    class Meta:
        model = Country
        interfaces = (relay.Node,)

class CityType(SQLAlchemyObjectType):
    class Meta:
        model = City
        interfaces = (relay.Node,)

class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = Target
        interfaces = (relay.Node,)

class TargettypeType(SQLAlchemyObjectType):
    class Meta:
        model = Targettype
        interfaces = (relay.Node,)

class MissionType(SQLAlchemyObjectType):
    class Meta:
        model = Mission
        interfaces = (relay.Node,)
    targets_list = List(TargetType)

