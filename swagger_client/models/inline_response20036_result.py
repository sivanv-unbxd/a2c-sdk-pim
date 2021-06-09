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


class InlineResponse20036Result(object):
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
        'delete_items': 'int'
    }

    attribute_map = {
        'delete_items': 'delete_items'
    }

    def __init__(self, delete_items=None):  # noqa: E501
        """InlineResponse20036Result - a model defined in Swagger"""  # noqa: E501

        self._delete_items = None
        self.discriminator = None

        if delete_items is not None:
            self.delete_items = delete_items

    @property
    def delete_items(self):
        """Gets the delete_items of this InlineResponse20036Result.  # noqa: E501


        :return: The delete_items of this InlineResponse20036Result.  # noqa: E501
        :rtype: int
        """
        return self._delete_items

    @delete_items.setter
    def delete_items(self, delete_items):
        """Sets the delete_items of this InlineResponse20036Result.


        :param delete_items: The delete_items of this InlineResponse20036Result.  # noqa: E501
        :type: int
        """

        self._delete_items = delete_items

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
        if issubclass(InlineResponse20036Result, dict):
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
        if not isinstance(other, InlineResponse20036Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other