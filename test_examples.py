# test_assert_examples.py

import weekend_api

def test_api():
    assert weekend_api.call_weather_api() != None
    
if __name__ == "__main__":
    test_api()
    print("Everything Passed")