# swagger_client.TaxApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_class_info**](TaxApi.md#tax_class_info) | **GET** /tax.class.info.json | 


# **tax_class_info**
> InlineResponse20086 tax_class_info(tax_class_id, params=params, exclude=exclude)



Get info about tax

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: store_key
configuration = swagger_client.Configuration()
configuration.api_key['store_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['store_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TaxApi(swagger_client.ApiClient(configuration))
tax_class_id = 'tax_class_id_example' # str | Retrieves taxes specified by class id
params = 'tax_class_id,name,avail' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to tax_class_id,name,avail)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.tax_class_info(tax_class_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->tax_class_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_class_id** | **str**| Retrieves taxes specified by class id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to tax_class_id,name,avail]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

