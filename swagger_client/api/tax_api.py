# coding: utf-8

"""
    Swagger API2Cart

    API2Cart  # noqa: E501

    OpenAPI spec version: 1.1
    Contact: contact@api2cart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TaxApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tax_class_info(self, tax_class_id, **kwargs):  # noqa: E501
        """tax_class_info  # noqa: E501

        Get info about tax  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tax_class_info(tax_class_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tax_class_id: Retrieves taxes specified by class id (required)
        :param str params: Set this parameter in order to choose which entity fields you want to retrieve
        :param str exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tax_class_info_with_http_info(tax_class_id, **kwargs)  # noqa: E501
        else:
            (data) = self.tax_class_info_with_http_info(tax_class_id, **kwargs)  # noqa: E501
            return data

    def tax_class_info_with_http_info(self, tax_class_id, **kwargs):  # noqa: E501
        """tax_class_info  # noqa: E501

        Get info about tax  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tax_class_info_with_http_info(tax_class_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tax_class_id: Retrieves taxes specified by class id (required)
        :param str params: Set this parameter in order to choose which entity fields you want to retrieve
        :param str exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class_id', 'params', 'exclude']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tax_class_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tax_class_id' is set
        if ('tax_class_id' not in params or
                params['tax_class_id'] is None):
            raise ValueError("Missing the required parameter `tax_class_id` when calling `tax_class_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tax_class_id' in params:
            query_params.append(('tax_class_id', params['tax_class_id']))  # noqa: E501
        if 'params' in params:
            query_params.append(('params', params['params']))  # noqa: E501
        if 'exclude' in params:
            query_params.append(('exclude', params['exclude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'store_key']  # noqa: E501

        return self.api_client.call_api(
            '/tax.class.info.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20086',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
