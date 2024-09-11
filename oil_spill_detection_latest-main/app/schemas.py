from pydantic import BaseModel
from typing import Optional

class VesselCreate(BaseModel):
    mmsi: str
    base_date_time: str
    latitude: float
    longitude: float
    sog: float
    cog: float
    heading: int
    vessel_name: Optional[str] = None
    imo: Optional[str] = None
    call_sign: Optional[str] = None
    vessel_type: Optional[str] = None
    status: Optional[str] = None
    length: Optional[float] = None
    width: Optional[float] = None
    draft: Optional[float] = None
    cargo: Optional[str] = None
    transceiver_class: Optional[str] = None

class VesselUpdate(BaseModel):
    base_date_time: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    sog: Optional[float] = None
    cog: Optional[float] = None
    heading: Optional[int] = None
    vessel_name: Optional[str] = None
    imo: Optional[str] = None
    call_sign: Optional[str] = None
    vessel_type: Optional[str] = None
    status: Optional[str] = None
    length: Optional[float] = None
    width: Optional[float] = None
    draft: Optional[float] = None
    cargo: Optional[str] = None
    transceiver_class: Optional[str] = None
