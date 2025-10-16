from datetime import date
from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    id: int
    name: str
    birthday_date: date
    
    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")
    
    
    @model_validator(mode='after')
    def check_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year - (
            (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))
        
        if age < 18:
            raise ValueError("Пользователь должен быть старше 18 лет")
        if age > 120:
            raise ValueError("Возраст не может превышать 120 лет")
        return self
    
    @model_validator(mode='after')
    def set_default_name(self):
        if self.name.strip() == '':
            self.name = f"User_{self.id}"
        return self
    
    
    
'''oleg = User(id=1, 
            name='Oleg', 
            birthday_date=date(year=1993, month=2, day=19))

to_dict = oleg.model_dump()
to_json = oleg.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))'''

user_data = {'id': 3, 'name': '156', 'birthday_date': '1990-11-22'}
user = User(**user_data)
print(user.dict())