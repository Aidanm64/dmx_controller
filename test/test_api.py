import requests
import time

url = "http://raspberrypi.local:8000/api"


def test_get_all():
    r = requests.get(f"{url}/all")

    assert r.status_code == 200
    print(r.json())
    assert r.json()['name'] == "test_universe"


def test_all_color():
    requests.put(f"{url}/all/color/Red")
    time.sleep(1)
    requests.put(f"{url}/all/color/Blue")
    time.sleep(1)
    requests.put(f"{url}/all/color/Black")


def test_all_intensity():
    requests.put(f"{url}/all/color/Red")
    time.sleep(1)
    requests.put(f"{url}/all/intensity/128")
    time.sleep(1)
    requests.put(f"{url}/all/intensity/255")


def test_fixtures_state():

    body = {
        "strip_1_1": {
            "color": [100, 100, 100]
        },
        "strip_1_2": {
            "color": [200, 200, 200]
        },
        "strip_1_3": {
            "color": [0, 255, 128],
            "ms": 5000
        }
    }

    r = requests.put(f"{url}/all/state", json=body)
    assert r.status_code == 200


def test_configure_fixture():
    r = requests.put(f"{url}/fixtures/strip_1_1/intensity/255")
    assert r.status_code == 200

    r = requests.put(f"{url}/fixtures/strip_1_2/color?r=100&g=250&b=150")
    assert r.status_code == 200

    time.sleep(1)
    r = requests.get(f"{url}/fixtures/strip_1_1")
    assert r.status_code == 200
