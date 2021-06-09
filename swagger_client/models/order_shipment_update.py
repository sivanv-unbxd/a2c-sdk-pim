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


class OrderShipmentUpdate(object):
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
        'store_id': 'str',
        'shipment_id': 'str',
        'order_id': 'str',
        'tracking_numbers': 'list[OrderShipmentAddTrackingNumbers]',
        'replace': 'bool'
    }

    attribute_map = {
        'store_id': 'store_id',
        'shipment_id': 'shipment_id',
        'order_id': 'order_id',
        'tracking_numbers': 'tracking_numbers',
        'replace': 'replace'
    }

    def __init__(self, store_id=None, shipment_id=None, order_id=None, tracking_numbers=None, replace=True):  # noqa: E501
        """OrderShipmentUpdate - a model defined in Swagger"""  # noqa: E501

        self._store_id = None
        self._shipment_id = None
        self._order_id = None
        self._tracking_numbers = None
        self._replace = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        self.shipment_id = shipment_id
        if order_id is not None:
            self.order_id = order_id
        if tracking_numbers is not None:
            self.tracking_numbers = tracking_numbers
        if replace is not None:
            self.replace = replace

    @property
    def store_id(self):
        """Gets the store_id of this OrderShipmentUpdate.  # noqa: E501

        Store Id  # noqa: E501

        :return: The store_id of this OrderShipmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this OrderShipmentUpdate.

        Store Id  # noqa: E501

        :param store_id: The store_id of this OrderShipmentUpdate.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def shipment_id(self):
        """Gets the shipment_id of this OrderShipmentUpdate.  # noqa: E501

        Shipment id indicates the number of delivery  # noqa: E501

        :return: The shipment_id of this OrderShipmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this OrderShipmentUpdate.

        Shipment id indicates the number of delivery  # noqa: E501

        :param shipment_id: The shipment_id of this OrderShipmentUpdate.  # noqa: E501
        :type: str
        """
        if shipment_id is None:
            raise ValueError("Invalid value for `shipment_id`, must not be `None`")  # noqa: E501

        self._shipment_id = shipment_id

    @property
    def order_id(self):
        """Gets the order_id of this OrderShipmentUpdate.  # noqa: E501

        Defines the order that will be updated  # noqa: E501

        :return: The order_id of this OrderShipmentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderShipmentUpdate.

        Defines the order that will be updated  # noqa: E501

        :param order_id: The order_id of this OrderShipmentUpdate.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def tracking_numbers(self):
        """Gets the tracking_numbers of this OrderShipmentUpdate.  # noqa: E501

        Defines shipment's tracking numbers that have to be added</br> How set tracking numbers to appropriate carrier:<ul><li>tracking_numbers[]=a2c.demo1,a2c.demo2 - set default carrier</li><li>tracking_numbers[<b>carrier_id</b>]=a2c.demo - set appropriate carrier</li></ul>To get the list of carriers IDs that are available in your store, use the <a href = \"http://docs.api2cart.com/cart-info\">cart.info</a > method  # noqa: E501

        :return: The tracking_numbers of this OrderShipmentUpdate.  # noqa: E501
        :rtype: list[OrderShipmentAddTrackingNumbers]
        """
        return self._tracking_numbers

    @tracking_numbers.setter
    def tracking_numbers(self, tracking_numbers):
        """Sets the tracking_numbers of this OrderShipmentUpdate.

        Defines shipment's tracking numbers that have to be added</br> How set tracking numbers to appropriate carrier:<ul><li>tracking_numbers[]=a2c.demo1,a2c.demo2 - set default carrier</li><li>tracking_numbers[<b>carrier_id</b>]=a2c.demo - set appropriate carrier</li></ul>To get the list of carriers IDs that are available in your store, use the <a href = \"http://docs.api2cart.com/cart-info\">cart.info</a > method  # noqa: E501

        :param tracking_numbers: The tracking_numbers of this OrderShipmentUpdate.  # noqa: E501
        :type: list[OrderShipmentAddTrackingNumbers]
        """

        self._tracking_numbers = tracking_numbers

    @property
    def replace(self):
        """Gets the replace of this OrderShipmentUpdate.  # noqa: E501

        Allows rewrite tracking numbers  # noqa: E501

        :return: The replace of this OrderShipmentUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        """Sets the replace of this OrderShipmentUpdate.

        Allows rewrite tracking numbers  # noqa: E501

        :param replace: The replace of this OrderShipmentUpdate.  # noqa: E501
        :type: bool
        """

        self._replace = replace

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
        if issubclass(OrderShipmentUpdate, dict):
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
        if not isinstance(other, OrderShipmentUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
