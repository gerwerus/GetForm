from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def testGetForm(data: str) -> str:
    response = client.post("/get_form/",
                           headers={'accept': 'application/json'},
                           json={"input": data})
    return response.text
tests = [
    "email=a@a.ru&phone=+7 888 888 88 88&text=123abc",
    "electronicMail=a@a.r&phone=+7 913 234 22 11",
    "email=a@a.r&phone=+7 123 456 11 22&date=10.10.2010",
    "phoneNumber=+7 555 353 55 55&birthday=2000-12-20",
    "mail=a@a.ru&phone=7 888 888 88 88&text=assvz",
    "yourMail=lopus@a.ru",
    "currentDate=2002-20-12&text=testing text",
    "email=a@a.r&phoneNumber=+7 888 888 88 88&currentDate=2000-12-20",
    "email=ok@mail.ru&date=32.20.2003",
    "email=zzz@gmail.com",
    "email=aar&phone=+7 999 999 88 88&text=123",
    "date=2003-10-10&email=a@a.r",
    "email=b@bk.ru&phone=+7 125 323 11 66&text=fsdfe&date=2020-04-04",
    "phone=+7 888 888 88 88&text=123",
    "text=lopusingre23fd",        
]
for index, test in enumerate(tests):
    print(index + 1, testGetForm(test))