# test_assert_examples.py
import os, sys
import pytest
from ..weekend_api import weekend_api


API_KEY = os.environ['API_KEY']

def test_api():
    assert weekend_api.call_weather_api(API_KEY, 32259) != None
    
if __name__ == "__main__":
    test_api()
    print("Everything Passed")
    