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


class OrderStatusRefundItem(object):
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
        'product_id': 'str',
        'variant_id': 'str',
        'order_product_id': 'str',
        'qty': 'float',
        'refund': 'float',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'product_id': 'product_id',
        'variant_id': 'variant_id',
        'order_product_id': 'order_product_id',
        'qty': 'qty',
        'refund': 'refund',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, product_id=None, variant_id=None, order_product_id=None, qty=None, refund=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """OrderStatusRefundItem - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._variant_id = None
        self._order_product_id = None
        self._qty = None
        self._refund = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if variant_id is not None:
            self.variant_id = variant_id
        if order_product_id is not None:
            self.order_product_id = order_product_id
        if qty is not None:
            self.qty = qty
        if refund is not None:
            self.refund = refund
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def product_id(self):
        """Gets the product_id of this OrderStatusRefundItem.  # noqa: E501


        :return: The product_id of this OrderStatusRefundItem.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this OrderStatusRefundItem.


        :param product_id: The product_id of this OrderStatusRefundItem.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def variant_id(self):
        """Gets the variant_id of this OrderStatusRefundItem.  # noqa: E501


        :return: The variant_id of this OrderStatusRefundItem.  # noqa: E501
        :rtype: str
        """
        return self._variant_id

    @variant_id.setter
    def variant_id(self, variant_id):
        """Sets the variant_id of this OrderStatusRefundItem.


        :param variant_id: The variant_id of this OrderStatusRefundItem.  # noqa: E501
        :type: str
        """

        self._variant_id = variant_id

    @property
    def order_product_id(self):
        """Gets the order_product_id of this OrderStatusRefundItem.  # noqa: E501


        :return: The order_product_id of this OrderStatusRefundItem.  # noqa: E501
        :rtype: str
        """
        return self._order_product_id

    @order_product_id.setter
    def order_product_id(self, order_product_id):
        """Sets the order_product_id of this OrderStatusRefundItem.


        :param order_product_id: The order_product_id of this OrderStatusRefundItem.  # noqa: E501
        :type: str
        """

        self._order_product_id = order_product_id

    @property
    def qty(self):
        """Gets the qty of this OrderStatusRefundItem.  # noqa: E501


        :return: The qty of this OrderStatusRefundItem.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this OrderStatusRefundItem.


        :param qty: The qty of this OrderStatusRefundItem.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def refund(self):
        """Gets the refund of this OrderStatusRefundItem.  # noqa: E501


        :return: The refund of this OrderStatusRefundItem.  # noqa: E501
        :rtype: float
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this OrderStatusRefundItem.


        :param refund: The refund of this OrderStatusRefundItem.  # noqa: E501
        :type: float
        """

        self._refund = refund

    @property
    def additional_fields(self):
        """Gets the additional_fields of this OrderStatusRefundItem.  # noqa: E501


        :return: The additional_fields of this OrderStatusRefundItem.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this OrderStatusRefundItem.


        :param additional_fields: The additional_fields of this OrderStatusRefundItem.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderStatusRefundItem.  # noqa: E501


        :return: The custom_fields of this OrderStatusRefundItem.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderStatusRefundItem.


        :param custom_fields: The custom_fields of this OrderStatusRefundItem.  # noqa: E501
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
        if issubclass(OrderStatusRefundItem, dict):
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
        if not isinstance(other, OrderStatusRefundItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other