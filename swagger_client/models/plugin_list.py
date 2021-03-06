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


class PluginList(object):
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
        'all_plugins': 'int',
        'plugins': 'list[Plugin]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'all_plugins': 'all_plugins',
        'plugins': 'plugins',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, all_plugins=None, plugins=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """PluginList - a model defined in Swagger"""  # noqa: E501

        self._all_plugins = None
        self._plugins = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if all_plugins is not None:
            self.all_plugins = all_plugins
        if plugins is not None:
            self.plugins = plugins
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def all_plugins(self):
        """Gets the all_plugins of this PluginList.  # noqa: E501


        :return: The all_plugins of this PluginList.  # noqa: E501
        :rtype: int
        """
        return self._all_plugins

    @all_plugins.setter
    def all_plugins(self, all_plugins):
        """Sets the all_plugins of this PluginList.


        :param all_plugins: The all_plugins of this PluginList.  # noqa: E501
        :type: int
        """

        self._all_plugins = all_plugins

    @property
    def plugins(self):
        """Gets the plugins of this PluginList.  # noqa: E501


        :return: The plugins of this PluginList.  # noqa: E501
        :rtype: list[Plugin]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this PluginList.


        :param plugins: The plugins of this PluginList.  # noqa: E501
        :type: list[Plugin]
        """

        self._plugins = plugins

    @property
    def additional_fields(self):
        """Gets the additional_fields of this PluginList.  # noqa: E501


        :return: The additional_fields of this PluginList.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this PluginList.


        :param additional_fields: The additional_fields of this PluginList.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this PluginList.  # noqa: E501


        :return: The custom_fields of this PluginList.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this PluginList.


        :param custom_fields: The custom_fields of this PluginList.  # noqa: E501
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
        if issubclass(PluginList, dict):
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
        if not isinstance(other, PluginList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
