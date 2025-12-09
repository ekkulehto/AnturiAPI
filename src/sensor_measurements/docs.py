# =================================================================================
#    GET ALL SENSOR MEASUREMENTS
# =================================================================================

GET_SENSOR_MEASUREMENTS_BY_ID_SUMMARY = 'List sensor measurements by ID'
GET_SENSOR_MEASUREMENTS_BY_ID_DESCRIPTION = '''
- Return measurements for a single sensor by its ID.
- The response also includes basic sensor and segment details.
'''

# =================================================================================
#    CREATE NEW MEASUREMENT
# =================================================================================

CREATE_MEASUREMENT_SUMMARY = 'Create a new measurement by sensor ID'
CREATE_MEASUREMENT_DESCRIPTION = '''
- Store a single measurement sent by a sensor.
- Use the sensor ID to link the measurement to an existing sensor.
- Provide the measurement payload with value, unit, and type.
- The timestamp can be sent explicitly; if omitted, it is generated automatically by the server.
'''