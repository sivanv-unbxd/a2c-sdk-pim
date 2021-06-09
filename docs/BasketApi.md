# swagger_client.BasketApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basket_info**](BasketApi.md#basket_info) | **GET** /basket.info.json | 
[**basket_item_add**](BasketApi.md#basket_item_add) | **POST** /basket.item.add.json | 
[**basket_live_shipping_service_create**](BasketApi.md#basket_live_shipping_service_create) | **POST** /basket.live_shipping_service.create.json | 
[**basket_live_shipping_service_delete**](BasketApi.md#basket_live_shipping_service_delete) | **DELETE** /basket.live_shipping_service.delete.json | 
[**basket_live_shipping_service_list**](BasketApi.md#basket_live_shipping_service_list) | **GET** /basket.live_shipping_service.list.json | 


# **basket_info**
> InlineResponse20055 basket_info(id, store_id=store_id, params=params, exclude=exclude)



Retrieve basket information.

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
api_instance = swagger_client.BasketApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.basket_info(id, store_id=store_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketApi->basket_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **store_id** | **str**| Store Id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basket_item_add**
> InlineResponse20087 basket_item_add(customer_id, product_id, variant_id=variant_id, quantity=quantity, store_id=store_id)



Add item to basket

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
api_instance = swagger_client.BasketApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Retrieves orders specified by customer id
product_id = 'product_id_example' # str | Defines id of the product which should be added to the basket
variant_id = 'variant_id_example' # str | Defines product's variants specified by variant id (optional)
quantity = 0 # float | Defines new items quantity (optional) (default to 0)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.basket_item_add(customer_id, product_id, variant_id=variant_id, quantity=quantity, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketApi->basket_item_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Retrieves orders specified by customer id | 
 **product_id** | **str**| Defines id of the product which should be added to the basket | 
 **variant_id** | **str**| Defines product&#39;s variants specified by variant id | [optional] 
 **quantity** | **float**| Defines new items quantity | [optional] [default to 0]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basket_live_shipping_service_create**
> InlineResponse20056 basket_live_shipping_service_create(name, param_callback, store_id=store_id)



Create live shipping rate service. (Beta)

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
api_instance = swagger_client.BasketApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Shipping Service Name
param_callback = 'param_callback_example' # str | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.basket_live_shipping_service_create(name, param_callback, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketApi->basket_live_shipping_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Shipping Service Name | 
 **param_callback** | **str**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basket_live_shipping_service_delete**
> InlineResponse20019 basket_live_shipping_service_delete(id)



Delete live shipping rate service. (Beta)

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
api_instance = swagger_client.BasketApi(swagger_client.ApiClient(configuration))
id = 56 # int | Entity id

try:
    api_response = api_instance.basket_live_shipping_service_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketApi->basket_live_shipping_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basket_live_shipping_service_list**
> InlineResponse20054 basket_live_shipping_service_list(store_id=store_id, start=start, count=count)



Retrieve a list of live shipping rate services. (Beta)

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
api_instance = swagger_client.BasketApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | Store Id (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)

try:
    api_response = api_instance.basket_live_shipping_service_list(store_id=store_id, start=start, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketApi->basket_live_shipping_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store Id | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

