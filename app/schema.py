from app.db.database import session_maker
from app.gql.models_types import *
import graphene as g
from graphene import String

from app.mutations import Mutation


class Query(g.ObjectType):
    mission_by_id = g.Field(MissionType,id=g.String(required=True))
    missions_by_range_date = g.List(MissionType,start_date=g.Date(required=True),end_date=g.Date(required=True))
    missions_by_country = g.List(MissionType,country_name=g.String(required=True))
    get_5_countries = g.List(CountryType)
    missions_by_target_industry = g.List(MissionType,target_industry=g.String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, id):
        with session_maker() as session:
            mission = session.query(Mission).get(id)
            mission.targets = session.query(Target).filter(Target.mission_id==mission.mission_id).all()
            return mission

    @staticmethod
    def resolve_missions_by_range_date(root, info, start_date, end_date):
        with session_maker() as session:
            missions = session.query(Mission).filter(Mission.mission_date >= start_date, Mission.mission_date <= end_date).all()
            return missions

    @staticmethod
    def resolve_missions_by_country(root, info, country_name):
        with session_maker() as session:
            country = session.query(Country).filter(Country.country_name.ilike(f"%{country_name}%")).first()
            missions = (
                session.query(Mission)
                .join(Target)
                .join(City)
                .filter(City.country_id == country.country_id)
                .all()
            )
            return missions

    @staticmethod
    def resolve_get_5_countries(root, info):
        with session_maker() as session:
            countries = session.query(Country).limit(5).all()
            return countries
    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        with session_maker() as session:
            missions = session.query(Mission).join(Target).filter(Target.target_industry == target_industry).all()
            return missions







schema = g.Schema(query=Query,mutation=Mutation)



# cities = session.query(City).filter(City.country_id == country.country_id).all()
            # missions_id = []
            # for city in cities:
            #     targets = session.query(Target).filter(Target.city_id == city.city_id).all()
            #     for target in targets:
            #         missions_id.append(target.mission_id)
            # missions = []
            # for mission_id in missions_id:
            #     mission = session.query(Mission).get(mission_id)
            #     missions.append(mission)
            # return missions