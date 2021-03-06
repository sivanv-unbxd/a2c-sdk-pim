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


class ProductOption(object):
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
        'product_option_id': 'str',
        'name': 'str',
        'description': 'str',
        'sort_order': 'int',
        'type': 'str',
        'required': 'bool',
        'available': 'bool',
        'used_in_combination': 'bool',
        'option_items': 'list[ProductOptionItem]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'product_option_id': 'product_option_id',
        'name': 'name',
        'description': 'description',
        'sort_order': 'sort_order',
        'type': 'type',
        'required': 'required',
        'available': 'available',
        'used_in_combination': 'used_in_combination',
        'option_items': 'option_items',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, product_option_id=None, name=None, description=None, sort_order=None, type=None, required=None, available=None, used_in_combination=None, option_items=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """ProductOption - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._product_option_id = None
        self._name = None
        self._description = None
        self._sort_order = None
        self._type = None
        self._required = None
        self._available = None
        self._used_in_combination = None
        self._option_items = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if product_option_id is not None:
            self.product_option_id = product_option_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if sort_order is not None:
            self.sort_order = sort_order
        if type is not None:
            self.type = type
        if required is not None:
            self.required = required
        if available is not None:
            self.available = available
        if used_in_combination is not None:
            self.used_in_combination = used_in_combination
        if option_items is not None:
            self.option_items = option_items
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ProductOption.  # noqa: E501


        :return: The id of this ProductOption.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductOption.


        :param id: The id of this ProductOption.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def product_option_id(self):
        """Gets the product_option_id of this ProductOption.  # noqa: E501


        :return: The product_option_id of this ProductOption.  # noqa: E501
        :rtype: str
        """
        return self._product_option_id

    @product_option_id.setter
    def product_option_id(self, product_option_id):
        """Sets the product_option_id of this ProductOption.


        :param product_option_id: The product_option_id of this ProductOption.  # noqa: E501
        :type: str
        """

        self._product_option_id = product_option_id

    @property
    def name(self):
        """Gets the name of this ProductOption.  # noqa: E501


        :return: The name of this ProductOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductOption.


        :param name: The name of this ProductOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProductOption.  # noqa: E501


        :return: The description of this ProductOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductOption.


        :param description: The description of this ProductOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sort_order(self):
        """Gets the sort_order of this ProductOption.  # noqa: E501


        :return: The sort_order of this ProductOption.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ProductOption.


        :param sort_order: The sort_order of this ProductOption.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def type(self):
        """Gets the type of this ProductOption.  # noqa: E501


        :return: The type of this ProductOption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductOption.


        :param type: The type of this ProductOption.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def required(self):
        """Gets the required of this ProductOption.  # noqa: E501


        :return: The required of this ProductOption.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ProductOption.


        :param required: The required of this ProductOption.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def available(self):
        """Gets the available of this ProductOption.  # noqa: E501


        :return: The available of this ProductOption.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this ProductOption.


        :param available: The available of this ProductOption.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def used_in_combination(self):
        """Gets the used_in_combination of this ProductOption.  # noqa: E501


        :return: The used_in_combination of this ProductOption.  # noqa: E501
        :rtype: bool
        """
        return self._used_in_combination

    @used_in_combination.setter
    def used_in_combination(self, used_in_combination):
        """Sets the used_in_combination of this ProductOption.


        :param used_in_combination: The used_in_combination of this ProductOption.  # noqa: E501
        :type: bool
        """

        self._used_in_combination = used_in_combination

    @property
    def option_items(self):
        """Gets the option_items of this ProductOption.  # noqa: E501


        :return: The option_items of this ProductOption.  # noqa: E501
        :rtype: list[ProductOptionItem]
        """
        return self._option_items

    @option_items.setter
    def option_items(self, option_items):
        """Sets the option_items of this ProductOption.


        :param option_items: The option_items of this ProductOption.  # noqa: E501
        :type: list[ProductOptionItem]
        """

        self._option_items = option_items

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ProductOption.  # noqa: E501


        :return: The additional_fields of this ProductOption.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ProductOption.


        :param additional_fields: The additional_fields of this ProductOption.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ProductOption.  # noqa: E501


        :return: The custom_fields of this ProductOption.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ProductOption.


        :param custom_fields: The custom_fields of this ProductOption.  # noqa: E501
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
        if issubclass(ProductOption, dict):
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
        if not isinstance(other, ProductOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
