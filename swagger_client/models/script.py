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


class Script(object):
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
        'name': 'str',
        'description': 'str',
        'src': 'str',
        'scope': 'str',
        'event': 'str',
        'load_method': 'str',
        'html': 'str',
        'created_time': 'A2CDateTime',
        'modified_time': 'A2CDateTime',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'src': 'src',
        'scope': 'scope',
        'event': 'event',
        'load_method': 'load_method',
        'html': 'html',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, name=None, description=None, src=None, scope=None, event=None, load_method=None, html=None, created_time=None, modified_time=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Script - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._src = None
        self._scope = None
        self._event = None
        self._load_method = None
        self._html = None
        self._created_time = None
        self._modified_time = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if src is not None:
            self.src = src
        if scope is not None:
            self.scope = scope
        if event is not None:
            self.event = event
        if load_method is not None:
            self.load_method = load_method
        if html is not None:
            self.html = html
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Script.  # noqa: E501


        :return: The id of this Script.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Script.


        :param id: The id of this Script.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Script.  # noqa: E501


        :return: The name of this Script.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Script.


        :param name: The name of this Script.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Script.  # noqa: E501


        :return: The description of this Script.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Script.


        :param description: The description of this Script.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def src(self):
        """Gets the src of this Script.  # noqa: E501


        :return: The src of this Script.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this Script.


        :param src: The src of this Script.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def scope(self):
        """Gets the scope of this Script.  # noqa: E501


        :return: The scope of this Script.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Script.


        :param scope: The scope of this Script.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def event(self):
        """Gets the event of this Script.  # noqa: E501


        :return: The event of this Script.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Script.


        :param event: The event of this Script.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def load_method(self):
        """Gets the load_method of this Script.  # noqa: E501


        :return: The load_method of this Script.  # noqa: E501
        :rtype: str
        """
        return self._load_method

    @load_method.setter
    def load_method(self, load_method):
        """Sets the load_method of this Script.


        :param load_method: The load_method of this Script.  # noqa: E501
        :type: str
        """

        self._load_method = load_method

    @property
    def html(self):
        """Gets the html of this Script.  # noqa: E501


        :return: The html of this Script.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this Script.


        :param html: The html of this Script.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def created_time(self):
        """Gets the created_time of this Script.  # noqa: E501


        :return: The created_time of this Script.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Script.


        :param created_time: The created_time of this Script.  # noqa: E501
        :type: A2CDateTime
        """

        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this Script.  # noqa: E501


        :return: The modified_time of this Script.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Script.


        :param modified_time: The modified_time of this Script.  # noqa: E501
        :type: A2CDateTime
        """

        self._modified_time = modified_time

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Script.  # noqa: E501


        :return: The additional_fields of this Script.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Script.


        :param additional_fields: The additional_fields of this Script.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Script.  # noqa: E501


        :return: The custom_fields of this Script.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Script.


        :param custom_fields: The custom_fields of this Script.  # noqa: E501
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
        if issubclass(Script, dict):
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
        if not isinstance(other, Script):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
