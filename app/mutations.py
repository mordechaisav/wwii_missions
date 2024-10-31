import graphene
from app.db.database import session_maker as session
from app.db.models.country_model import Mission, Target
from app.gql.models_types import MissionType, TargetType


# add class mutations to add mission with this arguments

class AddMission(graphene.Mutation):
    class Arguments:
        mission_id = graphene.Int(required=False)
        mission_date = graphene.Date()
        airborne_aircraft = graphene.Float()
        attacking_aircraft = graphene.Float()
        bombing_aircraft = graphene.Float()
        aircraft_returned = graphene.Float()
        aircraft_failed = graphene.Float()
        aircraft_damaged = graphene.Float()
        aircraft_lost = graphene.Float()

    mission = graphene.Field(MissionType)

    def mutate(self, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost,mission_id=None):
        new_mission = Mission(
            mission_id=mission_id,
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost
        )

        with session():

            session.add(new_mission)
            session.commit()
            session.refresh(new_mission)
            return AddMission(mission=new_mission)


class AddTarget(graphene.Mutation):
    class Arguments:
        target_id = graphene.Int(required=False)
        mission_id = graphene.Int(required=False)
        target_industry = graphene.String(required=False)
        city_id = graphene.Int(required=False)
        target_type_id = graphene.Int(required=False)
        target_priority = graphene.Int(required=False)

    target = graphene.Field(TargetType)
    def mutate(self, info, target_industry, city_id, target_type_id, target_priority, mission_id=None, target_id=None):
        new_target = Target(
            target_id=target_id,
            mission_id=mission_id,
            target_industry=target_industry,
            city_id=city_id,
            target_type_id=target_type_id,
            target_priority=target_priority
        )
        with session():
            session.add(new_target)
            session.commit()
            session.refresh(new_target)
            return AddTarget(target=new_target)

class UpdateTarget(graphene.Mutation):
    class Arguments:
        target_id = graphene.Int(required=True)
        target_industry = graphene.String()
        city_id = graphene.Int()
        target_type_id = graphene.Int()
        target_priority = graphene.Int()
        mission_id = graphene.Int()
    target = graphene.Field(TargetType)
    def mutate(self, info, target_id, target_industry=None, city_id=None, target_type_id=None, target_priority=None, mission_id=None):
        target = session.query(Target).get(target_id)
        if target:
            target.target_industry = target_industry or target.target_industry
            target.city_id = city_id or target.city_id
            target.target_type_id = target_type_id or target.target_type_id
            target.target_priority = target_priority or target.target_priority
            target.mission_id = mission_id or target.mission_id
            session.commit()
            return UpdateTarget(target=target)
        else:
            return None
class DeleteMission(graphene.Mutation):
    class Arguments:
        mission_id = graphene.Int(required=True)
    ok = graphene.Boolean(required=True)
    def mutate(self, info, mission_id):
        mission = session.query(Mission).get(mission_id)
        if mission:
            session.delete(mission)
            session.commit()
            return DeleteMission(ok=True)
        else:
            return DeleteMission(ok=False)




class Mutation(graphene.ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
    update_target = UpdateTarget.Field()

