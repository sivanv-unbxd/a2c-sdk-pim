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


class InlineResponse20013Result(object):
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
        'store_name': 'str',
        'store_url': 'str',
        'db_prefix': 'str'
    }

    attribute_map = {
        'store_name': 'store_name',
        'store_url': 'store_url',
        'db_prefix': 'db_prefix'
    }

    def __init__(self, store_name=None, store_url=None, db_prefix=None):  # noqa: E501
        """InlineResponse20013Result - a model defined in Swagger"""  # noqa: E501

        self._store_name = None
        self._store_url = None
        self._db_prefix = None
        self.discriminator = None

        if store_name is not None:
            self.store_name = store_name
        if store_url is not None:
            self.store_url = store_url
        if db_prefix is not None:
            self.db_prefix = db_prefix

    @property
    def store_name(self):
        """Gets the store_name of this InlineResponse20013Result.  # noqa: E501


        :return: The store_name of this InlineResponse20013Result.  # noqa: E501
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        """Sets the store_name of this InlineResponse20013Result.


        :param store_name: The store_name of this InlineResponse20013Result.  # noqa: E501
        :type: str
        """

        self._store_name = store_name

    @property
    def store_url(self):
        """Gets the store_url of this InlineResponse20013Result.  # noqa: E501


        :return: The store_url of this InlineResponse20013Result.  # noqa: E501
        :rtype: str
        """
        return self._store_url

    @store_url.setter
    def store_url(self, store_url):
        """Sets the store_url of this InlineResponse20013Result.


        :param store_url: The store_url of this InlineResponse20013Result.  # noqa: E501
        :type: str
        """

        self._store_url = store_url

    @property
    def db_prefix(self):
        """Gets the db_prefix of this InlineResponse20013Result.  # noqa: E501


        :return: The db_prefix of this InlineResponse20013Result.  # noqa: E501
        :rtype: str
        """
        return self._db_prefix

    @db_prefix.setter
    def db_prefix(self, db_prefix):
        """Sets the db_prefix of this InlineResponse20013Result.


        :param db_prefix: The db_prefix of this InlineResponse20013Result.  # noqa: E501
        :type: str
        """

        self._db_prefix = db_prefix

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
        if issubclass(InlineResponse20013Result, dict):
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
        if not isinstance(other, InlineResponse20013Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other