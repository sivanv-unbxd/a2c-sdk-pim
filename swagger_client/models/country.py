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


class Country(object):
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
        'code2': 'str',
        'code3': 'str',
        'name': 'str',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'code2': 'code2',
        'code3': 'code3',
        'name': 'name',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, code2=None, code3=None, name=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Country - a model defined in Swagger"""  # noqa: E501

        self._code2 = None
        self._code3 = None
        self._name = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if code2 is not None:
            self.code2 = code2
        if code3 is not None:
            self.code3 = code3
        if name is not None:
            self.name = name
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def code2(self):
        """Gets the code2 of this Country.  # noqa: E501


        :return: The code2 of this Country.  # noqa: E501
        :rtype: str
        """
        return self._code2

    @code2.setter
    def code2(self, code2):
        """Sets the code2 of this Country.


        :param code2: The code2 of this Country.  # noqa: E501
        :type: str
        """

        self._code2 = code2

    @property
    def code3(self):
        """Gets the code3 of this Country.  # noqa: E501


        :return: The code3 of this Country.  # noqa: E501
        :rtype: str
        """
        return self._code3

    @code3.setter
    def code3(self, code3):
        """Sets the code3 of this Country.


        :param code3: The code3 of this Country.  # noqa: E501
        :type: str
        """

        self._code3 = code3

    @property
    def name(self):
        """Gets the name of this Country.  # noqa: E501


        :return: The name of this Country.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Country.


        :param name: The name of this Country.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Country.  # noqa: E501


        :return: The additional_fields of this Country.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Country.


        :param additional_fields: The additional_fields of this Country.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Country.  # noqa: E501


        :return: The custom_fields of this Country.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Country.


        :param custom_fields: The custom_fields of this Country.  # noqa: E501
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
        if issubclass(Country, dict):
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
        if not isinstance(other, Country):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
