from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    birthday_date: date
    
    
oleg = User(id=1, 
            name='Oleg', 
            birthday_date=date(year=1993, month=2, day=19))

to_dict = oleg.model_dump()
to_json = oleg.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))