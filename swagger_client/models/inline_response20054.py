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


class InlineResponse20054(object):
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
        'return_code': 'int',
        'return_message': 'str',
        'result': 'InlineResponse20054Result'
    }

    attribute_map = {
        'return_code': 'return_code',
        'return_message': 'return_message',
        'result': 'result'
    }

    def __init__(self, return_code=None, return_message=None, result=None):  # noqa: E501
        """InlineResponse20054 - a model defined in Swagger"""  # noqa: E501

        self._return_code = None
        self._return_message = None
        self._result = None
        self.discriminator = None

        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if result is not None:
            self.result = result

    @property
    def return_code(self):
        """Gets the return_code of this InlineResponse20054.  # noqa: E501


        :return: The return_code of this InlineResponse20054.  # noqa: E501
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this InlineResponse20054.


        :param return_code: The return_code of this InlineResponse20054.  # noqa: E501
        :type: int
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this InlineResponse20054.  # noqa: E501


        :return: The return_message of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this InlineResponse20054.


        :param return_message: The return_message of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def result(self):
        """Gets the result of this InlineResponse20054.  # noqa: E501


        :return: The result of this InlineResponse20054.  # noqa: E501
        :rtype: InlineResponse20054Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse20054.


        :param result: The result of this InlineResponse20054.  # noqa: E501
        :type: InlineResponse20054Result
        """

        self._result = result

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
        if issubclass(InlineResponse20054, dict):
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
        if not isinstance(other, InlineResponse20054):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
