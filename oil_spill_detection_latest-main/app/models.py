from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime
from .database import Base

class AISData(Base):
    __tablename__ = "ais_data"

    id = Column(Integer, primary_key=True, index=True)
    mmsi = Column(BigInteger, index=True)
    base_date_time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    sog = Column(Float)  # Speed Over Ground
    cog = Column(Float)  # Course Over Ground
    heading = Column(Float)
    vessel_name = Column(String(255))
    imo = Column(String(50))
    call_sign = Column(String(50))
    vessel_type = Column(Integer)
    status = Column(Integer)
    length = Column(Float)
    width = Column(Float)
    draft = Column(Float)
    cargo = Column(Float)
    transceiver_class = Column(String(1))
