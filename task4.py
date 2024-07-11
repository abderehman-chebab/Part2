import unittest

from unittest.mock import Mock

from cache_decorator import CacheDecorator


class TestCacheDecorator(unittest.TestCase):

    def test_cache_decorator_basic_functionality(self):
        mock_function = Mock(return_value=42)
        cached_function = CacheDecorator()(mock_function)

        result1 = cached_function(1, 2)  # First call: should calculate
        result2 = cached_function(1, 2)  # Second call: should use cache

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_function.assert_called_once()  # Ensure function called only once

    def test_cache_decorator_different_arguments(self):
        mock_function = Mock(side_effect=[10, 20])
        cached_function = CacheDecorator()(mock_function)

        result1 = cached_function("a")
        result2 = cached_function("b")

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 20)
        self.assertEqual(mock_function.call_count, 2)  # Should call twice

    def test_cache_decorator_with_kwargs(self):
        mock_function = Mock(return_value="hello")
        cached_function = CacheDecorator()(mock_function)

        result1 = cached_function(name="Alice")
        result2 = cached_function(name="Bob")

        self.assertEqual(result1, "hello")  # This should fail
        self.assertEqual(result2, "hello")  # This should fail
        self.assertEqual(mock_function.call_count, 1)  # Expected behavior

    def test_cache_decorator_with_multiple_args(self):
        mock_function = Mock(return_value=30)
        cached_function = CacheDecorator()(mock_function)

        result1 = cached_function(1, 2, 3)
        result2 = cached_function(1, 2, 3)

        self.assertEqual(result1, 30)
        self.assertEqual(result2, 30)
        mock_function.assert_called_once()

    def test_cache_decorator_multiple_decorators_same_function(self):
        mock_function = Mock(return_value=77)
        decorator1 = CacheDecorator()
        decorator2 = CacheDecorator()

        cached_function1 = decorator1(mock_function)
        cached_function2 = decorator2(mock_function)

        result1 = cached_function1(4)
        result2 = cached_function2(4)

        self.assertEqual(result1, 77)
        self.assertEqual(result2, 77)
        self.assertEqual(mock_function.call_count, 1)  # Should be called once


if __name__ == '__main__':
    unittest.main()

