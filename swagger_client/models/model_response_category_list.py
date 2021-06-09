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


class ModelResponseCategoryList(object):
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
        'return_code': 'int',
        'return_message': 'str',
        'pagination': 'Pagination',
        'result': 'ResponseCategoryListResult',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'return_code': 'return_code',
        'return_message': 'return_message',
        'pagination': 'pagination',
        'result': 'result',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, return_code=None, return_message=None, pagination=None, result=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """ModelResponseCategoryList - a model defined in Swagger"""  # noqa: E501

        self._return_code = None
        self._return_message = None
        self._pagination = None
        self._result = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if pagination is not None:
            self.pagination = pagination
        if result is not None:
            self.result = result
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def return_code(self):
        """Gets the return_code of this ModelResponseCategoryList.  # noqa: E501


        :return: The return_code of this ModelResponseCategoryList.  # noqa: E501
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this ModelResponseCategoryList.


        :param return_code: The return_code of this ModelResponseCategoryList.  # noqa: E501
        :type: int
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this ModelResponseCategoryList.  # noqa: E501


        :return: The return_message of this ModelResponseCategoryList.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this ModelResponseCategoryList.


        :param return_message: The return_message of this ModelResponseCategoryList.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def pagination(self):
        """Gets the pagination of this ModelResponseCategoryList.  # noqa: E501


        :return: The pagination of this ModelResponseCategoryList.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ModelResponseCategoryList.


        :param pagination: The pagination of this ModelResponseCategoryList.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def result(self):
        """Gets the result of this ModelResponseCategoryList.  # noqa: E501


        :return: The result of this ModelResponseCategoryList.  # noqa: E501
        :rtype: ResponseCategoryListResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ModelResponseCategoryList.


        :param result: The result of this ModelResponseCategoryList.  # noqa: E501
        :type: ResponseCategoryListResult
        """

        self._result = result

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ModelResponseCategoryList.  # noqa: E501


        :return: The additional_fields of this ModelResponseCategoryList.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ModelResponseCategoryList.


        :param additional_fields: The additional_fields of this ModelResponseCategoryList.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ModelResponseCategoryList.  # noqa: E501


        :return: The custom_fields of this ModelResponseCategoryList.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ModelResponseCategoryList.


        :param custom_fields: The custom_fields of this ModelResponseCategoryList.  # noqa: E501
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
        if issubclass(ModelResponseCategoryList, dict):
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
        if not isinstance(other, ModelResponseCategoryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
