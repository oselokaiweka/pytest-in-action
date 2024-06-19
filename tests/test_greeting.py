import pytest

from src.greeting import my_name



def test_my_name():
    assert "My name is: bob" == my_name("bob")

def test_my_name2():
    assert "My name is: bob2" == my_name("bob2")



# Using @pytest.fixture decorators to provide test data
# Define fixture
@pytest.fixture
def my_name3_data():
    return "My name is: sally"

@pytest.fixture
def my_name4_data():
    return "My name is: sally2"

def test_my_name3(my_name3_data): # Pass fixture as arguement
    assert my_name3_data == my_name("sally")

def test_my_name4(my_name4_data):
    assert my_name4_data == my_name("sally2")



# Alternatively I can use one fixture to provide multiple testing data
# Define fixture
@pytest.fixture
def my_name5and6_data():
    return {
        "name5":"My name is: osey", 
        "name6":"My name is: osey2"
    }

def test_my_name5(my_name5and6_data): # Pass fixture as arguement
    assert my_name5and6_data["name5"] == my_name("osey")

def test_my_name6(my_name5and6_data):
    assert my_name5and6_data["name6"] == my_name("osey2")