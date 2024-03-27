import requests

def to_sum(valyuta):
    url = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{valyuta}/'
    nat = requests.get(url)
    javob = nat.json()[0]['Rate']
    return f"1 {valyuta} - <code><b>{javob}</b> SUM</code>"

