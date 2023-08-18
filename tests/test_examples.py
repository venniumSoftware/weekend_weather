# test_assert_examples.py
import os, sys
import pytest


from setuptools import setup, find_packages
setup(
    name = 'weekend_api',
    packages = find_packages(),
)


API_KEY = os.environ['API_KEY']

def test_api():
    assert weekend_api.call_weather_api(API_KEY, 32259) != None
    
if __name__ == "__main__":
    test_api()
    print("Everything Passed")
    