import requests

domain = 'https://a3e1b004a2d9bad3eb9d5e0d76494caf.ctf.hacker101.com'
for i in range(5):
    r = requests.post(
            domain + '/page/edit/' + str(i)
        )

    print(i)
    print(r.headers)
    print(r.text)