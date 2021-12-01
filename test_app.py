import requests
import pytest
import time

def test_connection():
    assert requests.get("http://localhost:5000").status_code == 200 , "web site is not up"


def test_site():
    assert float(requests.get("http://localhost:5000/mean_get?q=1,2,3").content) == 2.0 , "error of the mean function"


def test_stress_requests():

    start = time.time()
    for i in range(1000):
        requests.get("http://localhost:5000")

    end = time.time()-start
    assert (end/1000) < 100 ,"stress not passed"

