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


class OrderStatus(object):
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
        'name': 'str',
        'history': 'list[OrderStatusHistoryItem]',
        'refund_info': 'OrderStatusRefund',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'history': 'history',
        'refund_info': 'refund_info',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, name=None, history=None, refund_info=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """OrderStatus - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._history = None
        self._refund_info = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if history is not None:
            self.history = history
        if refund_info is not None:
            self.refund_info = refund_info
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this OrderStatus.  # noqa: E501


        :return: The id of this OrderStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderStatus.


        :param id: The id of this OrderStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrderStatus.  # noqa: E501


        :return: The name of this OrderStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrderStatus.


        :param name: The name of this OrderStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def history(self):
        """Gets the history of this OrderStatus.  # noqa: E501


        :return: The history of this OrderStatus.  # noqa: E501
        :rtype: list[OrderStatusHistoryItem]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this OrderStatus.


        :param history: The history of this OrderStatus.  # noqa: E501
        :type: list[OrderStatusHistoryItem]
        """

        self._history = history

    @property
    def refund_info(self):
        """Gets the refund_info of this OrderStatus.  # noqa: E501


        :return: The refund_info of this OrderStatus.  # noqa: E501
        :rtype: OrderStatusRefund
        """
        return self._refund_info

    @refund_info.setter
    def refund_info(self, refund_info):
        """Sets the refund_info of this OrderStatus.


        :param refund_info: The refund_info of this OrderStatus.  # noqa: E501
        :type: OrderStatusRefund
        """

        self._refund_info = refund_info

    @property
    def additional_fields(self):
        """Gets the additional_fields of this OrderStatus.  # noqa: E501


        :return: The additional_fields of this OrderStatus.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this OrderStatus.


        :param additional_fields: The additional_fields of this OrderStatus.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderStatus.  # noqa: E501


        :return: The custom_fields of this OrderStatus.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderStatus.


        :param custom_fields: The custom_fields of this OrderStatus.  # noqa: E501
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
        if issubclass(OrderStatus, dict):
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
        if not isinstance(other, OrderStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
