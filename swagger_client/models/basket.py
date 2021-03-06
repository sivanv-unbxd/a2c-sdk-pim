# coding: utf-8

"""
    Swagger API2Cart

    API2Cart  # noqa: E501

    OpenAPI spec version: 1.1
    Contact: contact@api2cart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Basket(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'customer': 'BaseCustomer',
        'basket_url': 'str',
        'created_at': 'A2CDateTime',
        'modified_at': 'A2CDateTime',
        'currency': 'Currency',
        'basket_products': 'list[BasketItem]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'customer': 'customer',
        'basket_url': 'basket_url',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'currency': 'currency',
        'basket_products': 'basket_products',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, customer=None, basket_url=None, created_at=None, modified_at=None, currency=None, basket_products=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Basket - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._customer = None
        self._basket_url = None
        self._created_at = None
        self._modified_at = None
        self._currency = None
        self._basket_products = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if customer is not None:
            self.customer = customer
        if basket_url is not None:
            self.basket_url = basket_url
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if currency is not None:
            self.currency = currency
        if basket_products is not None:
            self.basket_products = basket_products
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Basket.  # noqa: E501


        :return: The id of this Basket.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Basket.


        :param id: The id of this Basket.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this Basket.  # noqa: E501


        :return: The customer of this Basket.  # noqa: E501
        :rtype: BaseCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Basket.


        :param customer: The customer of this Basket.  # noqa: E501
        :type: BaseCustomer
        """

        self._customer = customer

    @property
    def basket_url(self):
        """Gets the basket_url of this Basket.  # noqa: E501


        :return: The basket_url of this Basket.  # noqa: E501
        :rtype: str
        """
        return self._basket_url

    @basket_url.setter
    def basket_url(self, basket_url):
        """Sets the basket_url of this Basket.


        :param basket_url: The basket_url of this Basket.  # noqa: E501
        :type: str
        """

        self._basket_url = basket_url

    @property
    def created_at(self):
        """Gets the created_at of this Basket.  # noqa: E501


        :return: The created_at of this Basket.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Basket.


        :param created_at: The created_at of this Basket.  # noqa: E501
        :type: A2CDateTime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Basket.  # noqa: E501


        :return: The modified_at of this Basket.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Basket.


        :param modified_at: The modified_at of this Basket.  # noqa: E501
        :type: A2CDateTime
        """

        self._modified_at = modified_at

    @property
    def currency(self):
        """Gets the currency of this Basket.  # noqa: E501


        :return: The currency of this Basket.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Basket.


        :param currency: The currency of this Basket.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def basket_products(self):
        """Gets the basket_products of this Basket.  # noqa: E501


        :return: The basket_products of this Basket.  # noqa: E501
        :rtype: list[BasketItem]
        """
        return self._basket_products

    @basket_products.setter
    def basket_products(self, basket_products):
        """Sets the basket_products of this Basket.


        :param basket_products: The basket_products of this Basket.  # noqa: E501
        :type: list[BasketItem]
        """

        self._basket_products = basket_products

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Basket.  # noqa: E501


        :return: The additional_fields of this Basket.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Basket.


        :param additional_fields: The additional_fields of this Basket.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Basket.  # noqa: E501


        :return: The custom_fields of this Basket.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Basket.


        :param custom_fields: The custom_fields of this Basket.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Basket, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Basket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
