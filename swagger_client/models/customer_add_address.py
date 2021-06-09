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


class CustomerAddAddress(object):
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
        'address_book_type': 'str',
        'address_book_first_name': 'str',
        'address_book_last_name': 'str',
        'address_book_company': 'str',
        'address_book_fax': 'str',
        'address_book_phone': 'str',
        'address_book_website': 'str',
        'address_book_address1': 'str',
        'address_book_address2': 'str',
        'address_book_city': 'str',
        'address_book_country': 'str',
        'address_book_state': 'str',
        'address_book_postcode': 'str',
        'address_book_gender': 'str',
        'address_book_region': 'str',
        'address_book_default': 'bool'
    }

    attribute_map = {
        'address_book_type': 'address_book_type',
        'address_book_first_name': 'address_book_first_name',
        'address_book_last_name': 'address_book_last_name',
        'address_book_company': 'address_book_company',
        'address_book_fax': 'address_book_fax',
        'address_book_phone': 'address_book_phone',
        'address_book_website': 'address_book_website',
        'address_book_address1': 'address_book_address1',
        'address_book_address2': 'address_book_address2',
        'address_book_city': 'address_book_city',
        'address_book_country': 'address_book_country',
        'address_book_state': 'address_book_state',
        'address_book_postcode': 'address_book_postcode',
        'address_book_gender': 'address_book_gender',
        'address_book_region': 'address_book_region',
        'address_book_default': 'address_book_default'
    }

    def __init__(self, address_book_type=None, address_book_first_name=None, address_book_last_name=None, address_book_company=None, address_book_fax=None, address_book_phone=None, address_book_website=None, address_book_address1=None, address_book_address2=None, address_book_city=None, address_book_country=None, address_book_state=None, address_book_postcode=None, address_book_gender=None, address_book_region=None, address_book_default=None):  # noqa: E501
        """CustomerAddAddress - a model defined in Swagger"""  # noqa: E501

        self._address_book_type = None
        self._address_book_first_name = None
        self._address_book_last_name = None
        self._address_book_company = None
        self._address_book_fax = None
        self._address_book_phone = None
        self._address_book_website = None
        self._address_book_address1 = None
        self._address_book_address2 = None
        self._address_book_city = None
        self._address_book_country = None
        self._address_book_state = None
        self._address_book_postcode = None
        self._address_book_gender = None
        self._address_book_region = None
        self._address_book_default = None
        self.discriminator = None

        if address_book_type is not None:
            self.address_book_type = address_book_type
        if address_book_first_name is not None:
            self.address_book_first_name = address_book_first_name
        if address_book_last_name is not None:
            self.address_book_last_name = address_book_last_name
        if address_book_company is not None:
            self.address_book_company = address_book_company
        if address_book_fax is not None:
            self.address_book_fax = address_book_fax
        if address_book_phone is not None:
            self.address_book_phone = address_book_phone
        if address_book_website is not None:
            self.address_book_website = address_book_website
        if address_book_address1 is not None:
            self.address_book_address1 = address_book_address1
        if address_book_address2 is not None:
            self.address_book_address2 = address_book_address2
        if address_book_city is not None:
            self.address_book_city = address_book_city
        if address_book_country is not None:
            self.address_book_country = address_book_country
        if address_book_state is not None:
            self.address_book_state = address_book_state
        if address_book_postcode is not None:
            self.address_book_postcode = address_book_postcode
        if address_book_gender is not None:
            self.address_book_gender = address_book_gender
        if address_book_region is not None:
            self.address_book_region = address_book_region
        if address_book_default is not None:
            self.address_book_default = address_book_default

    @property
    def address_book_type(self):
        """Gets the address_book_type of this CustomerAddAddress.  # noqa: E501

        Specifies customer's address type  # noqa: E501

        :return: The address_book_type of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_type

    @address_book_type.setter
    def address_book_type(self, address_book_type):
        """Sets the address_book_type of this CustomerAddAddress.

        Specifies customer's address type  # noqa: E501

        :param address_book_type: The address_book_type of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_type = address_book_type

    @property
    def address_book_first_name(self):
        """Gets the address_book_first_name of this CustomerAddAddress.  # noqa: E501

        Specifies customer's first name in the address book  # noqa: E501

        :return: The address_book_first_name of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_first_name

    @address_book_first_name.setter
    def address_book_first_name(self, address_book_first_name):
        """Sets the address_book_first_name of this CustomerAddAddress.

        Specifies customer's first name in the address book  # noqa: E501

        :param address_book_first_name: The address_book_first_name of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_first_name = address_book_first_name

    @property
    def address_book_last_name(self):
        """Gets the address_book_last_name of this CustomerAddAddress.  # noqa: E501

        Specifies customer's last name in the address book  # noqa: E501

        :return: The address_book_last_name of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_last_name

    @address_book_last_name.setter
    def address_book_last_name(self, address_book_last_name):
        """Sets the address_book_last_name of this CustomerAddAddress.

        Specifies customer's last name in the address book  # noqa: E501

        :param address_book_last_name: The address_book_last_name of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_last_name = address_book_last_name

    @property
    def address_book_company(self):
        """Gets the address_book_company of this CustomerAddAddress.  # noqa: E501

        Specifies customer's company name in the address book  # noqa: E501

        :return: The address_book_company of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_company

    @address_book_company.setter
    def address_book_company(self, address_book_company):
        """Sets the address_book_company of this CustomerAddAddress.

        Specifies customer's company name in the address book  # noqa: E501

        :param address_book_company: The address_book_company of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_company = address_book_company

    @property
    def address_book_fax(self):
        """Gets the address_book_fax of this CustomerAddAddress.  # noqa: E501

        Specifies customer's fax in the address book  # noqa: E501

        :return: The address_book_fax of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_fax

    @address_book_fax.setter
    def address_book_fax(self, address_book_fax):
        """Sets the address_book_fax of this CustomerAddAddress.

        Specifies customer's fax in the address book  # noqa: E501

        :param address_book_fax: The address_book_fax of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_fax = address_book_fax

    @property
    def address_book_phone(self):
        """Gets the address_book_phone of this CustomerAddAddress.  # noqa: E501

        Specifies customer's phone number in the address book  # noqa: E501

        :return: The address_book_phone of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_phone

    @address_book_phone.setter
    def address_book_phone(self, address_book_phone):
        """Sets the address_book_phone of this CustomerAddAddress.

        Specifies customer's phone number in the address book  # noqa: E501

        :param address_book_phone: The address_book_phone of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_phone = address_book_phone

    @property
    def address_book_website(self):
        """Gets the address_book_website of this CustomerAddAddress.  # noqa: E501

        Specifies customer's website in the address book  # noqa: E501

        :return: The address_book_website of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_website

    @address_book_website.setter
    def address_book_website(self, address_book_website):
        """Sets the address_book_website of this CustomerAddAddress.

        Specifies customer's website in the address book  # noqa: E501

        :param address_book_website: The address_book_website of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_website = address_book_website

    @property
    def address_book_address1(self):
        """Gets the address_book_address1 of this CustomerAddAddress.  # noqa: E501

        Specifies customer's first address in the address book  # noqa: E501

        :return: The address_book_address1 of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_address1

    @address_book_address1.setter
    def address_book_address1(self, address_book_address1):
        """Sets the address_book_address1 of this CustomerAddAddress.

        Specifies customer's first address in the address book  # noqa: E501

        :param address_book_address1: The address_book_address1 of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_address1 = address_book_address1

    @property
    def address_book_address2(self):
        """Gets the address_book_address2 of this CustomerAddAddress.  # noqa: E501

        Specifies customer's second address in the address book  # noqa: E501

        :return: The address_book_address2 of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_address2

    @address_book_address2.setter
    def address_book_address2(self, address_book_address2):
        """Sets the address_book_address2 of this CustomerAddAddress.

        Specifies customer's second address in the address book  # noqa: E501

        :param address_book_address2: The address_book_address2 of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_address2 = address_book_address2

    @property
    def address_book_city(self):
        """Gets the address_book_city of this CustomerAddAddress.  # noqa: E501

        Specifies customer's city in the address book  # noqa: E501

        :return: The address_book_city of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_city

    @address_book_city.setter
    def address_book_city(self, address_book_city):
        """Sets the address_book_city of this CustomerAddAddress.

        Specifies customer's city in the address book  # noqa: E501

        :param address_book_city: The address_book_city of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_city = address_book_city

    @property
    def address_book_country(self):
        """Gets the address_book_country of this CustomerAddAddress.  # noqa: E501

        ISO code or name of country  # noqa: E501

        :return: The address_book_country of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_country

    @address_book_country.setter
    def address_book_country(self, address_book_country):
        """Sets the address_book_country of this CustomerAddAddress.

        ISO code or name of country  # noqa: E501

        :param address_book_country: The address_book_country of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_country = address_book_country

    @property
    def address_book_state(self):
        """Gets the address_book_state of this CustomerAddAddress.  # noqa: E501

        ISO code or name of state.  # noqa: E501

        :return: The address_book_state of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_state

    @address_book_state.setter
    def address_book_state(self, address_book_state):
        """Sets the address_book_state of this CustomerAddAddress.

        ISO code or name of state.  # noqa: E501

        :param address_book_state: The address_book_state of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_state = address_book_state

    @property
    def address_book_postcode(self):
        """Gets the address_book_postcode of this CustomerAddAddress.  # noqa: E501

        Specifies customer's postcode  # noqa: E501

        :return: The address_book_postcode of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_postcode

    @address_book_postcode.setter
    def address_book_postcode(self, address_book_postcode):
        """Sets the address_book_postcode of this CustomerAddAddress.

        Specifies customer's postcode  # noqa: E501

        :param address_book_postcode: The address_book_postcode of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_postcode = address_book_postcode

    @property
    def address_book_gender(self):
        """Gets the address_book_gender of this CustomerAddAddress.  # noqa: E501

        Specifies customer's gender  # noqa: E501

        :return: The address_book_gender of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_gender

    @address_book_gender.setter
    def address_book_gender(self, address_book_gender):
        """Sets the address_book_gender of this CustomerAddAddress.

        Specifies customer's gender  # noqa: E501

        :param address_book_gender: The address_book_gender of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_gender = address_book_gender

    @property
    def address_book_region(self):
        """Gets the address_book_region of this CustomerAddAddress.  # noqa: E501

        Specifies customer's region  # noqa: E501

        :return: The address_book_region of this CustomerAddAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_book_region

    @address_book_region.setter
    def address_book_region(self, address_book_region):
        """Sets the address_book_region of this CustomerAddAddress.

        Specifies customer's region  # noqa: E501

        :param address_book_region: The address_book_region of this CustomerAddAddress.  # noqa: E501
        :type: str
        """

        self._address_book_region = address_book_region

    @property
    def address_book_default(self):
        """Gets the address_book_default of this CustomerAddAddress.  # noqa: E501

        Defines whether the address is used by default  # noqa: E501

        :return: The address_book_default of this CustomerAddAddress.  # noqa: E501
        :rtype: bool
        """
        return self._address_book_default

    @address_book_default.setter
    def address_book_default(self, address_book_default):
        """Sets the address_book_default of this CustomerAddAddress.

        Defines whether the address is used by default  # noqa: E501

        :param address_book_default: The address_book_default of this CustomerAddAddress.  # noqa: E501
        :type: bool
        """

        self._address_book_default = address_book_default

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
        if issubclass(CustomerAddAddress, dict):
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
        if not isinstance(other, CustomerAddAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
