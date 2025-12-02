from sqlmodel import SQLModel, Field, Relationship

class SensorBase(SQLModel):
    pass

class SensorIn(SensorBase):
    pass

class SensorDb(SensorBase, table=True):
    pass

class SegmentBase(SQLModel):
    pass

class SegmentIn(SegmentBase):
    pass

class SegmentDb(SegmentBase, table=True):
    pass