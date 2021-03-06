# coding: utf-8

"""
    Swagger API2Cart

    API2Cart  # noqa: E501

    OpenAPI spec version: 1.1
    Contact: contact@api2cart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.basket_api import BasketApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBasketApi(unittest.TestCase):
    """BasketApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.basket_api.BasketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_basket_info(self):
        """Test case for basket_info

        """
        pass

    def test_basket_item_add(self):
        """Test case for basket_item_add

        """
        pass

    def test_basket_live_shipping_service_create(self):
        """Test case for basket_live_shipping_service_create

        """
        pass

    def test_basket_live_shipping_service_delete(self):
        """Test case for basket_live_shipping_service_delete

        """
        pass

    def test_basket_live_shipping_service_list(self):
        """Test case for basket_live_shipping_service_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
