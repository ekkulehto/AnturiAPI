# =================================================================================
#    GET ALL MEASUREMENTS
# =================================================================================

GET_ALL_MEASUREMENTS_SUMMARY = 'List all measurements'
GET_ALL_MEASUREMENTS_DESCRIPTION = (
    'Return all measurements stored in the system for all sensors. '
    'Mainly intended for debugging, testing, or simple data views.'
)
GET_ALL_MEASUREMENTS_TYPE_FILTER_DESCRIPTION = (
    'Optional filter for measurement type. '
    'If omitted, measurements of all types are returned.'
)

# =================================================================================
#    CREATE NEW MEASUREMENT
# =================================================================================

CREATE_MEASUREMENT_SUMMARY = 'Create a new measurement'
CREATE_MEASUREMENT_DESCRIPTION = (
    'Store a single measurement sent by a sensor. '
    'The request must include the sensor ID and the measurement payload '
    '(value, unit, type, and timestamp).'
)

# =================================================================================
#    GET MEASUREMENT BY ID
# =================================================================================

GET_MEASUREMENT_BY_ID_SUMMARY = 'Get a measurement by ID'
GET_MEASUREMENT_BY_ID_DESCRIPTION = (
    'Fetch a single measurement using its unique ID. '
    'Returns the measurement data together with the sensor ID.'
)

# =================================================================================
#    DELETE MEASUREMENT BY ID
# =================================================================================

DELETE_MEASUREMENT_BY_ID_SUMMARY = 'Delete a measurement by ID'
DELETE_MEASUREMENT_BY_ID_DESCRIPTION = (
    'Delete a single measurement using its unique ID. '
    'Does not return any content, only the HTTP status code.'
)
