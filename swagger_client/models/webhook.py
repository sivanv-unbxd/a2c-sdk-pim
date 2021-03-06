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


class Webhook(object):
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
        'id': 'int',
        'label': 'str',
        'store_id': 'str',
        'active': 'bool',
        'callback': 'str',
        'fields': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'entity': 'str',
        'action': 'str',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'store_id': 'store_id',
        'active': 'active',
        'callback': 'callback',
        'fields': 'fields',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'entity': 'entity',
        'action': 'action',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, label=None, store_id=None, active=None, callback=None, fields=None, created_at=None, updated_at=None, entity=None, action=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._label = None
        self._store_id = None
        self._active = None
        self._callback = None
        self._fields = None
        self._created_at = None
        self._updated_at = None
        self._entity = None
        self._action = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if store_id is not None:
            self.store_id = store_id
        if active is not None:
            self.active = active
        if callback is not None:
            self.callback = callback
        if fields is not None:
            self.fields = fields
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if entity is not None:
            self.entity = entity
        if action is not None:
            self.action = action
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501


        :return: The id of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.


        :param id: The id of this Webhook.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Webhook.  # noqa: E501


        :return: The label of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Webhook.


        :param label: The label of this Webhook.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def store_id(self):
        """Gets the store_id of this Webhook.  # noqa: E501


        :return: The store_id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this Webhook.


        :param store_id: The store_id of this Webhook.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def active(self):
        """Gets the active of this Webhook.  # noqa: E501


        :return: The active of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Webhook.


        :param active: The active of this Webhook.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def callback(self):
        """Gets the callback of this Webhook.  # noqa: E501


        :return: The callback of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this Webhook.


        :param callback: The callback of this Webhook.  # noqa: E501
        :type: str
        """

        self._callback = callback

    @property
    def fields(self):
        """Gets the fields of this Webhook.  # noqa: E501


        :return: The fields of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Webhook.


        :param fields: The fields of this Webhook.  # noqa: E501
        :type: str
        """

        self._fields = fields

    @property
    def created_at(self):
        """Gets the created_at of this Webhook.  # noqa: E501


        :return: The created_at of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Webhook.


        :param created_at: The created_at of this Webhook.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Webhook.  # noqa: E501


        :return: The updated_at of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Webhook.


        :param updated_at: The updated_at of this Webhook.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def entity(self):
        """Gets the entity of this Webhook.  # noqa: E501


        :return: The entity of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Webhook.


        :param entity: The entity of this Webhook.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def action(self):
        """Gets the action of this Webhook.  # noqa: E501


        :return: The action of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Webhook.


        :param action: The action of this Webhook.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Webhook.  # noqa: E501


        :return: The additional_fields of this Webhook.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Webhook.


        :param additional_fields: The additional_fields of this Webhook.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Webhook.  # noqa: E501


        :return: The custom_fields of this Webhook.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Webhook.


        :param custom_fields: The custom_fields of this Webhook.  # noqa: E501
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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
