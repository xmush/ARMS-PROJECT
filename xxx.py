from faker import Faker
import requests, random

fake = Faker()

url = "http://0.0.0.0:5000/user"


for i in range(100) :
    name = fake.name()
    pswd = name.replace(' ', '')
    status = random.choice(['true', 'false'])


    payload = "{\n\t\"name\" : \""+name+"\",\n\t\"password\" : \""+pswd+"\",\n\t\"status\" : "+status+"\n}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))