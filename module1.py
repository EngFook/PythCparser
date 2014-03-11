from mock import patch, Mock
import unittest

class MyClass():
    def my_method(self):
        pass


class SomeOtherClassThatUsesMyClass():
    def method_under_test(self):
        myclass = MyClass()
        return myclass.my_method()


def test_my_method_shouldReturnTrue_whenMyMethodReturnsSomeValue(self, mock_my_method):
    mock_my_method.return_value=True
    some_other_class =  SomeOtherClassThatUsesMyClass()
    result = some_other_class.method_under_test()
    self.assertTrue(result)

def test_my_method_shouldReturnMultipleValues_whenMyMethodReturnsSomeValue(self, mock_my_method):
    list_of_return_values= [True,False,False]
    def side_effect():
        return list_of_return_values.pop()
    mock_my_method.side_effect = side_effect
    some_other_class =  SomeOtherClassThatUsesMyClass()
    self.assertFalse(some_other_class.method_under_test())
    self.assertFalse(some_other_class.method_under_test())
    self.assertTrue(some_other_class.method_under_test())

def test_my_method_shouldReturnTrue_whenSomeOtherClassMethodIsCalledAndAReturnValueIsSet(self, mock_my_class):
    mc = mock_my_class.return_value
    mc.my_method.return_value = True
    some_other_class =  SomeOtherClassThatUsesMyClass()
    result = some_other_class.method_under_test()
    self.assertTrue(result)

if __name__=='__main__':
    unittest.main()
