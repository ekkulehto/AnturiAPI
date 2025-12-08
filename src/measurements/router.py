from fastapi import APIRouter, Path, Query, status, Depends
from sqlmodel import Session

from ..database import get_session
from ..measurements import service as crud
from ..models import MeasurementIn, MeasurementOutWithSensor, MeasurementType

from .docs import (
    GET_ALL_MEASUREMENTS_DESCRIPTION, 
    GET_ALL_MEASUREMENTS_SUMMARY,
    GET_ALL_MEASUREMENTS_TYPE_FILTER_DESCRIPTION,
    CREATE_MEASUREMENT_SUMMARY,
    CREATE_MEASUREMENT_DESCRIPTION,
    GET_MEASUREMENT_BY_ID_SUMMARY,
    GET_MEASUREMENT_BY_ID_DESCRIPTION,
    DELETE_MEASUREMENT_BY_ID_SUMMARY,
    DELETE_MEASUREMENT_BY_ID_DESCRIPTION
)

router = APIRouter(prefix='/sensors', tags=['Sensor Measurements'])

# =================================================================================
#    GET ALL MEASUREMENTS
# =================================================================================

@router.get(
        '/{sensor_id}/measurements', 
        response_model=list[MeasurementOutWithSensor], 
        summary=GET_ALL_MEASUREMENTS_SUMMARY, 
        description=GET_ALL_MEASUREMENTS_DESCRIPTION
)
def get_all_measurements(
    *, 
    session: Session = Depends(get_session),
    measurement_type: MeasurementType | None = Query(
        default=None,
        description=GET_ALL_MEASUREMENTS_TYPE_FILTER_DESCRIPTION
    )
):
    return crud.get_all_measurements(session, measurement_type)

# =================================================================================
#    CREATE NEW MEASUREMENT
# =================================================================================

@router.post(
        '/{sensor_id}/measurements', 
        status_code=status.HTTP_201_CREATED, 
        response_model=MeasurementOutWithSensor,
        summary=CREATE_MEASUREMENT_SUMMARY,
        description=CREATE_MEASUREMENT_DESCRIPTION
)
def create_measurement(
    *, 
    session: Session = Depends(get_session), 
    measurement_in: MeasurementIn
):
    return crud.create_measurement(session, measurement_in)

# =================================================================================
#    GET MEASUREMENT BY ID
# =================================================================================

@router.get(
        '/{sensor_id}/measurements/{measurement_id}', 
        response_model=MeasurementOutWithSensor,
        summary=GET_MEASUREMENT_BY_ID_SUMMARY,
        description=GET_MEASUREMENT_BY_ID_DESCRIPTION
)
def get_measurement_by_id(
    *, 
    session: Session = Depends(get_session), 
    measurement_id: int = Path(..., description='Unique identifier of the measurement to retrieve'),
):
    return crud.get_measurement_by_id(session, measurement_id)

# =================================================================================
#    DELETE MEASUREMENT BY ID
# =================================================================================

@router.delete(
        '/{sensor_id}/measurements/{measurement_id}', 
        status_code=status.HTTP_204_NO_CONTENT,
        summary=DELETE_MEASUREMENT_BY_ID_SUMMARY,
        description=DELETE_MEASUREMENT_BY_ID_DESCRIPTION
)
def delete_measurement_by_id(
    *, 
    session: Session = Depends(get_session), 
    measurement_id: int = Path(..., description='Unique identifier of the measurement to delete'),
):
    return crud.delete_measurement_by_id(session, measurement_id)