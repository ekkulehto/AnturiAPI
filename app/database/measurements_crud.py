from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from .models import MeasurementIn, MeasurementDb

def create_measurement(session: Session, measurement_in: MeasurementIn):
    measurement = MeasurementDb.model_validate(measurement_in)
    session.add(measurement)
    session.commit()
    session.refresh(measurement)
    return measurement

def get_all_measurements(session: Session):
    return session.exec(select(MeasurementDb)).all()

def get_measurement_by_id(session: Session, measurement_id: int):
    measurement = session.get(MeasurementDb, measurement_id)

    if not measurement:
        raise HTTPException(
            detail='Measurement not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return measurement

def delete_measurement_by_id(session: Session, measurement_id: int):
    measurement = session.get(MeasurementDb, measurement_id)

    if not measurement:
        raise HTTPException(
            detail='Measurement not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    session.delete(measurement)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)