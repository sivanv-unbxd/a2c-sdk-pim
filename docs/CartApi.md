# swagger_client.CartApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bridge_download**](CartApi.md#bridge_download) | **GET** /bridge.download.file | 
[**cart_bridge**](CartApi.md#cart_bridge) | **GET** /cart.bridge.json | 
[**cart_catalog_price_rules_count**](CartApi.md#cart_catalog_price_rules_count) | **GET** /cart.catalog_price_rules.count.json | 
[**cart_catalog_price_rules_list**](CartApi.md#cart_catalog_price_rules_list) | **GET** /cart.catalog_price_rules.list.json | 
[**cart_clear_cache**](CartApi.md#cart_clear_cache) | **POST** /cart.clear_cache.json | 
[**cart_config**](CartApi.md#cart_config) | **GET** /cart.config.json | 
[**cart_config_update**](CartApi.md#cart_config_update) | **PUT** /cart.config.update.json | 
[**cart_coupon_add**](CartApi.md#cart_coupon_add) | **POST** /cart.coupon.add.json | 
[**cart_coupon_condition_add**](CartApi.md#cart_coupon_condition_add) | **POST** /cart.coupon.condition.add.json | 
[**cart_coupon_count**](CartApi.md#cart_coupon_count) | **GET** /cart.coupon.count.json | 
[**cart_coupon_delete**](CartApi.md#cart_coupon_delete) | **DELETE** /cart.coupon.delete.json | 
[**cart_coupon_list**](CartApi.md#cart_coupon_list) | **GET** /cart.coupon.list.json | 
[**cart_create**](CartApi.md#cart_create) | **POST** /cart.create.json | 
[**cart_delete**](CartApi.md#cart_delete) | **DELETE** /cart.delete.json | 
[**cart_disconnect**](CartApi.md#cart_disconnect) | **GET** /cart.disconnect.json | 
[**cart_giftcard_add**](CartApi.md#cart_giftcard_add) | **POST** /cart.giftcard.add.json | 
[**cart_giftcard_count**](CartApi.md#cart_giftcard_count) | **GET** /cart.giftcard.count.json | 
[**cart_giftcard_list**](CartApi.md#cart_giftcard_list) | **GET** /cart.giftcard.list.json | 
[**cart_info**](CartApi.md#cart_info) | **GET** /cart.info.json | 
[**cart_list**](CartApi.md#cart_list) | **GET** /cart.list.json | 
[**cart_meta_data_list**](CartApi.md#cart_meta_data_list) | **GET** /cart.meta_data.list.json | 
[**cart_meta_data_set**](CartApi.md#cart_meta_data_set) | **POST** /cart.meta_data.set.json | 
[**cart_meta_data_unset**](CartApi.md#cart_meta_data_unset) | **DELETE** /cart.meta_data.unset.json | 
[**cart_methods**](CartApi.md#cart_methods) | **GET** /cart.methods.json | 
[**cart_plugin_list**](CartApi.md#cart_plugin_list) | **GET** /cart.plugin.list.json | 
[**cart_script_add**](CartApi.md#cart_script_add) | **POST** /cart.script.add.json | 
[**cart_script_delete**](CartApi.md#cart_script_delete) | **DELETE** /cart.script.delete.json | 
[**cart_script_list**](CartApi.md#cart_script_list) | **GET** /cart.script.list.json | 
[**cart_shipping_zones_list**](CartApi.md#cart_shipping_zones_list) | **GET** /cart.shipping_zones.list.json | 
[**cart_validate**](CartApi.md#cart_validate) | **GET** /cart.validate.json | 


# **bridge_download**
> file bridge_download(whitelabel=whitelabel)



Download bridge for store

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
whitelabel = false # bool | Identifies if there is a necessity to download whitelabel bridge. (optional) (default to false)

try:
    api_response = api_instance.bridge_download(whitelabel=whitelabel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->bridge_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whitelabel** | **bool**| Identifies if there is a necessity to download whitelabel bridge. | [optional] [default to false]

### Return type

[**file**](file.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_bridge**
> InlineResponse2009 cart_bridge()



Get bridge key and store key

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

# create an instance of the API class
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.cart_bridge()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_bridge: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_catalog_price_rules_count**
> InlineResponse20020 cart_catalog_price_rules_count()



Get count of cart catalog price rules discounts.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.cart_catalog_price_rules_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_catalog_price_rules_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_catalog_price_rules_list**
> ModelResponseCartCatalogPriceRulesList cart_catalog_price_rules_list(page_cursor=page_cursor, start=start, count=count, ids=ids, params=params, exclude=exclude)



Get cart catalog price rules discounts.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
ids = 'ids_example' # str | Retrieves  catalog_price_rules by ids (optional)
params = 'id,name,description' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_catalog_price_rules_list(page_cursor=page_cursor, start=start, count=count, ids=ids, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_catalog_price_rules_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **ids** | **str**| Retrieves  catalog_price_rules by ids | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartCatalogPriceRulesList**](ModelResponseCartCatalogPriceRulesList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_clear_cache**
> InlineResponse20024 cart_clear_cache(cache_type)



Clear cache on store.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
cache_type = 'cache_type_example' # str | Defines which cache should be cleared.

try:
    api_response = api_instance.cart_clear_cache(cache_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_clear_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_type** | **str**| Defines which cache should be cleared. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_config**
> InlineResponse20013 cart_config(params=params, exclude=exclude)



Get list of cart configs

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
params = 'store_name,store_url,db_prefix' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to store_name,store_url,db_prefix)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_config(params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to store_name,store_url,db_prefix]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_config_update**
> InlineResponse20014 cart_config_update(body)



Use this API method to update custom data in client database.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
body = swagger_client.CartConfigUpdate() # CartConfigUpdate | 

try:
    api_response = api_instance.cart_config_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_config_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartConfigUpdate**](CartConfigUpdate.md)|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_coupon_add**
> InlineResponse20018 cart_coupon_add(body)



Create new coupon

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
body = swagger_client.CartCouponAdd() # CartCouponAdd | 

try:
    api_response = api_instance.cart_coupon_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_coupon_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartCouponAdd**](CartCouponAdd.md)|  | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_coupon_condition_add**
> InlineResponse20019 cart_coupon_condition_add(coupon_id, entity, key, operator, value, store_id=store_id, target=target)



Create new coupon condition

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
coupon_id = 'coupon_id_example' # str | Coupon Id
entity = 'entity_example' # str | Defines condition entity type
key = 'key_example' # str | Defines condition entity attribute key
operator = 'operator_example' # str | Defines condition operator
value = 'value_example' # str | Defines condition value, can be comma separated according to the operator.
store_id = 'store_id_example' # str | Store Id (optional)
target = 'coupon_prerequisite' # str | Defines condition operator (optional) (default to coupon_prerequisite)

try:
    api_response = api_instance.cart_coupon_condition_add(coupon_id, entity, key, operator, value, store_id=store_id, target=target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_coupon_condition_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_id** | **str**| Coupon Id | 
 **entity** | **str**| Defines condition entity type | 
 **key** | **str**| Defines condition entity attribute key | 
 **operator** | **str**| Defines condition operator | 
 **value** | **str**| Defines condition value, can be comma separated according to the operator. | 
 **store_id** | **str**| Store Id | [optional] 
 **target** | **str**| Defines condition operator | [optional] [default to coupon_prerequisite]

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_coupon_count**
> InlineResponse20015 cart_coupon_count(store_id=store_id, date_start_from=date_start_from, date_start_to=date_start_to, date_end_from=date_end_from, date_end_to=date_end_to, avail=avail)



Get cart coupons count.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | Store Id (optional)
date_start_from = 'date_start_from_example' # str | Filter entity by date_start (greater or equal) (optional)
date_start_to = 'date_start_to_example' # str | Filter entity by date_start (less or equal) (optional)
date_end_from = 'date_end_from_example' # str | Filter entity by date_end (greater or equal) (optional)
date_end_to = 'date_end_to_example' # str | Filter entity by date_end (less or equal) (optional)
avail = true # bool | Defines category's visibility status (optional) (default to true)

try:
    api_response = api_instance.cart_coupon_count(store_id=store_id, date_start_from=date_start_from, date_start_to=date_start_to, date_end_from=date_end_from, date_end_to=date_end_to, avail=avail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_coupon_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store Id | [optional] 
 **date_start_from** | **str**| Filter entity by date_start (greater or equal) | [optional] 
 **date_start_to** | **str**| Filter entity by date_start (less or equal) | [optional] 
 **date_end_from** | **str**| Filter entity by date_end (greater or equal) | [optional] 
 **date_end_to** | **str**| Filter entity by date_end (less or equal) | [optional] 
 **avail** | **bool**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_coupon_delete**
> InlineResponse2004 cart_coupon_delete(id, store_id=store_id)



Delete coupon

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_coupon_delete(id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_coupon_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_coupon_list**
> ModelResponseCartCouponList cart_coupon_list(page_cursor=page_cursor, start=start, count=count, coupons_ids=coupons_ids, store_id=store_id, date_start_from=date_start_from, date_start_to=date_start_to, date_end_from=date_end_from, date_end_to=date_end_to, avail=avail, lang_id=lang_id, params=params, exclude=exclude)



Get cart coupon discounts.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
coupons_ids = 'coupons_ids_example' # str | Filter coupons by ids (optional)
store_id = 'store_id_example' # str | Filter coupons by store id (optional)
date_start_from = 'date_start_from_example' # str | Filter entity by date_start (greater or equal) (optional)
date_start_to = 'date_start_to_example' # str | Filter entity by date_start (less or equal) (optional)
date_end_from = 'date_end_from_example' # str | Filter entity by date_end (greater or equal) (optional)
date_end_to = 'date_end_to_example' # str | Filter entity by date_end (less or equal) (optional)
avail = true # bool | Filter coupons by avail status (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_coupon_list(page_cursor=page_cursor, start=start, count=count, coupons_ids=coupons_ids, store_id=store_id, date_start_from=date_start_from, date_start_to=date_start_to, date_end_from=date_end_from, date_end_to=date_end_to, avail=avail, lang_id=lang_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_coupon_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **coupons_ids** | **str**| Filter coupons by ids | [optional] 
 **store_id** | **str**| Filter coupons by store id | [optional] 
 **date_start_from** | **str**| Filter entity by date_start (greater or equal) | [optional] 
 **date_start_to** | **str**| Filter entity by date_start (less or equal) | [optional] 
 **date_end_from** | **str**| Filter entity by date_end (greater or equal) | [optional] 
 **date_end_to** | **str**| Filter entity by date_end (less or equal) | [optional] 
 **avail** | **bool**| Filter coupons by avail status | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartCouponList**](ModelResponseCartCouponList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_create**
> InlineResponse2006 cart_create(cart_id, store_url, store_id, bridge_url=bridge_url, store_root=store_root, store_key=store_key, shared_secret=shared_secret, validate_version=validate_version, verify=verify, db_tables_prefix=db_tables_prefix, ftp_host=ftp_host, ftp_user=ftp_user, ftp_password=ftp_password, ftp_port=ftp_port, ftp_store_dir=ftp_store_dir, api_key_3dcart=api_key_3dcart, admin_account=admin_account, api_path=api_path, api_key=api_key, client_id=client_id, access_token=access_token, context=context, access_token2=access_token2, api_key_shopify=api_key_shopify, api_password=api_password, access_token_shopify=access_token_shopify, api_key2=api_key2, api_username=api_username, encrypted_password=encrypted_password, login=login, api_user_adnsf=api_user_adnsf, api_pass=api_pass, access_key_scelite=access_key_scelite, api_key_scelite=api_key_scelite, api_secret_key_scelite=api_secret_key_scelite, private_key=private_key, app_token=app_token, etsy_keystring=etsy_keystring, etsy_shared_secret=etsy_shared_secret, token_secret=token_secret, ebay_client_id=ebay_client_id, ebay_client_secret=ebay_client_secret, ebay_runame=ebay_runame, ebay_access_token=ebay_access_token, ebay_refresh_token=ebay_refresh_token, ebay_environment=ebay_environment, ebay_site_id=ebay_site_id, dw_client_id=dw_client_id, dw_api_pass=dw_api_pass, demandware_user_name=demandware_user_name, demandware_user_password=demandware_user_password, seller_id=seller_id, amazon_secret_key=amazon_secret_key, amazon_access_key_id=amazon_access_key_id, marketplaces_ids=marketplaces_ids, environment=environment, hybris_client_id=hybris_client_id, hybris_client_secret=hybris_client_secret, hybris_username=hybris_username, hybris_password=hybris_password, hybris_websites=hybris_websites, walmart_client_id=walmart_client_id, walmart_client_secret=walmart_client_secret, walmart_environment=walmart_environment, walmart_channel_type=walmart_channel_type, lightspeed_api_key=lightspeed_api_key, lightspeed_api_secret=lightspeed_api_secret, shopware_api_key=shopware_api_key, shopware_api_secret=shopware_api_secret, commercehq_api_key=commercehq_api_key, commercehq_api_password=commercehq_api_password)



Add store to the account

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

# create an instance of the API class
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
cart_id = 'cart_id_example' # str | Store’s identifier which you can get from cart_list method
store_url = 'store_url_example' # str | A web address of a store that you would like to connect to API2Cart
store_id = 'store_id_example' # str | Store Id
bridge_url = 'bridge_url_example' # str | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) (optional)
store_root = 'store_root_example' # str | Absolute path to the store root directory (used with \"bridge_url\" parameter) (optional)
store_key = 'store_key_example' # str | Set this parameter if bridge is already uploaded to store (optional)
shared_secret = 'shared_secret_example' # str | Shared secret (optional)
validate_version = false # bool | Specify if api2cart should validate cart version (optional) (default to false)
verify = true # bool | Enables or disables cart's verification (optional) (default to true)
db_tables_prefix = 'db_tables_prefix_example' # str | DB tables prefix (optional)
ftp_host = 'ftp_host_example' # str | FTP connection host (optional)
ftp_user = 'ftp_user_example' # str | FTP User (optional)
ftp_password = 'ftp_password_example' # str | FTP Password (optional)
ftp_port = 56 # int | FTP Port (optional)
ftp_store_dir = 'ftp_store_dir_example' # str | FTP Store dir (optional)
api_key_3dcart = 'api_key_3dcart_example' # str | 3DCart API Key (optional)
admin_account = 'admin_account_example' # str | It's a BigCommerce account for which API is enabled (optional)
api_path = 'api_path_example' # str | BigCommerce API URL (optional)
api_key = 'api_key_example' # str | Bigcommerce API Key (optional)
client_id = 'client_id_example' # str | Client ID of the requesting app (optional)
access_token = 'access_token_example' # str | Access token authorizing the app to access resources on behalf of a user (optional)
context = 'context_example' # str | API Path section unique to the store (optional)
access_token2 = 'access_token_example' # str | Access token authorizing the app to access resources on behalf of a user (optional)
api_key_shopify = 'api_key_shopify_example' # str | Shopify API Key (optional)
api_password = 'api_password_example' # str | Shopify API Password (optional)
access_token_shopify = 'access_token_shopify_example' # str | Access token authorizing the app to access resources on behalf of a user (optional)
api_key2 = 'api_key_example' # str | Neto API Key (optional)
api_username = 'api_username_example' # str | Neto User Name (optional)
encrypted_password = 'encrypted_password_example' # str | Volusion API Password (optional)
login = 'login_example' # str | It's a Volusion account for which API is enabled (optional)
api_user_adnsf = 'api_user_adnsf_example' # str | It's a AspDotNetStorefront account for which API is available (optional)
api_pass = 'api_pass_example' # str | AspDotNetStorefront API Password (optional)
access_key_scelite = 'access_key_scelite_example' # str | Shopping Cart Elite Access Key (optional)
api_key_scelite = 'api_key_scelite_example' # str | Shopping Cart Elite API Key (optional)
api_secret_key_scelite = 'api_secret_key_scelite_example' # str | Shopping Cart Elite API Secret Key (optional)
private_key = 'private_key_example' # str | 3DCart Application Private Key (optional)
app_token = 'app_token_example' # str | 3DCart Token from Application (optional)
etsy_keystring = 'etsy_keystring_example' # str | Etsy keystring (optional)
etsy_shared_secret = 'etsy_shared_secret_example' # str | Etsy shared secret (optional)
token_secret = 'token_secret_example' # str | Secret token authorizing the app to access resources on behalf of a user (optional)
ebay_client_id = 'ebay_client_id_example' # str | Application ID (AppID). (optional)
ebay_client_secret = 'ebay_client_secret_example' # str | Shared Secret from eBay application (optional)
ebay_runame = 'ebay_runame_example' # str | The RuName value that eBay assigns to your application. (optional)
ebay_access_token = 'ebay_access_token_example' # str | Used to authenticate API requests. (optional)
ebay_refresh_token = 'ebay_refresh_token_example' # str | Used to renew the access token. (optional)
ebay_environment = 'production' # str | eBay environment (optional) (default to production)
ebay_site_id = 0 # int | eBay global ID (optional) (default to 0)
dw_client_id = 'dw_client_id_example' # str | Demandware client id (optional)
dw_api_pass = 'dw_api_pass_example' # str | Demandware api password (optional)
demandware_user_name = 'demandware_user_name_example' # str | Demandware user name (optional)
demandware_user_password = 'demandware_user_password_example' # str | Demandware user password (optional)
seller_id = 'seller_id_example' # str | Seller Id (optional)
amazon_secret_key = 'amazon_secret_key_example' # str | Amazon Secret Key (optional)
amazon_access_key_id = 'amazon_access_key_id_example' # str | Amazon Secret Key Id (optional)
marketplaces_ids = 'marketplaces_ids_example' # str | Comma separated marketplaces ids (optional)
environment = 'production' # str |  (optional) (default to production)
hybris_client_id = 'hybris_client_id_example' # str | Omni Commerce Connector Client ID (optional)
hybris_client_secret = 'hybris_client_secret_example' # str | Omni Commerce Connector Client Secret (optional)
hybris_username = 'hybris_username_example' # str | User Name (optional)
hybris_password = 'hybris_password_example' # str | User password (optional)
hybris_websites = ['hybris_websites_example'] # list[str] | Websites to stores mapping data (optional)
walmart_client_id = 'walmart_client_id_example' # str | Walmart client ID (optional)
walmart_client_secret = 'walmart_client_secret_example' # str | Walmart client secret (optional)
walmart_environment = 'production' # str | Walmart environment (optional) (default to production)
walmart_channel_type = 'walmart_channel_type_example' # str | Walmart WM_CONSUMER.CHANNEL.TYPE header (optional)
lightspeed_api_key = 'lightspeed_api_key_example' # str | LightSpeed api key (optional)
lightspeed_api_secret = 'lightspeed_api_secret_example' # str | LightSpeed api secret (optional)
shopware_api_key = 'shopware_api_key_example' # str | Shopware api key (optional)
shopware_api_secret = 'shopware_api_secret_example' # str | Shopware client secret access key (optional)
commercehq_api_key = 'commercehq_api_key_example' # str | CommerceHQ api key (optional)
commercehq_api_password = 'commercehq_api_password_example' # str | CommerceHQ api password (optional)

try:
    api_response = api_instance.cart_create(cart_id, store_url, store_id, bridge_url=bridge_url, store_root=store_root, store_key=store_key, shared_secret=shared_secret, validate_version=validate_version, verify=verify, db_tables_prefix=db_tables_prefix, ftp_host=ftp_host, ftp_user=ftp_user, ftp_password=ftp_password, ftp_port=ftp_port, ftp_store_dir=ftp_store_dir, api_key_3dcart=api_key_3dcart, admin_account=admin_account, api_path=api_path, api_key=api_key, client_id=client_id, access_token=access_token, context=context, access_token2=access_token2, api_key_shopify=api_key_shopify, api_password=api_password, access_token_shopify=access_token_shopify, api_key2=api_key2, api_username=api_username, encrypted_password=encrypted_password, login=login, api_user_adnsf=api_user_adnsf, api_pass=api_pass, access_key_scelite=access_key_scelite, api_key_scelite=api_key_scelite, api_secret_key_scelite=api_secret_key_scelite, private_key=private_key, app_token=app_token, etsy_keystring=etsy_keystring, etsy_shared_secret=etsy_shared_secret, token_secret=token_secret, ebay_client_id=ebay_client_id, ebay_client_secret=ebay_client_secret, ebay_runame=ebay_runame, ebay_access_token=ebay_access_token, ebay_refresh_token=ebay_refresh_token, ebay_environment=ebay_environment, ebay_site_id=ebay_site_id, dw_client_id=dw_client_id, dw_api_pass=dw_api_pass, demandware_user_name=demandware_user_name, demandware_user_password=demandware_user_password, seller_id=seller_id, amazon_secret_key=amazon_secret_key, amazon_access_key_id=amazon_access_key_id, marketplaces_ids=marketplaces_ids, environment=environment, hybris_client_id=hybris_client_id, hybris_client_secret=hybris_client_secret, hybris_username=hybris_username, hybris_password=hybris_password, hybris_websites=hybris_websites, walmart_client_id=walmart_client_id, walmart_client_secret=walmart_client_secret, walmart_environment=walmart_environment, walmart_channel_type=walmart_channel_type, lightspeed_api_key=lightspeed_api_key, lightspeed_api_secret=lightspeed_api_secret, shopware_api_key=shopware_api_key, shopware_api_secret=shopware_api_secret, commercehq_api_key=commercehq_api_key, commercehq_api_password=commercehq_api_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Store’s identifier which you can get from cart_list method | 
 **store_url** | **str**| A web address of a store that you would like to connect to API2Cart | 
 **store_id** | **str**| Store Id | 
 **bridge_url** | **str**| This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] 
 **store_root** | **str**| Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] 
 **store_key** | **str**| Set this parameter if bridge is already uploaded to store | [optional] 
 **shared_secret** | **str**| Shared secret | [optional] 
 **validate_version** | **bool**| Specify if api2cart should validate cart version | [optional] [default to false]
 **verify** | **bool**| Enables or disables cart&#39;s verification | [optional] [default to true]
 **db_tables_prefix** | **str**| DB tables prefix | [optional] 
 **ftp_host** | **str**| FTP connection host | [optional] 
 **ftp_user** | **str**| FTP User | [optional] 
 **ftp_password** | **str**| FTP Password | [optional] 
 **ftp_port** | **int**| FTP Port | [optional] 
 **ftp_store_dir** | **str**| FTP Store dir | [optional] 
 **api_key_3dcart** | **str**| 3DCart API Key | [optional] 
 **admin_account** | **str**| It&#39;s a BigCommerce account for which API is enabled | [optional] 
 **api_path** | **str**| BigCommerce API URL | [optional] 
 **api_key** | **str**| Bigcommerce API Key | [optional] 
 **client_id** | **str**| Client ID of the requesting app | [optional] 
 **access_token** | **str**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **context** | **str**| API Path section unique to the store | [optional] 
 **access_token2** | **str**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **api_key_shopify** | **str**| Shopify API Key | [optional] 
 **api_password** | **str**| Shopify API Password | [optional] 
 **access_token_shopify** | **str**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **api_key2** | **str**| Neto API Key | [optional] 
 **api_username** | **str**| Neto User Name | [optional] 
 **encrypted_password** | **str**| Volusion API Password | [optional] 
 **login** | **str**| It&#39;s a Volusion account for which API is enabled | [optional] 
 **api_user_adnsf** | **str**| It&#39;s a AspDotNetStorefront account for which API is available | [optional] 
 **api_pass** | **str**| AspDotNetStorefront API Password | [optional] 
 **access_key_scelite** | **str**| Shopping Cart Elite Access Key | [optional] 
 **api_key_scelite** | **str**| Shopping Cart Elite API Key | [optional] 
 **api_secret_key_scelite** | **str**| Shopping Cart Elite API Secret Key | [optional] 
 **private_key** | **str**| 3DCart Application Private Key | [optional] 
 **app_token** | **str**| 3DCart Token from Application | [optional] 
 **etsy_keystring** | **str**| Etsy keystring | [optional] 
 **etsy_shared_secret** | **str**| Etsy shared secret | [optional] 
 **token_secret** | **str**| Secret token authorizing the app to access resources on behalf of a user | [optional] 
 **ebay_client_id** | **str**| Application ID (AppID). | [optional] 
 **ebay_client_secret** | **str**| Shared Secret from eBay application | [optional] 
 **ebay_runame** | **str**| The RuName value that eBay assigns to your application. | [optional] 
 **ebay_access_token** | **str**| Used to authenticate API requests. | [optional] 
 **ebay_refresh_token** | **str**| Used to renew the access token. | [optional] 
 **ebay_environment** | **str**| eBay environment | [optional] [default to production]
 **ebay_site_id** | **int**| eBay global ID | [optional] [default to 0]
 **dw_client_id** | **str**| Demandware client id | [optional] 
 **dw_api_pass** | **str**| Demandware api password | [optional] 
 **demandware_user_name** | **str**| Demandware user name | [optional] 
 **demandware_user_password** | **str**| Demandware user password | [optional] 
 **seller_id** | **str**| Seller Id | [optional] 
 **amazon_secret_key** | **str**| Amazon Secret Key | [optional] 
 **amazon_access_key_id** | **str**| Amazon Secret Key Id | [optional] 
 **marketplaces_ids** | **str**| Comma separated marketplaces ids | [optional] 
 **environment** | **str**|  | [optional] [default to production]
 **hybris_client_id** | **str**| Omni Commerce Connector Client ID | [optional] 
 **hybris_client_secret** | **str**| Omni Commerce Connector Client Secret | [optional] 
 **hybris_username** | **str**| User Name | [optional] 
 **hybris_password** | **str**| User password | [optional] 
 **hybris_websites** | [**list[str]**](str.md)| Websites to stores mapping data | [optional] 
 **walmart_client_id** | **str**| Walmart client ID | [optional] 
 **walmart_client_secret** | **str**| Walmart client secret | [optional] 
 **walmart_environment** | **str**| Walmart environment | [optional] [default to production]
 **walmart_channel_type** | **str**| Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] 
 **lightspeed_api_key** | **str**| LightSpeed api key | [optional] 
 **lightspeed_api_secret** | **str**| LightSpeed api secret | [optional] 
 **shopware_api_key** | **str**| Shopware api key | [optional] 
 **shopware_api_secret** | **str**| Shopware client secret access key | [optional] 
 **commercehq_api_key** | **str**| CommerceHQ api key | [optional] 
 **commercehq_api_password** | **str**| CommerceHQ api password | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_delete**
> InlineResponse20010 cart_delete(delete_bridge=delete_bridge)



Remove store from API2Cart

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
delete_bridge = true # bool | Identifies if there is a necessity to delete bridge (optional) (default to true)

try:
    api_response = api_instance.cart_delete(delete_bridge=delete_bridge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_bridge** | **bool**| Identifies if there is a necessity to delete bridge | [optional] [default to true]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_disconnect**
> InlineResponse20011 cart_disconnect(delete_bridge=delete_bridge)



Disconnect with the store and clear store session data.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
delete_bridge = false # bool | Identifies if there is a necessity to delete bridge (optional) (default to false)

try:
    api_response = api_instance.cart_disconnect(delete_bridge=delete_bridge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_disconnect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_bridge** | **bool**| Identifies if there is a necessity to delete bridge | [optional] [default to false]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_giftcard_add**
> InlineResponse20017 cart_giftcard_add(amount, code=code, owner_email=owner_email)



Create new gift card

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
amount = 8.14 # float | Defines the gift card amount value.
code = 'code_example' # str | Gift card code (optional)
owner_email = 'owner_email_example' # str | Gift card owner email (optional)

try:
    api_response = api_instance.cart_giftcard_add(amount, code=code, owner_email=owner_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_giftcard_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**| Defines the gift card amount value. | 
 **code** | **str**| Gift card code | [optional] 
 **owner_email** | **str**| Gift card owner email | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_giftcard_count**
> InlineResponse20016 cart_giftcard_count(store_id=store_id)



Get gift cards count.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_giftcard_count(store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_giftcard_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_giftcard_list**
> ModelResponseCartGiftCardList cart_giftcard_list(page_cursor=page_cursor, start=start, count=count, store_id=store_id, params=params, exclude=exclude)



Get gift cards list.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
store_id = 'store_id_example' # str | Store Id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_giftcard_list(page_cursor=page_cursor, start=start, count=count, store_id=store_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_giftcard_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **store_id** | **str**| Store Id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartGiftCardList**](ModelResponseCartGiftCardList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_info**
> InlineResponse20023 cart_info(params=params, exclude=exclude, store_id=store_id)



Get cart information

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
params = 'store_name,store_url,db_prefix' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to store_name,store_url,db_prefix)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_info(params=params, exclude=exclude, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to store_name,store_url,db_prefix]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_list**
> InlineResponse2008 cart_list()



Get list of supported carts

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

# create an instance of the API class
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.cart_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_meta_data_list**
> ModelResponseCartMetaDataList cart_meta_data_list(entity_id, entity=entity, store_id=store_id, key=key, count=count, page_cursor=page_cursor, params=params, exclude=exclude)



Get entity meta data

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Entity Id
entity = 'product' # str | Entity (optional) (default to product)
store_id = 'store_id_example' # str | Store Id (optional)
key = 'key_example' # str | Key (optional)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
params = 'key,value' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to key,value)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_meta_data_list(entity_id, entity=entity, store_id=store_id, key=key, count=count, page_cursor=page_cursor, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_meta_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity Id | 
 **entity** | **str**| Entity | [optional] [default to product]
 **store_id** | **str**| Store Id | [optional] 
 **key** | **str**| Key | [optional] 
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to key,value]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartMetaDataList**](ModelResponseCartMetaDataList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_meta_data_set**
> InlineResponse200 cart_meta_data_set(entity_id, key, value, entity=entity, store_id=store_id)



Set meta data for a specific entity

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Entity Id
key = 'key_example' # str | Key
value = 'value_example' # str | Value
entity = 'product' # str | Entity (optional) (default to product)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_meta_data_set(entity_id, key, value, entity=entity, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_meta_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity Id | 
 **key** | **str**| Key | 
 **value** | **str**| Value | 
 **entity** | **str**| Entity | [optional] [default to product]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_meta_data_unset**
> InlineResponse20019 cart_meta_data_unset(entity_id, key, entity=entity, store_id=store_id)



Unset meta data for a specific entity

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Entity Id
key = 'key_example' # str | Key
entity = 'product' # str | Entity (optional) (default to product)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_meta_data_unset(entity_id, key, entity=entity, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_meta_data_unset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity Id | 
 **key** | **str**| Key | 
 **entity** | **str**| Entity | [optional] [default to product]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_methods**
> InlineResponse20012 cart_methods()



Get list of cart methods

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.cart_methods()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_methods: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_plugin_list**
> InlineResponse20025 cart_plugin_list(store_key=store_key, store_id=store_id, start=start, count=count)



Get list of installed plugins

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
store_key = 'store_key_example' # str | Set this parameter if bridge is already uploaded to store (optional)
store_id = 'store_id_example' # str | Store Id (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)

try:
    api_response = api_instance.cart_plugin_list(store_key=store_key, store_id=store_id, start=start, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_plugin_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_key** | **str**| Set this parameter if bridge is already uploaded to store | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_script_add**
> InlineResponse20021 cart_script_add(name=name, description=description, html=html, src=src, load_method=load_method, scope=scope, store_id=store_id)



Add new script to the storefront

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The user-friendly script name (optional)
description = 'description_example' # str | The user-friendly description (optional)
html = 'html_example' # str | An html string containing exactly one `script` tag. (optional)
src = 'src_example' # str | The URL of the remote script (optional)
load_method = 'load_method_example' # str | The load method to use for the script (optional)
scope = 'storefront' # str | The page or pages on the online store where the script should be included (optional) (default to storefront)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_script_add(name=name, description=description, html=html, src=src, load_method=load_method, scope=scope, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_script_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user-friendly script name | [optional] 
 **description** | **str**| The user-friendly description | [optional] 
 **html** | **str**| An html string containing exactly one &#x60;script&#x60; tag. | [optional] 
 **src** | **str**| The URL of the remote script | [optional] 
 **load_method** | **str**| The load method to use for the script | [optional] 
 **scope** | **str**| The page or pages on the online store where the script should be included | [optional] [default to storefront]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_script_delete**
> InlineResponse20022 cart_script_delete(id, store_id=store_id)



Remove script from the storefront

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_script_delete(id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_script_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_script_list**
> ModelResponseCartScriptList cart_script_list(page_cursor=page_cursor, start=start, count=count, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, script_ids=script_ids, store_id=store_id, params=params, exclude=exclude)



Get scripts installed to the storefront

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
script_ids = 'script_ids_example' # str | Retrieves only scripts with specific ids (optional)
store_id = 'store_id_example' # str | Store Id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.cart_script_list(page_cursor=page_cursor, start=start, count=count, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, script_ids=script_ids, store_id=store_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_script_list: %s\n" % e)
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
 **script_ids** | **str**| Retrieves only scripts with specific ids | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartScriptList**](ModelResponseCartScriptList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_shipping_zones_list**
> InlineResponse20026 cart_shipping_zones_list(store_id=store_id)



Get list of shipping zones

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.cart_shipping_zones_list(store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_shipping_zones_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_validate**
> InlineResponse2007 cart_validate(validate_version=validate_version)



Check store availability, bridge connection for the downloadable carts, identify DB prefix, validate API accesses for API carts.

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
validate_version = false # bool | Specify if api2cart should validate cart version (optional) (default to false)

try:
    api_response = api_instance.cart_validate(validate_version=validate_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->cart_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_version** | **bool**| Specify if api2cart should validate cart version | [optional] [default to false]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

