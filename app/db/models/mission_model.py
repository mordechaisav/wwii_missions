from sqlalchemy import Column, Integer, Date, Numeric
from sqlalchemy.orm import relationship

from app.db.models import Base


class Mission(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=False)
    airborne_aircraft = Column(Numeric(10, 2), nullable=False)
    attacking_aircraft = Column(Numeric(10, 2), nullable=False)
    bombing_aircraft = Column(Numeric(10, 2), nullable=False)
    aircraft_returned = Column(Numeric(10, 2), nullable=False)
    aircraft_failed = Column(Numeric(10, 2), nullable=False)
    aircraft_damaged = Column(Numeric(10, 2), nullable=False)
    aircraft_lost = Column(Numeric(10, 2), nullable=False)
    #targets = relationship('Target', back_populates='mission')
