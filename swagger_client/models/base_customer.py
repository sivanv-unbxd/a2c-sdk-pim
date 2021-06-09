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


class BaseCustomer(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'phone': 'str',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'phone': 'phone',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, email=None, first_name=None, last_name=None, phone=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """BaseCustomer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this BaseCustomer.  # noqa: E501


        :return: The id of this BaseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseCustomer.


        :param id: The id of this BaseCustomer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this BaseCustomer.  # noqa: E501


        :return: The email of this BaseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BaseCustomer.


        :param email: The email of this BaseCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this BaseCustomer.  # noqa: E501


        :return: The first_name of this BaseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BaseCustomer.


        :param first_name: The first_name of this BaseCustomer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BaseCustomer.  # noqa: E501


        :return: The last_name of this BaseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BaseCustomer.


        :param last_name: The last_name of this BaseCustomer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this BaseCustomer.  # noqa: E501


        :return: The phone of this BaseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BaseCustomer.


        :param phone: The phone of this BaseCustomer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def additional_fields(self):
        """Gets the additional_fields of this BaseCustomer.  # noqa: E501


        :return: The additional_fields of this BaseCustomer.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this BaseCustomer.


        :param additional_fields: The additional_fields of this BaseCustomer.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this BaseCustomer.  # noqa: E501


        :return: The custom_fields of this BaseCustomer.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this BaseCustomer.


        :param custom_fields: The custom_fields of this BaseCustomer.  # noqa: E501
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
        if issubclass(BaseCustomer, dict):
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
        if not isinstance(other, BaseCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
