import math_func
import pytest

@pytest.mark.number
def test_add():
    assert math_func.add(7,3,) == 10
    assert math_func.add(5,5) == 10

@pytest.mark.number
def test_product():
    assert math_func.product(2,2) == 4
    assert math_func.product(7) == 14


@pytest.mark.strings
def test_add_string():
    result = math_func.add('hello' , 'world')
    assert result == 'hello world'
    assert type(result) is str       

  


