import requests
import time

url = "http://raspberrypi.local:8000"


def test_global_color():
    requests.put(f"{url}/global/color/Red")
    time.sleep(1)
    requests.put(f"{url}/global/color/Blue")
    time.sleep(1)
    requests.put(f"{url}/global/color/Black")


def test_global_intensity():
    requests.put(f"{url}/global/color/Red")
    time.sleep(1)
    requests.put(f"{url}/global/intensity/128")
    time.sleep(1)
    requests.put(f"{url}/global/intensity/255")