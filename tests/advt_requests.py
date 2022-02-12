import requests
import base64

resp = requests.get('http://127.0.0.1:5000/advts/1').json()
print(resp)

#
resp = requests.post('http://127.0.0.1:5000/advts/',

                     auth=('test1502', 'sgdsppo34FET323211'),

                     json={
                         'title': 'hello',
                         'text': "world"
                     }).json()
print(resp)

resp = requests.delete('http://127.0.0.1:5000/advts/1',
                       auth=('test1502', 'sgdsppo34FET323211'),
                       ).json()
print(resp)


resp = requests.patch('http://127.0.0.1:5000/advts/1',
                        auth=('test1502', 'sgdsppo34FET323211'),
                        json={
                            'title': 'hellooooooo',
                        }).json()
print(resp)