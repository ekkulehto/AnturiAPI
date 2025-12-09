from fastapi import APIRouter, Path, status, Depends
from sqlmodel import Session

from ..database import get_session
from ..measurements import service as crud
from ..models import MeasurementOutWithSensor

from .docs import (
    GET_MEASUREMENT_BY_ID_SUMMARY,
    GET_MEASUREMENT_BY_ID_DESCRIPTION,
    DELETE_MEASUREMENT_BY_ID_SUMMARY,
    DELETE_MEASUREMENT_BY_ID_DESCRIPTION
)

router = APIRouter(prefix='/measurements', tags=['Measurements'])

# =================================================================================
#    GET MEASUREMENT BY ID
# =================================================================================

@router.get(
        '/{measurement_id}', 
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
        '/{measurement_id}', 
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