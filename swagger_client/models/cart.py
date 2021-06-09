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


class Cart(object):
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
        'name': 'str',
        'url': 'str',
        'version': 'str',
        'db_prefix': 'str',
        'stores_info': 'list[CartStoreInfo]',
        'warehouses': 'list[CartWarehouse]',
        'shipping_zones': 'list[CartShippingZone]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'version': 'version',
        'db_prefix': 'db_prefix',
        'stores_info': 'stores_info',
        'warehouses': 'warehouses',
        'shipping_zones': 'shipping_zones',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, name=None, url=None, version=None, db_prefix=None, stores_info=None, warehouses=None, shipping_zones=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Cart - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._url = None
        self._version = None
        self._db_prefix = None
        self._stores_info = None
        self._warehouses = None
        self._shipping_zones = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if version is not None:
            self.version = version
        if db_prefix is not None:
            self.db_prefix = db_prefix
        if stores_info is not None:
            self.stores_info = stores_info
        if warehouses is not None:
            self.warehouses = warehouses
        if shipping_zones is not None:
            self.shipping_zones = shipping_zones
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def name(self):
        """Gets the name of this Cart.  # noqa: E501


        :return: The name of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cart.


        :param name: The name of this Cart.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Cart.  # noqa: E501


        :return: The url of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Cart.


        :param url: The url of this Cart.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def version(self):
        """Gets the version of this Cart.  # noqa: E501


        :return: The version of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Cart.


        :param version: The version of this Cart.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def db_prefix(self):
        """Gets the db_prefix of this Cart.  # noqa: E501


        :return: The db_prefix of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._db_prefix

    @db_prefix.setter
    def db_prefix(self, db_prefix):
        """Sets the db_prefix of this Cart.


        :param db_prefix: The db_prefix of this Cart.  # noqa: E501
        :type: str
        """

        self._db_prefix = db_prefix

    @property
    def stores_info(self):
        """Gets the stores_info of this Cart.  # noqa: E501


        :return: The stores_info of this Cart.  # noqa: E501
        :rtype: list[CartStoreInfo]
        """
        return self._stores_info

    @stores_info.setter
    def stores_info(self, stores_info):
        """Sets the stores_info of this Cart.


        :param stores_info: The stores_info of this Cart.  # noqa: E501
        :type: list[CartStoreInfo]
        """

        self._stores_info = stores_info

    @property
    def warehouses(self):
        """Gets the warehouses of this Cart.  # noqa: E501


        :return: The warehouses of this Cart.  # noqa: E501
        :rtype: list[CartWarehouse]
        """
        return self._warehouses

    @warehouses.setter
    def warehouses(self, warehouses):
        """Sets the warehouses of this Cart.


        :param warehouses: The warehouses of this Cart.  # noqa: E501
        :type: list[CartWarehouse]
        """

        self._warehouses = warehouses

    @property
    def shipping_zones(self):
        """Gets the shipping_zones of this Cart.  # noqa: E501


        :return: The shipping_zones of this Cart.  # noqa: E501
        :rtype: list[CartShippingZone]
        """
        return self._shipping_zones

    @shipping_zones.setter
    def shipping_zones(self, shipping_zones):
        """Sets the shipping_zones of this Cart.


        :param shipping_zones: The shipping_zones of this Cart.  # noqa: E501
        :type: list[CartShippingZone]
        """

        self._shipping_zones = shipping_zones

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Cart.  # noqa: E501


        :return: The additional_fields of this Cart.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Cart.


        :param additional_fields: The additional_fields of this Cart.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Cart.  # noqa: E501


        :return: The custom_fields of this Cart.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Cart.


        :param custom_fields: The custom_fields of this Cart.  # noqa: E501
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
        if issubclass(Cart, dict):
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
        if not isinstance(other, Cart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
