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


class Info(object):
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
        'owner': 'str',
        'country': 'str',
        'state': 'str',
        'state_code': 'str',
        'city': 'str',
        'street_address': 'str',
        'street_address_line_2': 'str',
        'zip_code': 'str',
        'email': 'str',
        'phone': 'str',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'owner': 'owner',
        'country': 'country',
        'state': 'state',
        'state_code': 'state_code',
        'city': 'city',
        'street_address': 'street_address',
        'street_address_line_2': 'street_address_line_2',
        'zip_code': 'zip_code',
        'email': 'email',
        'phone': 'phone',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, owner=None, country=None, state=None, state_code=None, city=None, street_address=None, street_address_line_2=None, zip_code=None, email=None, phone=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Info - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._country = None
        self._state = None
        self._state_code = None
        self._city = None
        self._street_address = None
        self._street_address_line_2 = None
        self._zip_code = None
        self._email = None
        self._phone = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if state_code is not None:
            self.state_code = state_code
        if city is not None:
            self.city = city
        if street_address is not None:
            self.street_address = street_address
        if street_address_line_2 is not None:
            self.street_address_line_2 = street_address_line_2
        if zip_code is not None:
            self.zip_code = zip_code
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def owner(self):
        """Gets the owner of this Info.  # noqa: E501


        :return: The owner of this Info.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Info.


        :param owner: The owner of this Info.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def country(self):
        """Gets the country of this Info.  # noqa: E501


        :return: The country of this Info.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Info.


        :param country: The country of this Info.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this Info.  # noqa: E501


        :return: The state of this Info.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Info.


        :param state: The state of this Info.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def state_code(self):
        """Gets the state_code of this Info.  # noqa: E501


        :return: The state_code of this Info.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this Info.


        :param state_code: The state_code of this Info.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def city(self):
        """Gets the city of this Info.  # noqa: E501


        :return: The city of this Info.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Info.


        :param city: The city of this Info.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def street_address(self):
        """Gets the street_address of this Info.  # noqa: E501


        :return: The street_address of this Info.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this Info.


        :param street_address: The street_address of this Info.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def street_address_line_2(self):
        """Gets the street_address_line_2 of this Info.  # noqa: E501


        :return: The street_address_line_2 of this Info.  # noqa: E501
        :rtype: str
        """
        return self._street_address_line_2

    @street_address_line_2.setter
    def street_address_line_2(self, street_address_line_2):
        """Sets the street_address_line_2 of this Info.


        :param street_address_line_2: The street_address_line_2 of this Info.  # noqa: E501
        :type: str
        """

        self._street_address_line_2 = street_address_line_2

    @property
    def zip_code(self):
        """Gets the zip_code of this Info.  # noqa: E501


        :return: The zip_code of this Info.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Info.


        :param zip_code: The zip_code of this Info.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def email(self):
        """Gets the email of this Info.  # noqa: E501


        :return: The email of this Info.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Info.


        :param email: The email of this Info.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Info.  # noqa: E501


        :return: The phone of this Info.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Info.


        :param phone: The phone of this Info.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Info.  # noqa: E501


        :return: The additional_fields of this Info.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Info.


        :param additional_fields: The additional_fields of this Info.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Info.  # noqa: E501


        :return: The custom_fields of this Info.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Info.


        :param custom_fields: The custom_fields of this Info.  # noqa: E501
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
        if issubclass(Info, dict):
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
        if not isinstance(other, Info):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
