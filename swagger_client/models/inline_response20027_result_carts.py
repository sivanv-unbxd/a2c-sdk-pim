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


class InlineResponse20027ResultCarts(object):
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
        'url': 'str',
        'store_key': 'str',
        'cart_id': 'str',
        'total_calls': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'store_key': 'store_key',
        'cart_id': 'cart_id',
        'total_calls': 'total_calls'
    }

    def __init__(self, id=None, url=None, store_key=None, cart_id=None, total_calls=None):  # noqa: E501
        """InlineResponse20027ResultCarts - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._store_key = None
        self._cart_id = None
        self._total_calls = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if store_key is not None:
            self.store_key = store_key
        if cart_id is not None:
            self.cart_id = cart_id
        if total_calls is not None:
            self.total_calls = total_calls

    @property
    def id(self):
        """Gets the id of this InlineResponse20027ResultCarts.  # noqa: E501


        :return: The id of this InlineResponse20027ResultCarts.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20027ResultCarts.


        :param id: The id of this InlineResponse20027ResultCarts.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this InlineResponse20027ResultCarts.  # noqa: E501


        :return: The url of this InlineResponse20027ResultCarts.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20027ResultCarts.


        :param url: The url of this InlineResponse20027ResultCarts.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def store_key(self):
        """Gets the store_key of this InlineResponse20027ResultCarts.  # noqa: E501


        :return: The store_key of this InlineResponse20027ResultCarts.  # noqa: E501
        :rtype: str
        """
        return self._store_key

    @store_key.setter
    def store_key(self, store_key):
        """Sets the store_key of this InlineResponse20027ResultCarts.


        :param store_key: The store_key of this InlineResponse20027ResultCarts.  # noqa: E501
        :type: str
        """

        self._store_key = store_key

    @property
    def cart_id(self):
        """Gets the cart_id of this InlineResponse20027ResultCarts.  # noqa: E501


        :return: The cart_id of this InlineResponse20027ResultCarts.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this InlineResponse20027ResultCarts.


        :param cart_id: The cart_id of this InlineResponse20027ResultCarts.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def total_calls(self):
        """Gets the total_calls of this InlineResponse20027ResultCarts.  # noqa: E501


        :return: The total_calls of this InlineResponse20027ResultCarts.  # noqa: E501
        :rtype: str
        """
        return self._total_calls

    @total_calls.setter
    def total_calls(self, total_calls):
        """Sets the total_calls of this InlineResponse20027ResultCarts.


        :param total_calls: The total_calls of this InlineResponse20027ResultCarts.  # noqa: E501
        :type: str
        """

        self._total_calls = total_calls

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
        if issubclass(InlineResponse20027ResultCarts, dict):
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
        if not isinstance(other, InlineResponse20027ResultCarts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
