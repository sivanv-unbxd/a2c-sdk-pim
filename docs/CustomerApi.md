# swagger_client.CustomerApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_add**](CustomerApi.md#customer_add) | **POST** /customer.add.json | 
[**customer_attribute_list**](CustomerApi.md#customer_attribute_list) | **GET** /customer.attribute.list.json | 
[**customer_count**](CustomerApi.md#customer_count) | **GET** /customer.count.json | 
[**customer_find**](CustomerApi.md#customer_find) | **GET** /customer.find.json | 
[**customer_group_add**](CustomerApi.md#customer_group_add) | **POST** /customer.group.add.json | 
[**customer_group_list**](CustomerApi.md#customer_group_list) | **GET** /customer.group.list.json | 
[**customer_info**](CustomerApi.md#customer_info) | **GET** /customer.info.json | 
[**customer_list**](CustomerApi.md#customer_list) | **GET** /customer.list.json | 
[**customer_update**](CustomerApi.md#customer_update) | **PUT** /customer.update.json | 


# **customer_add**
> InlineResponse20060 customer_add(body)



Add customer into store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerAdd() # CustomerAdd | 

try:
    api_response = api_instance.customer_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerAdd**](CustomerAdd.md)|  | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_attribute_list**
> ModelResponseCustomerAttributeList customer_attribute_list(customer_id, count=count, page_cursor=page_cursor, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude)



Get attributes for specific customer

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Retrieves orders specified by customer id
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.customer_attribute_list(customer_id, count=count, page_cursor=page_cursor, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_attribute_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Retrieves orders specified by customer id | 
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCustomerAttributeList**](ModelResponseCustomerAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_count**
> InlineResponse20057 customer_count(group_id=group_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, store_id=store_id, customer_list_id=customer_list_id)



Get number of customers from store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Customer group_id (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
store_id = 'store_id_example' # str | Counts customer specified by store id (optional)
customer_list_id = 'customer_list_id_example' # str | The numeric ID of the customer list in Demandware. (optional)

try:
    api_response = api_instance.customer_count(group_id=group_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, store_id=store_id, customer_list_id=customer_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Customer group_id | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **store_id** | **str**| Counts customer specified by store id | [optional] 
 **customer_list_id** | **str**| The numeric ID of the customer list in Demandware. | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_find**
> InlineResponse20059 customer_find(find_value, find_where=find_where, find_params=find_params, store_id=store_id)



Find customers in store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
find_value = 'find_value_example' # str | Entity search that is specified by some value
find_where = 'email' # str | Entity search that is specified by the comma-separated unique fields (optional) (default to email)
find_params = 'whole_words' # str | Entity search that is specified by comma-separated parameters (optional) (default to whole_words)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.customer_find(find_value, find_where=find_where, find_params=find_params, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_value** | **str**| Entity search that is specified by some value | 
 **find_where** | **str**| Entity search that is specified by the comma-separated unique fields | [optional] [default to email]
 **find_params** | **str**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_add**
> InlineResponse20014 customer_group_add(name, store_id=store_id, stores_ids=stores_ids)



Create customer group.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Customer group name
store_id = 'store_id_example' # str | Store Id (optional)
stores_ids = 'stores_ids_example' # str | Assign customer group to the stores that is specified by comma-separated stores' id (optional)

try:
    api_response = api_instance.customer_group_add(name, store_id=store_id, stores_ids=stores_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_group_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Customer group name | 
 **store_id** | **str**| Store Id | [optional] 
 **stores_ids** | **str**| Assign customer group to the stores that is specified by comma-separated stores&#39; id | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_list**
> ModelResponseCustomerGroupList customer_group_list(page_cursor=page_cursor, start=start, count=count, store_id=store_id, lang_id=lang_id, group_ids=group_ids, params=params, exclude=exclude)



Get list of customers groups.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
group_ids = 'group_ids_example' # str | Groups that will be assigned to a customer (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.customer_group_list(page_cursor=page_cursor, start=start, count=count, store_id=store_id, lang_id=lang_id, group_ids=group_ids, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **group_ids** | **str**| Groups that will be assigned to a customer | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCustomerGroupList**](ModelResponseCustomerGroupList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_info**
> InlineResponse20058 customer_info(id, params=params, exclude=exclude, store_id=store_id)



Get customers' details from store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Retrieves customer's info specified by customer id
params = 'id,email,first_name,last_name' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,email,first_name,last_name)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Retrieves customer info specified by store id (optional)

try:
    api_response = api_instance.customer_info(id, params=params, exclude=exclude, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Retrieves customer&#39;s info specified by customer id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,email,first_name,last_name]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Retrieves customer info specified by store id | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_list**
> ModelResponseCustomerList customer_list(page_cursor=page_cursor, start=start, count=count, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, params=params, exclude=exclude, group_id=group_id, store_id=store_id, customer_list_id=customer_list_id)



Get list of customers from store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
params = 'id,email,first_name,last_name' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,email,first_name,last_name)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
group_id = 'group_id_example' # str | Customer group_id (optional)
store_id = 'store_id_example' # str | Retrieves customers specified by store id (optional)
customer_list_id = 'customer_list_id_example' # str | The numeric ID of the customer list in Demandware. (optional)

try:
    api_response = api_instance.customer_list(page_cursor=page_cursor, start=start, count=count, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, params=params, exclude=exclude, group_id=group_id, store_id=store_id, customer_list_id=customer_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,email,first_name,last_name]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **group_id** | **str**| Customer group_id | [optional] 
 **store_id** | **str**| Retrieves customers specified by store id | [optional] 
 **customer_list_id** | **str**| The numeric ID of the customer list in Demandware. | [optional] 

### Return type

[**ModelResponseCustomerList**](ModelResponseCustomerList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_update**
> InlineResponse2005 customer_update(id, group_id=group_id, group_ids=group_ids, first_name=first_name, last_name=last_name, news_letter_subscription=news_letter_subscription, tags=tags)



Update information of customer in store.

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
group_id = 'group_id_example' # str | Customer group_id (optional)
group_ids = 'group_ids_example' # str | Groups that will be assigned to a customer (optional)
first_name = 'first_name_example' # str | Defines customer's first name (optional)
last_name = 'last_name_example' # str | Defines customer's last name (optional)
news_letter_subscription = true # bool | Defines whether the newsletter subscription is available for the user (optional)
tags = 'tags_example' # str | Customer tags (optional)

try:
    api_response = api_instance.customer_update(id, group_id=group_id, group_ids=group_ids, first_name=first_name, last_name=last_name, news_letter_subscription=news_letter_subscription, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **group_id** | **str**| Customer group_id | [optional] 
 **group_ids** | **str**| Groups that will be assigned to a customer | [optional] 
 **first_name** | **str**| Defines customer&#39;s first name | [optional] 
 **last_name** | **str**| Defines customer&#39;s last name | [optional] 
 **news_letter_subscription** | **bool**| Defines whether the newsletter subscription is available for the user | [optional] 
 **tags** | **str**| Customer tags | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

