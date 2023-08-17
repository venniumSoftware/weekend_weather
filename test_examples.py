# test_assert_examples.py

import weekend_api
import os
import coverage

# Start code coverage before importing other modules:
cov = coverage.Coverage()
cov.start()

API_KEY = os.environ['API_KEY']

import sys
sys.path.append(sys.path[0] + "/..")

def test_api():
    assert weekend_api.call_weather_api(API_KEY, 32259) != None
    
if __name__ == "__main__":
    test_api()
    print("Everything Passed")
    

cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')