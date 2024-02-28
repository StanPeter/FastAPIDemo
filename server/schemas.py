from pydantic import BaseModel


# schema/model for pydantic to validate
class SoldierBaseSchema(BaseModel):
    name: str
    email: str


class SoldierSchema(SoldierBaseSchema):
    id: int

    class ConfigDict:
        from_attributes = True
