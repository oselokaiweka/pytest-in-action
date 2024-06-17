from src.greeting import my_name

def test_my_name():
    assert "My name is: bob" == my_name("bob")

def test_my_name2():
    assert "My name is: bob2" == my_name("bob2")

def test_my_name3():
    assert "My name is: bob3" == my_name("bob3")

def test_my_name4():
    assert "My name is: bob4" == my_name("bob4")