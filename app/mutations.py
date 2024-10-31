import graphene
from app.db.database import session_maker as session
from app.db.models.country_model import Mission
from app.gql.models_types import MissionType


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
    print(8)
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
        print(new_mission.mission_id)
        with session():

            session.add(new_mission)
            session.commit()
            session.refresh(new_mission)
            return AddMission(mission=new_mission)

class AddTarget(graphene.Mutation):



class Mutation(graphene.ObjectType):
    add_mission = AddMission.Field()

