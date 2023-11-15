from datetime import datetime
import re
from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from tinydb import TinyDB, Query
db = TinyDB('./db/db.json')

class EmailModel(BaseModel):
    email: EmailStr

class PhoneNumberModel(BaseModel):
    phoneNumber: str
    @field_validator('phoneNumber')
    def phoneFormat(cls, p: str) -> str:
        if not bool(re.fullmatch(r'[+]7 \d{3} \d{3} \d{2} \d{2}', p)):
            raise ValueError('value is not valid phone number. The phone number must be like +7 xxx xxx xx xx')
        return p
    
class DateModel(BaseModel):
    date: str
    @field_validator('date')
    def dateFormat(cls, p: str) -> str:
        try:
            assert datetime.strptime(p, '%Y-%m-%d')
        except:
            assert datetime.strptime(p, '%d.%m.%Y')
        return p

class InputModel(BaseModel):
    input: str

def search(dictionary: dict) -> dict:
    fields = list(dictionary.keys())
    values = list(dictionary.values())
    query = Query()[fields.pop(0)].one_of(values)
    for field in fields:
        query = query & Query()[field].one_of(values)
    result = db.search(query)
    return {'name': result[0]['name']} if result else dictionary

def getAnswer(dictionary: dict) -> dict:
    answer = dict()
    for key in dictionary:
        try:
            EmailModel.model_validate({'email': dictionary[key]})
            answer[key] = 'email'
        except:
            try:
                PhoneNumberModel.model_validate({'phoneNumber': dictionary[key]})
                answer[key] = 'phone'
            except:
                try:
                    DateModel.model_validate({'date': dictionary[key]})
                    answer[key] = 'date'
                except:
                    answer[key] = 'text'
    return search(answer)



