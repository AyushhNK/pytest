import pytest
import math
import source.my_class as my_class

class TestCircle:
	def setup_method(self,method):
		print(f'setting up {method}')
		self.circle=my_class.Circle(10)

	def teardown_method(self,method):
		print(f'tearing down {method}')
		del self.circle

	def test_area(self):
		assert self.circle.area()==math.pi*self.circle.radius**2

	def test_perimeter(self):
		assert self.circle.perimeter()==2*math.pi*self.circle.radius