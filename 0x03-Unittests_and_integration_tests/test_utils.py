#!/usr/bin/env python3
""" Parameterize a unit test
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for utils.access_nested_map"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Test access_nested_map method.
        
        Args:
            nested_map (Mapping): The dictionary to traverse.
            path (Sequence): Keys to access nested dictionary.
            expected (Any): Expected value at the given path.
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access_nested_map raises KeyError for invalid path.
        
        Args:
            nested_map (Mapping): Dictionary to traverse.
            path (Sequence): Keys that should raise a KeyError.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function, mocking HTTP requests."""
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_requests_get: unittest.mock.Mock) -> None:
        """Test get_json with mock HTTP response.
        
        Args:
            test_url (str): URL to send request to.
            test_payload (dict): Expected JSON response.
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""
    
    def test_memoize(self) -> None:
        """Test that the memoize decorator caches the result of a_method."""
        
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock_object:
            test = TestClass()
            test.a_property
            test.a_property
            mock_object.assert_called_once()
