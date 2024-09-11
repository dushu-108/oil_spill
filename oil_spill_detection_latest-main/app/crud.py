from sqlalchemy.orm import Session
from sqlalchemy import update
from .models import AISData
from .schemas import VesselCreate, VesselUpdate

# Create a new vessel record
def create_vessel(db: Session, vessel: VesselCreate):
    db_vessel = AISData(
        mmsi=vessel.mmsi,
        base_date_time=vessel.base_date_time,
        latitude=vessel.latitude,
        longitude=vessel.longitude,
        sog=vessel.sog,
        cog=vessel.cog,
        heading=vessel.heading,
        vessel_name=vessel.vessel_name,
        imo=vessel.imo,
        call_sign=vessel.call_sign,
        vessel_type=vessel.vessel_type,
        status=vessel.status,
        length=vessel.length,
        width=vessel.width,
        draft=vessel.draft,
        cargo=vessel.cargo,
        transceiver_class=vessel.transceiver_class
    )
    db.add(db_vessel)
    db.commit()
    db.refresh(db_vessel)
    return db_vessel

# Retrieve a vessel by its ID
def get_vessel(db: Session, vessel_id: int):
    return db.query(AISData).filter(AISData.id == vessel_id).first()

# Retrieve all vessels (optionally, with filters)
def get_vessels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AISData).offset(skip).limit(limit).all()

# Update a vessel's data
def update_vessel(db: Session, vessel_id: int, vessel_update: VesselUpdate):
    db_vessel = db.query(AISData).filter(AISData.id == vessel_id).first()
    if db_vessel:
        for key, value in vessel_update.dict(exclude_unset=True).items():
            setattr(db_vessel, key, value)
        db.commit()
        db.refresh(db_vessel)
    return db_vessel

# Delete a vessel by its ID
def delete_vessel(db: Session, vessel_id: int):
    db_vessel = db.query(AISData).filter(AISData.id == vessel_id).first()
    if db_vessel:
        db.delete(db_vessel)
        db.commit()
    return db_vessel
