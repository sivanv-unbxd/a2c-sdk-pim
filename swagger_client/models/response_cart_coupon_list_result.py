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


class ResponseCartCouponListResult(object):
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
        'coupon_count': 'int',
        'coupon': 'list[Coupon]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'coupon_count': 'coupon_count',
        'coupon': 'coupon',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, coupon_count=None, coupon=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """ResponseCartCouponListResult - a model defined in Swagger"""  # noqa: E501

        self._coupon_count = None
        self._coupon = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if coupon_count is not None:
            self.coupon_count = coupon_count
        if coupon is not None:
            self.coupon = coupon
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def coupon_count(self):
        """Gets the coupon_count of this ResponseCartCouponListResult.  # noqa: E501


        :return: The coupon_count of this ResponseCartCouponListResult.  # noqa: E501
        :rtype: int
        """
        return self._coupon_count

    @coupon_count.setter
    def coupon_count(self, coupon_count):
        """Sets the coupon_count of this ResponseCartCouponListResult.


        :param coupon_count: The coupon_count of this ResponseCartCouponListResult.  # noqa: E501
        :type: int
        """

        self._coupon_count = coupon_count

    @property
    def coupon(self):
        """Gets the coupon of this ResponseCartCouponListResult.  # noqa: E501


        :return: The coupon of this ResponseCartCouponListResult.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this ResponseCartCouponListResult.


        :param coupon: The coupon of this ResponseCartCouponListResult.  # noqa: E501
        :type: list[Coupon]
        """

        self._coupon = coupon

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ResponseCartCouponListResult.  # noqa: E501


        :return: The additional_fields of this ResponseCartCouponListResult.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ResponseCartCouponListResult.


        :param additional_fields: The additional_fields of this ResponseCartCouponListResult.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResponseCartCouponListResult.  # noqa: E501


        :return: The custom_fields of this ResponseCartCouponListResult.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResponseCartCouponListResult.


        :param custom_fields: The custom_fields of this ResponseCartCouponListResult.  # noqa: E501
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
        if issubclass(ResponseCartCouponListResult, dict):
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
        if not isinstance(other, ResponseCartCouponListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
