'''Документация API: https://restful-booker.herokuapp.com/apidoc/index.html
1. Воспроизвести все методы, рассмотренные на лекции
2. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
3. Проверить, что изменения применились
'''
import pytest
import requests

base_url ='https://restful-booker.herokuapp.com/booking/'
login_url ='https://restful-booker.herokuapp.com/auth'
healthcheck_url ='https://restful-booker.herokuapp.com/ping'
data_auth={
    "username":"admin",
    "password":"password123"
}
booking_data={
        "firstname": "Test1",
        "lastname": "Test2",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-02-02"
        },
        "additionalneeds": "Testing"
    }
def test_health_check():
    response= requests.get(healthcheck_url)
    code= response.status_code
    assert code==201

@pytest.fixture(scope='module')
def create_token():
    response=requests.post(login_url,json=data_auth)
    token=response.json()['token']
    yield token

@pytest.fixture()
def create_booking():
    response=requests.post(base_url,json=booking_data)
    booking_id=response.json()['bookingid']
    yield booking_id

def test_get_booking(create_booking):
    url = f'{base_url}{create_booking}'
    response=requests.get(url)
    print (url)
    code=response.status_code
    assert code==200
    assert response.json()==booking_data

def test_update_booking(create_booking,create_token):
    new_boooking_data = {
        "firstname": "Test2",
        "lastname": "Test3",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Lunch"
    }
    token = {"Cookie": f"token={create_token}"}
    response = requests.put(f'{base_url}{create_booking}', json=new_boooking_data, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f'{base_url}{create_booking}')
    response_2.json()== new_boooking_data


def test_delete_booking(create_booking, create_token):
    token = {"Cookie": f"token={create_token}"}
    response = requests.delete(f'{base_url}{create_booking}', headers=token)
    assert response.status_code == 201
    response_get = requests.get(f'{base_url}{create_booking}')
    assert response_get.status_code == 404



