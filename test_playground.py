'''Документация API: https://restful-booker.herokuapp.com/apidoc/index.html
1. Воспроизвести все методы, рассмотренные на лекции
2. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
3. Проверить, что изменения применились
Также вы можете тренироваться на следующих сайтах:
https://jsonplaceholder.typicode.com
https://playground.learnqa.ru/api/map '''
import random
import pytest
import requests

base_url='https://playground.learnqa.ru/api/user/'
login_url='https://playground.learnqa.ru/api/user/login'
email='test1@test1.com'
password='password'

@pytest.fixture(scope='module')
def create_user():
    data_json={'username' : 'Testing3',
    'firstName' : 'Test12',
    'lastName' : 'Test123',
    'email' : email,
    'password' : password
    }
    response= requests.post(base_url,data_json)
    user_id= response.json()['id']
    print(user_id)
    yield user_id


@pytest.fixture(scope='module')
def login():
    data_login={
        'email': email,
        'password': password
    }
    response = requests.post(login_url,data_login)
    cook=response.cookies.get('auth_sid')
    tok=response.headers.get('x-csrf-token')
    id_data=requests.get('https://playground.learnqa.ru/api/user/auth',
                         cookies={'auth_sid':cook},
                         headers={'x-csrf-token':tok,'Set-Cookie':f"auth_sid={cook}"})
    print(id_data.json())
    yield {'auth_sid':cook},{'x-csrf-token':tok,'Set-Cookie':f"auth_sid={cook}"}

def test_update_user(create_user,login):
    name='Test'+str(random.randint(0,100))
    params={
        'username': name
    }
    url = f'{base_url}{create_user}'
    response=requests.put(url,data=params,cookies=login[0], headers=login[1])
    response_data=response.json()
    assert response.status_code==200
    assert response_data['success']=='!'
    assert requests.get(url).json()['username']==name

def test_delete_user(login,create_user):
    url = f'{base_url}{create_user}'
    response = requests.delete(url, cookies=login[0], headers=login[1])
    assert response.status_code==200
    assert requests.get(url).status_code==404





