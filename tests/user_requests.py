import requests


# resp = requests.get('http://127.0.0.1:5000/health').json()
# print(resp)


resp = requests.get('http://127.0.0.1:5000/users/1').json()
print(resp)

#
resp = requests.post('http://127.0.0.1:5000/users/',
                     json={
                         'username': 'test1',
                         'password': 'sgdsppo34FET32321',
                         'email': 'test@test.test'
                     }).json()
print(resp)

resp = requests.delete('http://127.0.0.1:5000/users/2').json()
print(resp)


resp = requests.patch('http://127.0.0.1:5000/users/1', json={
                         'username': 'test1502',
                         'password': 'sgdsppo34FET32321',
                         'email': 'test@test.test'
                     }).json()
print(resp)