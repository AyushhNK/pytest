import pytest 
import source.my_function as my_function


def test_add():
	result=my_function.add(number_one=1,number_two=4)
	assert result==5

def test_string():
	result=my_function.add("i like ","you")
	assert result=="i like you"

def test_divide():
	result=my_function.divide(number_one=4,number_two=2)
	assert result==2


def test_divide_by_zero():
	with pytest.raises(ZeroDivisionError):
		result=my_function.divide(number_one=4,number_two=0)
