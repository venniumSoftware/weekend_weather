# test_assert_examples.py

import weekend_api

def test_uppercase():
    assert weekend_api.call_weather_api() != None