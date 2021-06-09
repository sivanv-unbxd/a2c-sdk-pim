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


class CustomerAddress(object):
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
        'type': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'postcode': 'str',
        'address1': 'str',
        'address2': 'str',
        'phone': 'str',
        'city': 'str',
        'country': 'Country',
        'state': 'State',
        'company': 'str',
        'fax': 'str',
        'website': 'str',
        'gender': 'str',
        'region': 'str',
        'default': 'bool',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'postcode': 'postcode',
        'address1': 'address1',
        'address2': 'address2',
        'phone': 'phone',
        'city': 'city',
        'country': 'country',
        'state': 'state',
        'company': 'company',
        'fax': 'fax',
        'website': 'website',
        'gender': 'gender',
        'region': 'region',
        'default': 'default',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, type=None, first_name=None, last_name=None, postcode=None, address1=None, address2=None, phone=None, city=None, country=None, state=None, company=None, fax=None, website=None, gender=None, region=None, default=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """CustomerAddress - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._first_name = None
        self._last_name = None
        self._postcode = None
        self._address1 = None
        self._address2 = None
        self._phone = None
        self._city = None
        self._country = None
        self._state = None
        self._company = None
        self._fax = None
        self._website = None
        self._gender = None
        self._region = None
        self._default = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if postcode is not None:
            self.postcode = postcode
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if phone is not None:
            self.phone = phone
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if company is not None:
            self.company = company
        if fax is not None:
            self.fax = fax
        if website is not None:
            self.website = website
        if gender is not None:
            self.gender = gender
        if region is not None:
            self.region = region
        if default is not None:
            self.default = default
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this CustomerAddress.  # noqa: E501


        :return: The id of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerAddress.


        :param id: The id of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this CustomerAddress.  # noqa: E501


        :return: The type of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomerAddress.


        :param type: The type of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def first_name(self):
        """Gets the first_name of this CustomerAddress.  # noqa: E501


        :return: The first_name of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CustomerAddress.


        :param first_name: The first_name of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CustomerAddress.  # noqa: E501


        :return: The last_name of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CustomerAddress.


        :param last_name: The last_name of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def postcode(self):
        """Gets the postcode of this CustomerAddress.  # noqa: E501


        :return: The postcode of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this CustomerAddress.


        :param postcode: The postcode of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def address1(self):
        """Gets the address1 of this CustomerAddress.  # noqa: E501


        :return: The address1 of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this CustomerAddress.


        :param address1: The address1 of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this CustomerAddress.  # noqa: E501


        :return: The address2 of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this CustomerAddress.


        :param address2: The address2 of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def phone(self):
        """Gets the phone of this CustomerAddress.  # noqa: E501


        :return: The phone of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerAddress.


        :param phone: The phone of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def city(self):
        """Gets the city of this CustomerAddress.  # noqa: E501


        :return: The city of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerAddress.


        :param city: The city of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this CustomerAddress.  # noqa: E501


        :return: The country of this CustomerAddress.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerAddress.


        :param country: The country of this CustomerAddress.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this CustomerAddress.  # noqa: E501


        :return: The state of this CustomerAddress.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CustomerAddress.


        :param state: The state of this CustomerAddress.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def company(self):
        """Gets the company of this CustomerAddress.  # noqa: E501


        :return: The company of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CustomerAddress.


        :param company: The company of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def fax(self):
        """Gets the fax of this CustomerAddress.  # noqa: E501


        :return: The fax of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this CustomerAddress.


        :param fax: The fax of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def website(self):
        """Gets the website of this CustomerAddress.  # noqa: E501


        :return: The website of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this CustomerAddress.


        :param website: The website of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def gender(self):
        """Gets the gender of this CustomerAddress.  # noqa: E501


        :return: The gender of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this CustomerAddress.


        :param gender: The gender of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def region(self):
        """Gets the region of this CustomerAddress.  # noqa: E501


        :return: The region of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CustomerAddress.


        :param region: The region of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def default(self):
        """Gets the default of this CustomerAddress.  # noqa: E501


        :return: The default of this CustomerAddress.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CustomerAddress.


        :param default: The default of this CustomerAddress.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def additional_fields(self):
        """Gets the additional_fields of this CustomerAddress.  # noqa: E501


        :return: The additional_fields of this CustomerAddress.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this CustomerAddress.


        :param additional_fields: The additional_fields of this CustomerAddress.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CustomerAddress.  # noqa: E501


        :return: The custom_fields of this CustomerAddress.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CustomerAddress.


        :param custom_fields: The custom_fields of this CustomerAddress.  # noqa: E501
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
        if issubclass(CustomerAddress, dict):
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
        if not isinstance(other, CustomerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other