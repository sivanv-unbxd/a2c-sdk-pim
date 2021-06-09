# swagger_client.OrderApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_abandoned_list**](OrderApi.md#order_abandoned_list) | **GET** /order.abandoned.list.json | 
[**order_add**](OrderApi.md#order_add) | **POST** /order.add.json | 
[**order_count**](OrderApi.md#order_count) | **GET** /order.count.json | 
[**order_financial_status_list**](OrderApi.md#order_financial_status_list) | **GET** /order.financial_status.list.json | 
[**order_find**](OrderApi.md#order_find) | **GET** /order.find.json | 
[**order_fulfillment_status_list**](OrderApi.md#order_fulfillment_status_list) | **GET** /order.fulfillment_status.list.json | 
[**order_info**](OrderApi.md#order_info) | **GET** /order.info.json | 
[**order_list**](OrderApi.md#order_list) | **GET** /order.list.json | 
[**order_refund_add**](OrderApi.md#order_refund_add) | **POST** /order.refund.add.json | 
[**order_shipment_add**](OrderApi.md#order_shipment_add) | **POST** /order.shipment.add.json | 
[**order_shipment_delete**](OrderApi.md#order_shipment_delete) | **DELETE** /order.shipment.delete.json | 
[**order_shipment_list**](OrderApi.md#order_shipment_list) | **GET** /order.shipment.list.json | 
[**order_shipment_tracking_add**](OrderApi.md#order_shipment_tracking_add) | **POST** /order.shipment.tracking.add.json | 
[**order_shipment_update**](OrderApi.md#order_shipment_update) | **PUT** /order.shipment.update.json | 
[**order_status_list**](OrderApi.md#order_status_list) | **GET** /order.status.list.json | 
[**order_update**](OrderApi.md#order_update) | **PUT** /order.update.json | 


# **order_abandoned_list**
> ModelResponseOrderAbandonedList order_abandoned_list(customer_id=customer_id, customer_email=customer_email, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, skip_empty_email=skip_empty_email, store_id=store_id, page_cursor=page_cursor, count=count, start=start, params=params, exclude=exclude)



Get list of orders that were left by customers before completing the order.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Retrieves orders specified by customer id (optional)
customer_email = 'customer_email_example' # str | Retrieves orders specified by customer email (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
skip_empty_email = false # bool | Filter empty emails (optional) (default to false)
store_id = 'store_id_example' # str | Store Id (optional)
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
params = 'customer,totals,items' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to customer,totals,items)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.order_abandoned_list(customer_id=customer_id, customer_email=customer_email, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, skip_empty_email=skip_empty_email, store_id=store_id, page_cursor=page_cursor, count=count, start=start, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_abandoned_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Retrieves orders specified by customer id | [optional] 
 **customer_email** | **str**| Retrieves orders specified by customer email | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **skip_empty_email** | **bool**| Filter empty emails | [optional] [default to false]
 **store_id** | **str**| Store Id | [optional] 
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to customer,totals,items]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseOrderAbandonedList**](ModelResponseOrderAbandonedList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_add**
> InlineResponse20046 order_add(body)



Add a new order to the cart.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderAdd() # OrderAdd | 

try:
    api_response = api_instance.order_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderAdd**](OrderAdd.md)|  | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_count**
> InlineResponse20043 order_count(customer_id=customer_id, customer_email=customer_email, order_status=order_status, order_status_ids=order_status_ids, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, store_id=store_id, ids=ids, order_ids=order_ids, ebay_order_status=ebay_order_status, financial_status=financial_status, fulfillment_status=fulfillment_status, shipping_method=shipping_method, delivery_method=delivery_method)



Count orders in store

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Counts orders quantity specified by customer id (optional)
customer_email = 'customer_email_example' # str | Counts orders quantity specified by customer email (optional)
order_status = 'order_status_example' # str | Counts orders quantity specified by order status (optional)
order_status_ids = ['order_status_ids_example'] # list[str] | Retrieves orders specified by order statuses (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
store_id = 'store_id_example' # str | Counts orders quantity specified by store id (optional)
ids = 'ids_example' # str | Counts orders specified by ids (optional)
order_ids = 'order_ids_example' # str | Counts orders specified by order ids (optional)
ebay_order_status = 'ebay_order_status_example' # str | Counts orders quantity specified by order status (optional)
financial_status = 'financial_status_example' # str | Counts orders quantity specified by financial status (optional)
fulfillment_status = 'fulfillment_status_example' # str | Create order with fulfillment status (optional)
shipping_method = 'shipping_method_example' # str | Retrieve entities according to shipping method (optional)
delivery_method = 'delivery_method_example' # str | Retrieves order with delivery method (optional)

try:
    api_response = api_instance.order_count(customer_id=customer_id, customer_email=customer_email, order_status=order_status, order_status_ids=order_status_ids, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, store_id=store_id, ids=ids, order_ids=order_ids, ebay_order_status=ebay_order_status, financial_status=financial_status, fulfillment_status=fulfillment_status, shipping_method=shipping_method, delivery_method=delivery_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Counts orders quantity specified by customer id | [optional] 
 **customer_email** | **str**| Counts orders quantity specified by customer email | [optional] 
 **order_status** | **str**| Counts orders quantity specified by order status | [optional] 
 **order_status_ids** | [**list[str]**](str.md)| Retrieves orders specified by order statuses | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **store_id** | **str**| Counts orders quantity specified by store id | [optional] 
 **ids** | **str**| Counts orders specified by ids | [optional] 
 **order_ids** | **str**| Counts orders specified by order ids | [optional] 
 **ebay_order_status** | **str**| Counts orders quantity specified by order status | [optional] 
 **financial_status** | **str**| Counts orders quantity specified by financial status | [optional] 
 **fulfillment_status** | **str**| Create order with fulfillment status | [optional] 
 **shipping_method** | **str**| Retrieve entities according to shipping method | [optional] 
 **delivery_method** | **str**| Retrieves order with delivery method | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_financial_status_list**
> InlineResponse20048 order_financial_status_list()



Retrieve list of financial statuses

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_financial_status_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_financial_status_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_find**
> InlineResponse20045 order_find(customer_id=customer_id, customer_email=customer_email, order_status=order_status, start=start, count=count, params=params, exclude=exclude, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, financial_status=financial_status)



Find orders

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Retrieves orders specified by customer id (optional)
customer_email = 'customer_email_example' # str | Retrieves orders specified by customer email (optional)
order_status = 'order_status_example' # str | Retrieves orders specified by order status (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'order_id,customer,totals,address,items,bundles,status' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to order_id,customer,totals,address,items,bundles,status)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
financial_status = 'financial_status_example' # str | Retrieves orders specified by financial status (optional)

try:
    api_response = api_instance.order_find(customer_id=customer_id, customer_email=customer_email, order_status=order_status, start=start, count=count, params=params, exclude=exclude, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, financial_status=financial_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Retrieves orders specified by customer id | [optional] 
 **customer_email** | **str**| Retrieves orders specified by customer email | [optional] 
 **order_status** | **str**| Retrieves orders specified by order status | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **financial_status** | **str**| Retrieves orders specified by financial status | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_fulfillment_status_list**
> InlineResponse20049 order_fulfillment_status_list()



Retrieve list of fulfillment statuses

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_fulfillment_status_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_fulfillment_status_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_info**
> InlineResponse20044 order_info(order_id=order_id, id=id, params=params, exclude=exclude, store_id=store_id, enable_cache=enable_cache)



Info about a specific order by ID

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | Retrieves order’s info specified by order id (optional)
id = 'id_example' # str | Retrieves order info specified by id (optional)
params = 'order_id,customer,totals,address,items,bundles,status' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to order_id,customer,totals,address,items,bundles,status)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Defines store id where the order should be found (optional)
enable_cache = false # bool | If the value is 'true' and order exist in our cache, we will return order.info response from cache (optional) (default to false)

try:
    api_response = api_instance.order_info(order_id=order_id, id=id, params=params, exclude=exclude, store_id=store_id, enable_cache=enable_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Retrieves order’s info specified by order id | [optional] 
 **id** | **str**| Retrieves order info specified by id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Defines store id where the order should be found | [optional] 
 **enable_cache** | **bool**| If the value is &#39;true&#39; and order exist in our cache, we will return order.info response from cache | [optional] [default to false]

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_list**
> ModelResponseOrderList order_list(customer_id=customer_id, customer_email=customer_email, phone=phone, order_status=order_status, order_status_ids=order_status_ids, start=start, count=count, page_cursor=page_cursor, sort_by=sort_by, sort_direction=sort_direction, params=params, exclude=exclude, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, store_id=store_id, ids=ids, order_ids=order_ids, ebay_order_status=ebay_order_status, basket_id=basket_id, financial_status=financial_status, fulfillment_status=fulfillment_status, shipping_method=shipping_method, skip_order_ids=skip_order_ids, since_id=since_id, is_deleted=is_deleted, shipping_country_iso3=shipping_country_iso3, enable_cache=enable_cache, delivery_method=delivery_method)



Get list of orders from store.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Retrieves orders specified by customer id (optional)
customer_email = 'customer_email_example' # str | Retrieves orders specified by customer email (optional)
phone = 'phone_example' # str | Filter orders by customer's phone number (optional)
order_status = 'order_status_example' # str | Retrieves orders specified by order status (optional)
order_status_ids = ['order_status_ids_example'] # list[str] | Retrieves orders specified by order statuses (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
page_cursor = 'page_cursor_example' # str | Used to retrieve orders via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
sort_by = 'order_id' # str | Set field to sort by (optional) (default to order_id)
sort_direction = 'asc' # str | Set sorting direction (optional) (default to asc)
params = 'order_id,customer,totals,address,items,bundles,status' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to order_id,customer,totals,address,items,bundles,status)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
store_id = 'store_id_example' # str | Store Id (optional)
ids = 'ids_example' # str | Retrieves orders specified by ids (optional)
order_ids = 'order_ids_example' # str | Retrieves orders specified by order ids (optional)
ebay_order_status = 'ebay_order_status_example' # str | Retrieves orders specified by order status (optional)
basket_id = 'basket_id_example' # str | Retrieves order’s info specified by basket id. (optional)
financial_status = 'financial_status_example' # str | Retrieves orders specified by financial status (optional)
fulfillment_status = 'fulfillment_status_example' # str | Create order with fulfillment status (optional)
shipping_method = 'shipping_method_example' # str | Retrieve entities according to shipping method (optional)
skip_order_ids = 'skip_order_ids_example' # str | Skipped orders by ids (optional)
since_id = 56 # int | Retrieve entities starting from the specified id. (optional)
is_deleted = true # bool | Filter deleted orders (optional)
shipping_country_iso3 = 'shipping_country_iso3_example' # str | Retrieve entities according to shipping country (optional)
enable_cache = false # bool | If the value is 'true', we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add) (optional) (default to false)
delivery_method = 'delivery_method_example' # str | Retrieves order with delivery method (optional)

try:
    api_response = api_instance.order_list(customer_id=customer_id, customer_email=customer_email, phone=phone, order_status=order_status, order_status_ids=order_status_ids, start=start, count=count, page_cursor=page_cursor, sort_by=sort_by, sort_direction=sort_direction, params=params, exclude=exclude, created_to=created_to, created_from=created_from, modified_to=modified_to, modified_from=modified_from, store_id=store_id, ids=ids, order_ids=order_ids, ebay_order_status=ebay_order_status, basket_id=basket_id, financial_status=financial_status, fulfillment_status=fulfillment_status, shipping_method=shipping_method, skip_order_ids=skip_order_ids, since_id=since_id, is_deleted=is_deleted, shipping_country_iso3=shipping_country_iso3, enable_cache=enable_cache, delivery_method=delivery_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Retrieves orders specified by customer id | [optional] 
 **customer_email** | **str**| Retrieves orders specified by customer email | [optional] 
 **phone** | **str**| Filter orders by customer&#39;s phone number | [optional] 
 **order_status** | **str**| Retrieves orders specified by order status | [optional] 
 **order_status_ids** | [**list[str]**](str.md)| Retrieves orders specified by order statuses | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **page_cursor** | **str**| Used to retrieve orders via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **sort_by** | **str**| Set field to sort by | [optional] [default to order_id]
 **sort_direction** | **str**| Set sorting direction | [optional] [default to asc]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **ids** | **str**| Retrieves orders specified by ids | [optional] 
 **order_ids** | **str**| Retrieves orders specified by order ids | [optional] 
 **ebay_order_status** | **str**| Retrieves orders specified by order status | [optional] 
 **basket_id** | **str**| Retrieves order’s info specified by basket id. | [optional] 
 **financial_status** | **str**| Retrieves orders specified by financial status | [optional] 
 **fulfillment_status** | **str**| Create order with fulfillment status | [optional] 
 **shipping_method** | **str**| Retrieve entities according to shipping method | [optional] 
 **skip_order_ids** | **str**| Skipped orders by ids | [optional] 
 **since_id** | **int**| Retrieve entities starting from the specified id. | [optional] 
 **is_deleted** | **bool**| Filter deleted orders | [optional] 
 **shipping_country_iso3** | **str**| Retrieve entities according to shipping country | [optional] 
 **enable_cache** | **bool**| If the value is &#39;true&#39;, we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add) | [optional] [default to false]
 **delivery_method** | **str**| Retrieves order with delivery method | [optional] 

### Return type

[**ModelResponseOrderList**](ModelResponseOrderList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_refund_add**
> InlineResponse20053 order_refund_add(body)



Add a refund to the order.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderRefundAdd() # OrderRefundAdd | 

try:
    api_response = api_instance.order_refund_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_refund_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderRefundAdd**](OrderRefundAdd.md)|  | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_shipment_add**
> InlineResponse20050 order_shipment_add(body)



Add a shipment to the order.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderShipmentAdd() # OrderShipmentAdd | 

try:
    api_response = api_instance.order_shipment_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_shipment_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderShipmentAdd**](OrderShipmentAdd.md)|  | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_shipment_delete**
> InlineResponse20051 order_shipment_delete(shipment_id, order_id)



Delete order's shipment.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
shipment_id = 'shipment_id_example' # str | Shipment id indicates the number of delivery
order_id = 'order_id_example' # str | Defines the order for which the shipment will be deleted

try:
    api_response = api_instance.order_shipment_delete(shipment_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_shipment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| Shipment id indicates the number of delivery | 
 **order_id** | **str**| Defines the order for which the shipment will be deleted | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_shipment_list**
> ModelResponseOrderShipmentList order_shipment_list(order_id, page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, store_id=store_id)



Get list of shipments by orders.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | Retrieves shipments specified by order id
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,order_id,items,tracking_numbers' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,order_id,items,tracking_numbers)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.order_shipment_list(order_id, page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_shipment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Retrieves shipments specified by order id | 
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,order_id,items,tracking_numbers]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**ModelResponseOrderShipmentList**](ModelResponseOrderShipmentList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_shipment_tracking_add**
> InlineResponse20052 order_shipment_tracking_add(body)



Add order shipment's tracking info.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderShipmentTrackingAdd() # OrderShipmentTrackingAdd | 

try:
    api_response = api_instance.order_shipment_tracking_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_shipment_tracking_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderShipmentTrackingAdd**](OrderShipmentTrackingAdd.md)|  | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_shipment_update**
> InlineResponse20028 order_shipment_update(body)



Update order's shipment information.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderShipmentUpdate() # OrderShipmentUpdate | 

try:
    api_response = api_instance.order_shipment_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_shipment_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderShipmentUpdate**](OrderShipmentUpdate.md)|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_status_list**
> InlineResponse20047 order_status_list(store_id=store_id)



Retrieve list of statuses

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.order_status_list(store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_status_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_update**
> InlineResponse20028 order_update(order_id, store_id=store_id, order_status=order_status, comment=comment, admin_comment=admin_comment, admin_private_comment=admin_private_comment, date_modified=date_modified, date_finished=date_finished, financial_status=financial_status, order_payment_method=order_payment_method, send_notifications=send_notifications)



Update existing order.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | Defines the orders specified by order id
store_id = 'store_id_example' # str | Defines store id where the order should be found (optional)
order_status = 'order_status_example' # str | Defines new order's status (optional)
comment = 'comment_example' # str | Specifies order comment (optional)
admin_comment = 'admin_comment_example' # str | Specifies admin's order comment (optional)
admin_private_comment = 'admin_private_comment_example' # str | Specifies private admin's order comment (optional)
date_modified = 'date_modified_example' # str | Specifies order's  modification date (optional)
date_finished = 'date_finished_example' # str | Specifies order's  finished date (optional)
financial_status = 'financial_status_example' # str | Update order financial status to specified (optional)
order_payment_method = 'order_payment_method_example' # str | Defines order payment method.<br/>Setting order_payment_method on Shopify will also change financial_status field value to 'paid' (optional)
send_notifications = false # bool | Send notifications to customer after order was created (optional) (default to false)

try:
    api_response = api_instance.order_update(order_id, store_id=store_id, order_status=order_status, comment=comment, admin_comment=admin_comment, admin_private_comment=admin_private_comment, date_modified=date_modified, date_finished=date_finished, financial_status=financial_status, order_payment_method=order_payment_method, send_notifications=send_notifications)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->order_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Defines the orders specified by order id | 
 **store_id** | **str**| Defines store id where the order should be found | [optional] 
 **order_status** | **str**| Defines new order&#39;s status | [optional] 
 **comment** | **str**| Specifies order comment | [optional] 
 **admin_comment** | **str**| Specifies admin&#39;s order comment | [optional] 
 **admin_private_comment** | **str**| Specifies private admin&#39;s order comment | [optional] 
 **date_modified** | **str**| Specifies order&#39;s  modification date | [optional] 
 **date_finished** | **str**| Specifies order&#39;s  finished date | [optional] 
 **financial_status** | **str**| Update order financial status to specified | [optional] 
 **order_payment_method** | **str**| Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39; | [optional] 
 **send_notifications** | **bool**| Send notifications to customer after order was created | [optional] [default to false]

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

