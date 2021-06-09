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


class InlineResponse2003ResultEvents(object):
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
        'webhook_name': 'str',
        'entity': 'str',
        'action': 'str'
    }

    attribute_map = {
        'webhook_name': 'webhook_name',
        'entity': 'entity',
        'action': 'action'
    }

    def __init__(self, webhook_name=None, entity=None, action=None):  # noqa: E501
        """InlineResponse2003ResultEvents - a model defined in Swagger"""  # noqa: E501

        self._webhook_name = None
        self._entity = None
        self._action = None
        self.discriminator = None

        if webhook_name is not None:
            self.webhook_name = webhook_name
        if entity is not None:
            self.entity = entity
        if action is not None:
            self.action = action

    @property
    def webhook_name(self):
        """Gets the webhook_name of this InlineResponse2003ResultEvents.  # noqa: E501


        :return: The webhook_name of this InlineResponse2003ResultEvents.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this InlineResponse2003ResultEvents.


        :param webhook_name: The webhook_name of this InlineResponse2003ResultEvents.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

    @property
    def entity(self):
        """Gets the entity of this InlineResponse2003ResultEvents.  # noqa: E501


        :return: The entity of this InlineResponse2003ResultEvents.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this InlineResponse2003ResultEvents.


        :param entity: The entity of this InlineResponse2003ResultEvents.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def action(self):
        """Gets the action of this InlineResponse2003ResultEvents.  # noqa: E501


        :return: The action of this InlineResponse2003ResultEvents.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InlineResponse2003ResultEvents.


        :param action: The action of this InlineResponse2003ResultEvents.  # noqa: E501
        :type: str
        """

        self._action = action

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
        if issubclass(InlineResponse2003ResultEvents, dict):
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
        if not isinstance(other, InlineResponse2003ResultEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other