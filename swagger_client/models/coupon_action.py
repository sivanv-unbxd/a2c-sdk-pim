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


class CouponAction(object):
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
        'scope': 'str',
        'apply_to': 'str',
        'amount': 'float',
        'currency_code': 'str',
        'include_tax': 'bool',
        'type': 'str',
        'discounted_quantity': 'float',
        'discount_quantity_step': 'int',
        'logic_operator': 'str',
        'conditions': 'list[CouponCondition]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'scope': 'scope',
        'apply_to': 'apply_to',
        'amount': 'amount',
        'currency_code': 'currency_code',
        'include_tax': 'include_tax',
        'type': 'type',
        'discounted_quantity': 'discounted_quantity',
        'discount_quantity_step': 'discount_quantity_step',
        'logic_operator': 'logic_operator',
        'conditions': 'conditions',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, scope=None, apply_to=None, amount=None, currency_code=None, include_tax=None, type=None, discounted_quantity=None, discount_quantity_step=None, logic_operator=None, conditions=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """CouponAction - a model defined in Swagger"""  # noqa: E501

        self._scope = None
        self._apply_to = None
        self._amount = None
        self._currency_code = None
        self._include_tax = None
        self._type = None
        self._discounted_quantity = None
        self._discount_quantity_step = None
        self._logic_operator = None
        self._conditions = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if apply_to is not None:
            self.apply_to = apply_to
        if amount is not None:
            self.amount = amount
        if currency_code is not None:
            self.currency_code = currency_code
        if include_tax is not None:
            self.include_tax = include_tax
        if type is not None:
            self.type = type
        if discounted_quantity is not None:
            self.discounted_quantity = discounted_quantity
        if discount_quantity_step is not None:
            self.discount_quantity_step = discount_quantity_step
        if logic_operator is not None:
            self.logic_operator = logic_operator
        if conditions is not None:
            self.conditions = conditions
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def scope(self):
        """Gets the scope of this CouponAction.  # noqa: E501


        :return: The scope of this CouponAction.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CouponAction.


        :param scope: The scope of this CouponAction.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def apply_to(self):
        """Gets the apply_to of this CouponAction.  # noqa: E501


        :return: The apply_to of this CouponAction.  # noqa: E501
        :rtype: str
        """
        return self._apply_to

    @apply_to.setter
    def apply_to(self, apply_to):
        """Sets the apply_to of this CouponAction.


        :param apply_to: The apply_to of this CouponAction.  # noqa: E501
        :type: str
        """

        self._apply_to = apply_to

    @property
    def amount(self):
        """Gets the amount of this CouponAction.  # noqa: E501


        :return: The amount of this CouponAction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CouponAction.


        :param amount: The amount of this CouponAction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this CouponAction.  # noqa: E501


        :return: The currency_code of this CouponAction.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CouponAction.


        :param currency_code: The currency_code of this CouponAction.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def include_tax(self):
        """Gets the include_tax of this CouponAction.  # noqa: E501


        :return: The include_tax of this CouponAction.  # noqa: E501
        :rtype: bool
        """
        return self._include_tax

    @include_tax.setter
    def include_tax(self, include_tax):
        """Sets the include_tax of this CouponAction.


        :param include_tax: The include_tax of this CouponAction.  # noqa: E501
        :type: bool
        """

        self._include_tax = include_tax

    @property
    def type(self):
        """Gets the type of this CouponAction.  # noqa: E501


        :return: The type of this CouponAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CouponAction.


        :param type: The type of this CouponAction.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def discounted_quantity(self):
        """Gets the discounted_quantity of this CouponAction.  # noqa: E501


        :return: The discounted_quantity of this CouponAction.  # noqa: E501
        :rtype: float
        """
        return self._discounted_quantity

    @discounted_quantity.setter
    def discounted_quantity(self, discounted_quantity):
        """Sets the discounted_quantity of this CouponAction.


        :param discounted_quantity: The discounted_quantity of this CouponAction.  # noqa: E501
        :type: float
        """

        self._discounted_quantity = discounted_quantity

    @property
    def discount_quantity_step(self):
        """Gets the discount_quantity_step of this CouponAction.  # noqa: E501


        :return: The discount_quantity_step of this CouponAction.  # noqa: E501
        :rtype: int
        """
        return self._discount_quantity_step

    @discount_quantity_step.setter
    def discount_quantity_step(self, discount_quantity_step):
        """Sets the discount_quantity_step of this CouponAction.


        :param discount_quantity_step: The discount_quantity_step of this CouponAction.  # noqa: E501
        :type: int
        """

        self._discount_quantity_step = discount_quantity_step

    @property
    def logic_operator(self):
        """Gets the logic_operator of this CouponAction.  # noqa: E501


        :return: The logic_operator of this CouponAction.  # noqa: E501
        :rtype: str
        """
        return self._logic_operator

    @logic_operator.setter
    def logic_operator(self, logic_operator):
        """Sets the logic_operator of this CouponAction.


        :param logic_operator: The logic_operator of this CouponAction.  # noqa: E501
        :type: str
        """

        self._logic_operator = logic_operator

    @property
    def conditions(self):
        """Gets the conditions of this CouponAction.  # noqa: E501


        :return: The conditions of this CouponAction.  # noqa: E501
        :rtype: list[CouponCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CouponAction.


        :param conditions: The conditions of this CouponAction.  # noqa: E501
        :type: list[CouponCondition]
        """

        self._conditions = conditions

    @property
    def additional_fields(self):
        """Gets the additional_fields of this CouponAction.  # noqa: E501


        :return: The additional_fields of this CouponAction.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this CouponAction.


        :param additional_fields: The additional_fields of this CouponAction.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CouponAction.  # noqa: E501


        :return: The custom_fields of this CouponAction.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CouponAction.


        :param custom_fields: The custom_fields of this CouponAction.  # noqa: E501
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
        if issubclass(CouponAction, dict):
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
        if not isinstance(other, CouponAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
