from fastapi import HTTPException, status
from sqlmodel import Session

from ..models import (
    MeasurementDb, 
    MeasurementOut, 
    MeasurementOutWithSensor,
)

# =================================================================================
#    GET MEASUREMENT BY ID
# =================================================================================

def get_measurement_by_id(session: Session, measurement_id: int):
    measurement = session.get(MeasurementDb, measurement_id)

    if not measurement:
        raise HTTPException(
            detail='Measurement not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return MeasurementOutWithSensor(
            sensor_id=measurement.sensor_id,
            measurement=MeasurementOut(
                id=measurement.id,
                type=measurement.type,
                unit=measurement.unit,
                value=measurement.value,
                timestamp=measurement.timestamp,
            )
        )

# =================================================================================
#    DELETE MEASUREMENT BY ID
# =================================================================================

def delete_measurement_by_id(session: Session, measurement_id: int):
    measurement = session.get(MeasurementDb, measurement_id)

    if not measurement:
        raise HTTPException(
            detail='Measurement not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    session.delete(measurement)
    session.commit()