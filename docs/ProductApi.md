# swagger_client.ProductApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_add**](ProductApi.md#product_add) | **POST** /product.add.json | 
[**product_attribute_list**](ProductApi.md#product_attribute_list) | **GET** /product.attribute.list.json | 
[**product_attribute_value_set**](ProductApi.md#product_attribute_value_set) | **POST** /product.attribute.value.set.json | 
[**product_attribute_value_unset**](ProductApi.md#product_attribute_value_unset) | **POST** /product.attribute.value.unset.json | 
[**product_brand_list**](ProductApi.md#product_brand_list) | **GET** /product.brand.list.json | 
[**product_child_item_find**](ProductApi.md#product_child_item_find) | **GET** /product.child_item.find.json | 
[**product_child_item_info**](ProductApi.md#product_child_item_info) | **GET** /product.child_item.info.json | 
[**product_child_item_list**](ProductApi.md#product_child_item_list) | **GET** /product.child_item.list.json | 
[**product_count**](ProductApi.md#product_count) | **GET** /product.count.json | 
[**product_currency_add**](ProductApi.md#product_currency_add) | **POST** /product.currency.add.json | 
[**product_currency_list**](ProductApi.md#product_currency_list) | **GET** /product.currency.list.json | 
[**product_delete**](ProductApi.md#product_delete) | **DELETE** /product.delete.json | 
[**product_fields**](ProductApi.md#product_fields) | **GET** /product.fields.json | 
[**product_find**](ProductApi.md#product_find) | **GET** /product.find.json | 
[**product_image_add**](ProductApi.md#product_image_add) | **POST** /product.image.add.json | 
[**product_image_delete**](ProductApi.md#product_image_delete) | **DELETE** /product.image.delete.json | 
[**product_image_update**](ProductApi.md#product_image_update) | **PUT** /product.image.update.json | 
[**product_info**](ProductApi.md#product_info) | **GET** /product.info.json | 
[**product_list**](ProductApi.md#product_list) | **GET** /product.list.json | 
[**product_manufacturer_add**](ProductApi.md#product_manufacturer_add) | **POST** /product.manufacturer.add.json | 
[**product_option_add**](ProductApi.md#product_option_add) | **POST** /product.option.add.json | 
[**product_option_assign**](ProductApi.md#product_option_assign) | **POST** /product.option.assign.json | 
[**product_option_list**](ProductApi.md#product_option_list) | **GET** /product.option.list.json | 
[**product_option_value_add**](ProductApi.md#product_option_value_add) | **POST** /product.option.value.add.json | 
[**product_option_value_assign**](ProductApi.md#product_option_value_assign) | **POST** /product.option.value.assign.json | 
[**product_option_value_update**](ProductApi.md#product_option_value_update) | **PUT** /product.option.value.update.json | 
[**product_price_add**](ProductApi.md#product_price_add) | **POST** /product.price.add.json | 
[**product_price_delete**](ProductApi.md#product_price_delete) | **DELETE** /product.price.delete.json | 
[**product_price_update**](ProductApi.md#product_price_update) | **PUT** /product.price.update.json | 
[**product_review_list**](ProductApi.md#product_review_list) | **GET** /product.review.list.json | 
[**product_store_assign**](ProductApi.md#product_store_assign) | **POST** /product.store.assign.json | 
[**product_tax_add**](ProductApi.md#product_tax_add) | **POST** /product.tax.add.json | 
[**product_update**](ProductApi.md#product_update) | **PUT** /product.update.json | 
[**product_variant_add**](ProductApi.md#product_variant_add) | **POST** /product.variant.add.json | 
[**product_variant_count**](ProductApi.md#product_variant_count) | **GET** /product.variant.count.json | 
[**product_variant_delete**](ProductApi.md#product_variant_delete) | **DELETE** /product.variant.delete.json | 
[**product_variant_image_add**](ProductApi.md#product_variant_image_add) | **POST** /product.variant.image.add.json | 
[**product_variant_info**](ProductApi.md#product_variant_info) | **GET** /product.variant.info.json | 
[**product_variant_list**](ProductApi.md#product_variant_list) | **GET** /product.variant.list.json | 
[**product_variant_price_add**](ProductApi.md#product_variant_price_add) | **POST** /product.variant.price.add.json | 
[**product_variant_price_delete**](ProductApi.md#product_variant_price_delete) | **DELETE** /product.variant.price.delete.json | 
[**product_variant_price_update**](ProductApi.md#product_variant_price_update) | **PUT** /product.variant.price.update.json | 
[**product_variant_update**](ProductApi.md#product_variant_update) | **PUT** /product.variant.update.json | 


# **product_add**
> InlineResponse20035 product_add(body)



Add new product to store.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductAdd() # ProductAdd | 

try:
    api_response = api_instance.product_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAdd**](ProductAdd.md)|  | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_list**
> ModelResponseProductAttributeList product_attribute_list(product_id, page_cursor=page_cursor, start=start, count=count, variant_id=variant_id, attribute_id=attribute_id, attribute_group_id=attribute_group_id, set_name=set_name, lang_id=lang_id, store_id=store_id, sort_by=sort_by, sort_direction=sort_direction, params=params, exclude=exclude)



Get list of attributes and values.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Retrieves attributes specified by product id
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
variant_id = 'variant_id_example' # str | Defines product's variants specified by variant id (optional)
attribute_id = 'attribute_id_example' # str | Retrieves info for specified attribute_id (optional)
attribute_group_id = 'attribute_group_id_example' # str | Filter by attribute_group_id (optional)
set_name = 'set_name_example' # str | Retrieves attributes specified by set_name in Magento (optional)
lang_id = 'lang_id_example' # str | Retrieves attributes specified by language id (optional)
store_id = 'store_id_example' # str | Retrieves attributes specified by store id (optional)
sort_by = 'attribute_id' # str | Set field to sort by (optional) (default to attribute_id)
sort_direction = 'asc' # str | Set sorting direction (optional) (default to asc)
params = 'attribute_id,name' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to attribute_id,name)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.product_attribute_list(product_id, page_cursor=page_cursor, start=start, count=count, variant_id=variant_id, attribute_id=attribute_id, attribute_group_id=attribute_group_id, set_name=set_name, lang_id=lang_id, store_id=store_id, sort_by=sort_by, sort_direction=sort_direction, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_attribute_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Retrieves attributes specified by product id | 
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **variant_id** | **str**| Defines product&#39;s variants specified by variant id | [optional] 
 **attribute_id** | **str**| Retrieves info for specified attribute_id | [optional] 
 **attribute_group_id** | **str**| Filter by attribute_group_id | [optional] 
 **set_name** | **str**| Retrieves attributes specified by set_name in Magento | [optional] 
 **lang_id** | **str**| Retrieves attributes specified by language id | [optional] 
 **store_id** | **str**| Retrieves attributes specified by store id | [optional] 
 **sort_by** | **str**| Set field to sort by | [optional] [default to attribute_id]
 **sort_direction** | **str**| Set sorting direction | [optional] [default to asc]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to attribute_id,name]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseProductAttributeList**](ModelResponseProductAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_value_set**
> InlineResponse20068 product_attribute_value_set(product_id, attribute_id=attribute_id, attribute_group_id=attribute_group_id, attribute_name=attribute_name, value=value, value_id=value_id, lang_id=lang_id, store_id=store_id)



Set attribute value to product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the attribute should be added
attribute_id = 'attribute_id_example' # str | Filter by attribute_id (optional)
attribute_group_id = 'attribute_group_id_example' # str | Filter by attribute_group_id (optional)
attribute_name = 'attribute_name_example' # str | Define attribute name (optional)
value = 'value_example' # str | Define attribute value (optional)
value_id = 56 # int | Define attribute value id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_attribute_value_set(product_id, attribute_id=attribute_id, attribute_group_id=attribute_group_id, attribute_name=attribute_name, value=value, value_id=value_id, lang_id=lang_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_attribute_value_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the attribute should be added | 
 **attribute_id** | **str**| Filter by attribute_id | [optional] 
 **attribute_group_id** | **str**| Filter by attribute_group_id | [optional] 
 **attribute_name** | **str**| Define attribute name | [optional] 
 **value** | **str**| Define attribute value | [optional] 
 **value_id** | **int**| Define attribute value id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_attribute_value_unset**
> InlineResponse20069 product_attribute_value_unset(product_id, attribute_id, store_id=store_id, include_default=include_default, reindex=reindex, clear_cache=clear_cache)



Removes attribute value for a product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Product id
attribute_id = 'attribute_id_example' # str | Attribute Id
store_id = 'store_id_example' # str | Store Id (optional)
include_default = false # bool | Boolean, whether or not to unset default value of the attribute, if applicable (optional) (default to false)
reindex = true # bool | Is reindex required (optional) (default to true)
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_attribute_value_unset(product_id, attribute_id, store_id=store_id, include_default=include_default, reindex=reindex, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_attribute_value_unset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product id | 
 **attribute_id** | **str**| Attribute Id | 
 **store_id** | **str**| Store Id | [optional] 
 **include_default** | **bool**| Boolean, whether or not to unset default value of the attribute, if applicable | [optional] [default to false]
 **reindex** | **bool**| Is reindex required | [optional] [default to true]
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_brand_list**
> InlineResponse20083 product_brand_list(start=start, count=count, params=params, brand_ids=brand_ids, exclude=exclude, store_id=store_id, lang_id=lang_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to)



Get list of brands from your store.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,name,short_description,active,url' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,short_description,active,url)
brand_ids = 'brand_ids_example' # str | Retrieves brands specified by brand ids (optional)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)

try:
    api_response = api_instance.product_brand_list(start=start, count=count, params=params, brand_ids=brand_ids, exclude=exclude, store_id=store_id, lang_id=lang_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_brand_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,short_description,active,url]
 **brand_ids** | **str**| Retrieves brands specified by brand ids | [optional] 
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_child_item_find**
> InlineResponse20078 product_child_item_find(find_value, find_where=find_where, find_params=find_params, store_id=store_id)



Search product child item (bundled item or configurable product variant) in store catalog.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
find_value = 'find_value_example' # str | Entity search that is specified by some value
find_where = 'name' # str | Entity search that is specified by the comma-separated unique fields (optional) (default to name)
find_params = 'whole_words' # str | Entity search that is specified by comma-separated parameters (optional) (default to whole_words)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_child_item_find(find_value, find_where=find_where, find_params=find_params, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_child_item_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_value** | **str**| Entity search that is specified by some value | 
 **find_where** | **str**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name]
 **find_params** | **str**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_child_item_info**
> InlineResponse20077 product_child_item_info(product_id, id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)



Get child for specific product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Filter by parent product id
id = 'id_example' # str | Entity id
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)

try:
    api_response = api_instance.product_child_item_info(product_id, id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_child_item_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Filter by parent product id | 
 **id** | **str**| Entity id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_child_item_list**
> ModelResponseProductChildItemList product_child_item_list(page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, product_id=product_id, product_ids=product_ids, store_id=store_id, lang_id=lang_id, currency_id=currency_id, avail_sale=avail_sale, report_request_id=report_request_id, disable_report_cache=disable_report_cache)



Get child items list of specific product(s).

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve products child items via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
product_id = 'product_id_example' # str | Filter by parent product id (optional)
product_ids = 'product_ids_example' # str | Filter by parent product ids (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
currency_id = 'currency_id_example' # str | Currency Id (optional)
avail_sale = true # bool | Specifies the set of available/not available products for sale (optional)
report_request_id = 'report_request_id_example' # str | Report request id (optional)
disable_report_cache = false # bool | Disable report cache for current request (optional) (default to false)

try:
    api_response = api_instance.product_child_item_list(page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, product_id=product_id, product_ids=product_ids, store_id=store_id, lang_id=lang_id, currency_id=currency_id, avail_sale=avail_sale, report_request_id=report_request_id, disable_report_cache=disable_report_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_child_item_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve products child items via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **product_id** | **str**| Filter by parent product id | [optional] 
 **product_ids** | **str**| Filter by parent product ids | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **currency_id** | **str**| Currency Id | [optional] 
 **avail_sale** | **bool**| Specifies the set of available/not available products for sale | [optional] 
 **report_request_id** | **str**| Report request id | [optional] 
 **disable_report_cache** | **bool**| Disable report cache for current request | [optional] [default to false]

### Return type

[**ModelResponseProductChildItemList**](ModelResponseProductChildItemList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_count**
> InlineResponse20032 product_count(category_id=category_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, avail_view=avail_view, avail_sale=avail_sale, store_id=store_id, lang_id=lang_id, product_ids=product_ids, report_request_id=report_request_id, disable_report_cache=disable_report_cache, brand_name=brand_name, product_attributes=product_attributes)



Count products in store.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str | Counts products specified by category id (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
avail_view = true # bool | Specifies the set of visible/invisible products (optional)
avail_sale = true # bool | Specifies the set of available/not available products for sale (optional)
store_id = 'store_id_example' # str | Counts products specified by store id (optional)
lang_id = 'lang_id_example' # str | Counts products specified by language id (optional)
product_ids = 'product_ids_example' # str | Counts products specified by product ids (optional)
report_request_id = 'report_request_id_example' # str | Report request id (optional)
disable_report_cache = false # bool | Disable report cache for current request (optional) (default to false)
brand_name = 'brand_name_example' # str | Retrieves brands specified by brand name (optional)
product_attributes = ['product_attributes_example'] # list[str] | Defines product attributes (optional)

try:
    api_response = api_instance.product_count(category_id=category_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, avail_view=avail_view, avail_sale=avail_sale, store_id=store_id, lang_id=lang_id, product_ids=product_ids, report_request_id=report_request_id, disable_report_cache=disable_report_cache, brand_name=brand_name, product_attributes=product_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Counts products specified by category id | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **avail_view** | **bool**| Specifies the set of visible/invisible products | [optional] 
 **avail_sale** | **bool**| Specifies the set of available/not available products for sale | [optional] 
 **store_id** | **str**| Counts products specified by store id | [optional] 
 **lang_id** | **str**| Counts products specified by language id | [optional] 
 **product_ids** | **str**| Counts products specified by product ids | [optional] 
 **report_request_id** | **str**| Report request id | [optional] 
 **disable_report_cache** | **bool**| Disable report cache for current request | [optional] [default to false]
 **brand_name** | **str**| Retrieves brands specified by brand name | [optional] 
 **product_attributes** | [**list[str]**](str.md)| Defines product attributes | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_currency_add**
> InlineResponse20084 product_currency_add(iso3, rate, name=name, avail=avail, symbol_left=symbol_left, symbol_right=symbol_right, default=default)



Add currency and/or set default in store

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
iso3 = 'iso3_example' # str | Specifies standardized currency code
rate = 8.14 # float | Defines the numerical identifier against to the major currency
name = 'name_example' # str | Defines currency's name (optional)
avail = true # bool | Specifies whether the currency is available (optional) (default to true)
symbol_left = 'symbol_left_example' # str | Defines the symbol that is located before the currency (optional)
symbol_right = 'symbol_right_example' # str | Defines the symbol that is located after the currency (optional)
default = false # bool | Specifies currency's default meaning (optional) (default to false)

try:
    api_response = api_instance.product_currency_add(iso3, rate, name=name, avail=avail, symbol_left=symbol_left, symbol_right=symbol_right, default=default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_currency_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso3** | **str**| Specifies standardized currency code | 
 **rate** | **float**| Defines the numerical identifier against to the major currency | 
 **name** | **str**| Defines currency&#39;s name | [optional] 
 **avail** | **bool**| Specifies whether the currency is available | [optional] [default to true]
 **symbol_left** | **str**| Defines the symbol that is located before the currency | [optional] 
 **symbol_right** | **str**| Defines the symbol that is located after the currency | [optional] 
 **default** | **bool**| Specifies currency&#39;s default meaning | [optional] [default to false]

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_currency_list**
> InlineResponse20085 product_currency_list(start=start, count=count, params=params, exclude=exclude, default=default, avail=avail)



Get list of currencies

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'name,iso3,default,avail' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to name,iso3,default,avail)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
default = true # bool | Specifies the set of default/not default currencies (optional)
avail = true # bool | Specifies the set of available/not available currencies (optional)

try:
    api_response = api_instance.product_currency_list(start=start, count=count, params=params, exclude=exclude, default=default, avail=avail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_currency_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to name,iso3,default,avail]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **default** | **bool**| Specifies the set of default/not default currencies | [optional] 
 **avail** | **bool**| Specifies the set of available/not available currencies | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_delete**
> InlineResponse20036 product_delete(id)



Product delete

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Product id that will be removed

try:
    api_response = api_instance.product_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product id that will be removed | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_fields**
> InlineResponse20014 product_fields()



Retrieve all available fields for product item in store.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.product_fields()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_fields: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_find**
> InlineResponse20034 product_find(find_value, find_where=find_where, find_params=find_params, find_what=find_what, lang_id=lang_id, store_id=store_id)



Search product in store catalog. \"Apple\" is specified here by default.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
find_value = 'find_value_example' # str | Entity search that is specified by some value
find_where = 'name' # str | Entity search that is specified by the comma-separated unique fields (optional) (default to name)
find_params = 'whole_words' # str | Entity search that is specified by comma-separated parameters (optional) (default to whole_words)
find_what = 'product' # str | Parameter's value specifies the entity that has to be found (optional) (default to product)
lang_id = 'lang_id_example' # str | Search products specified by language id (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_find(find_value, find_where=find_where, find_params=find_params, find_what=find_what, lang_id=lang_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_value** | **str**| Entity search that is specified by some value | 
 **find_where** | **str**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name]
 **find_params** | **str**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words]
 **find_what** | **str**| Parameter&#39;s value specifies the entity that has to be found | [optional] [default to product]
 **lang_id** | **str**| Search products specified by language id | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_image_add**
> InlineResponse20037 product_image_add(product_id, image_name, type, url=url, label=label, mime=mime, position=position, content=content, product_variant_id=product_variant_id, variant_ids=variant_ids, store_id=store_id, lang_id=lang_id)



Add image to product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the image should be added
image_name = 'image_name_example' # str | Defines image's name
type = 'type_example' # str | Defines image's types that are specified by comma-separated list
url = 'url_example' # str | Defines URL of the image that has to be added (optional)
label = 'label_example' # str | Defines alternative text that has to be attached to the picture (optional)
mime = 'mime_example' # str | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. (optional)
position = 0 # int | Defines image’s position in the list (optional) (default to 0)
content = 'content_example' # str | Content(body) encoded in base64 of image file (optional)
product_variant_id = 56 # int | Defines product's variants specified by variant id (optional)
variant_ids = 'variant_ids_example' # str | Defines product's variants ids (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Add product image on specified language id (optional)

try:
    api_response = api_instance.product_image_add(product_id, image_name, type, url=url, label=label, mime=mime, position=position, content=content, product_variant_id=product_variant_id, variant_ids=variant_ids, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_image_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the image should be added | 
 **image_name** | **str**| Defines image&#39;s name | 
 **type** | **str**| Defines image&#39;s types that are specified by comma-separated list | 
 **url** | **str**| Defines URL of the image that has to be added | [optional] 
 **label** | **str**| Defines alternative text that has to be attached to the picture | [optional] 
 **mime** | **str**| Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. | [optional] 
 **position** | **int**| Defines image’s position in the list | [optional] [default to 0]
 **content** | **str**| Content(body) encoded in base64 of image file | [optional] 
 **product_variant_id** | **int**| Defines product&#39;s variants specified by variant id | [optional] 
 **variant_ids** | **str**| Defines product&#39;s variants ids | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Add product image on specified language id | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_image_delete**
> InlineResponse2004 product_image_delete(product_id, id, store_id=store_id)



Delete image

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the image should be deleted
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_image_delete(product_id, id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_image_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the image should be deleted | 
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

# **product_image_update**
> InlineResponse2005 product_image_update(product_id, id, image_name=image_name, type=type, label=label, position=position, store_id=store_id, lang_id=lang_id, hidden=hidden)



Update details of image

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the image should be updated
id = 'id_example' # str | Defines image update specified by image id
image_name = 'image_name_example' # str | Defines image's name (optional)
type = 'additional' # str | Defines image's types that are specified by comma-separated list (optional) (default to additional)
label = 'label_example' # str | Defines alternative text that has to be attached to the picture (optional)
position = 56 # int | Defines image’s position in the list (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
hidden = true # bool | Define is hide image (optional)

try:
    api_response = api_instance.product_image_update(product_id, id, image_name=image_name, type=type, label=label, position=position, store_id=store_id, lang_id=lang_id, hidden=hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_image_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the image should be updated | 
 **id** | **str**| Defines image update specified by image id | 
 **image_name** | **str**| Defines image&#39;s name | [optional] 
 **type** | **str**| Defines image&#39;s types that are specified by comma-separated list | [optional] [default to additional]
 **label** | **str**| Defines alternative text that has to be attached to the picture | [optional] 
 **position** | **int**| Defines image’s position in the list | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **hidden** | **bool**| Define is hide image | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_info**
> InlineResponse20033 product_info(id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id, currency_id=currency_id, product_variant_params=product_variant_params, report_request_id=report_request_id, disable_report_cache=disable_report_cache)



Get product info about product ID *** or specify other product ID.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Retrieves product's info specified by product id
params = 'id,name,description,price,categories_ids' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description,price,categories_ids)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Retrieves product info specified by store id (optional)
lang_id = 'lang_id_example' # str | Retrieves product info specified by language id (optional)
currency_id = 'currency_id_example' # str | Currency Id (optional)
product_variant_params = 'force_all' # str | Set this parameter in order to choose which product variants fields you want to retrieve (optional) (default to force_all)
report_request_id = 'report_request_id_example' # str | Report request id (optional)
disable_report_cache = false # bool | Disable report cache for current request (optional) (default to false)

try:
    api_response = api_instance.product_info(id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id, currency_id=currency_id, product_variant_params=product_variant_params, report_request_id=report_request_id, disable_report_cache=disable_report_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Retrieves product&#39;s info specified by product id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price,categories_ids]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Retrieves product info specified by store id | [optional] 
 **lang_id** | **str**| Retrieves product info specified by language id | [optional] 
 **currency_id** | **str**| Currency Id | [optional] 
 **product_variant_params** | **str**| Set this parameter in order to choose which product variants fields you want to retrieve | [optional] [default to force_all]
 **report_request_id** | **str**| Report request id | [optional] 
 **disable_report_cache** | **bool**| Disable report cache for current request | [optional] [default to false]

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list**
> ModelResponseProductList product_list(page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, category_id=category_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, avail_view=avail_view, avail_sale=avail_sale, store_id=store_id, lang_id=lang_id, currency_id=currency_id, product_ids=product_ids, product_variant_params=product_variant_params, since_id=since_id, report_request_id=report_request_id, disable_report_cache=disable_report_cache, sort_by=sort_by, sort_direction=sort_direction, sku=sku, disable_cache=disable_cache, brand_name=brand_name, product_attributes=product_attributes)



Get list of products from your store. Returns 10 products by default.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
page_cursor = 'page_cursor_example' # str | Used to retrieve products via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,name,description,price,categories_ids' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description,price,categories_ids)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
category_id = 'category_id_example' # str | Retrieves products specified by category id (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
avail_view = true # bool | Specifies the set of visible/invisible products (optional)
avail_sale = true # bool | Specifies the set of available/not available products for sale (optional)
store_id = 'store_id_example' # str | Retrieves products specified by store id (optional)
lang_id = 'lang_id_example' # str | Retrieves products specified by language id (optional)
currency_id = 'currency_id_example' # str | Currency Id (optional)
product_ids = 'product_ids_example' # str | Retrieves products specified by product ids (optional)
product_variant_params = 'force_all' # str | Set this parameter in order to choose which product variants fields you want to retrieve (optional) (default to force_all)
since_id = 56 # int | Retrieve entities starting from the specified id. (optional)
report_request_id = 'report_request_id_example' # str | Report request id (optional)
disable_report_cache = false # bool | Disable report cache for current request (optional) (default to false)
sort_by = 'id' # str | Set field to sort by (optional) (default to id)
sort_direction = 'asc' # str | Set sorting direction (optional) (default to asc)
sku = 'sku_example' # str | Filter by product's sku (optional)
disable_cache = false # bool | Disable cache for current request (optional) (default to false)
brand_name = 'brand_name_example' # str | Retrieves brands specified by brand name (optional)
product_attributes = ['product_attributes_example'] # list[str] | Defines product attributes (optional)

try:
    api_response = api_instance.product_list(page_cursor=page_cursor, start=start, count=count, params=params, exclude=exclude, category_id=category_id, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, avail_view=avail_view, avail_sale=avail_sale, store_id=store_id, lang_id=lang_id, currency_id=currency_id, product_ids=product_ids, product_variant_params=product_variant_params, since_id=since_id, report_request_id=report_request_id, disable_report_cache=disable_report_cache, sort_by=sort_by, sort_direction=sort_direction, sku=sku, disable_cache=disable_cache, brand_name=brand_name, product_attributes=product_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Used to retrieve products via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price,categories_ids]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **category_id** | **str**| Retrieves products specified by category id | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **avail_view** | **bool**| Specifies the set of visible/invisible products | [optional] 
 **avail_sale** | **bool**| Specifies the set of available/not available products for sale | [optional] 
 **store_id** | **str**| Retrieves products specified by store id | [optional] 
 **lang_id** | **str**| Retrieves products specified by language id | [optional] 
 **currency_id** | **str**| Currency Id | [optional] 
 **product_ids** | **str**| Retrieves products specified by product ids | [optional] 
 **product_variant_params** | **str**| Set this parameter in order to choose which product variants fields you want to retrieve | [optional] [default to force_all]
 **since_id** | **int**| Retrieve entities starting from the specified id. | [optional] 
 **report_request_id** | **str**| Report request id | [optional] 
 **disable_report_cache** | **bool**| Disable report cache for current request | [optional] [default to false]
 **sort_by** | **str**| Set field to sort by | [optional] [default to id]
 **sort_direction** | **str**| Set sorting direction | [optional] [default to asc]
 **sku** | **str**| Filter by product&#39;s sku | [optional] 
 **disable_cache** | **bool**| Disable cache for current request | [optional] [default to false]
 **brand_name** | **str**| Retrieves brands specified by brand name | [optional] 
 **product_attributes** | [**list[str]**](str.md)| Defines product attributes | [optional] 

### Return type

[**ModelResponseProductList**](ModelResponseProductList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_manufacturer_add**
> InlineResponse20082 product_manufacturer_add(product_id, manufacturer)



Add manufacturer to store and assign to product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines products specified by product id
manufacturer = 'manufacturer_example' # str | Defines product’s manufacturer's name

try:
    api_response = api_instance.product_manufacturer_add(product_id, manufacturer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_manufacturer_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines products specified by product id | 
 **manufacturer** | **str**| Defines product’s manufacturer&#39;s name | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_add**
> InlineResponse20070 product_option_add(name, type, product_id=product_id, default_option_value=default_option_value, option_values=option_values, description=description, avail=avail, sort_order=sort_order, required=required, clear_cache=clear_cache)



Add product option from store.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Defines option's name
type = 'type_example' # str | Defines option's type that has to be added
product_id = 'product_id_example' # str | Defines product id where the option should be added (optional)
default_option_value = 'default_option_value_example' # str | Defines default option value that has to be added (optional)
option_values = 'option_values_example' # str | Defines option values that has to be added (optional)
description = 'description_example' # str | Defines option's description (optional)
avail = true # bool | Defines whether the option is available (optional) (default to true)
sort_order = 0 # int | Sort number in the list (optional) (default to 0)
required = false # bool | Defines if the option is required (optional) (default to false)
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_option_add(name, type, product_id=product_id, default_option_value=default_option_value, option_values=option_values, description=description, avail=avail, sort_order=sort_order, required=required, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Defines option&#39;s name | 
 **type** | **str**| Defines option&#39;s type that has to be added | 
 **product_id** | **str**| Defines product id where the option should be added | [optional] 
 **default_option_value** | **str**| Defines default option value that has to be added | [optional] 
 **option_values** | **str**| Defines option values that has to be added | [optional] 
 **description** | **str**| Defines option&#39;s description | [optional] 
 **avail** | **bool**| Defines whether the option is available | [optional] [default to true]
 **sort_order** | **int**| Sort number in the list | [optional] [default to 0]
 **required** | **bool**| Defines if the option is required | [optional] [default to false]
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_assign**
> InlineResponse20072 product_option_assign(product_id, option_id, required=required, sort_order=sort_order, option_values=option_values, clear_cache=clear_cache)



Assign option from product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the option should be assigned
option_id = 56 # int | Defines option id which has to be assigned
required = false # bool | Defines if the option is required (optional) (default to false)
sort_order = 0 # int | Sort number in the list (optional) (default to 0)
option_values = 'option_values_example' # str | Defines option values that has to be assigned (optional)
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_option_assign(product_id, option_id, required=required, sort_order=sort_order, option_values=option_values, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the option should be assigned | 
 **option_id** | **int**| Defines option id which has to be assigned | 
 **required** | **bool**| Defines if the option is required | [optional] [default to false]
 **sort_order** | **int**| Sort number in the list | [optional] [default to 0]
 **option_values** | **str**| Defines option values that has to be assigned | [optional] 
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_list**
> InlineResponse20071 product_option_list(start=start, count=count, params=params, exclude=exclude, product_id=product_id, lang_id=lang_id, store_id=store_id)



Get list of options.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,name,description' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
product_id = 'product_id_example' # str | Retrieves products' options specified by product id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_option_list(start=start, count=count, params=params, exclude=exclude, product_id=product_id, lang_id=lang_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **product_id** | **str**| Retrieves products&#39; options specified by product id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_value_add**
> InlineResponse20073 product_option_value_add(product_id, option_id, option_value, sort_order=sort_order, clear_cache=clear_cache)



Add product option item from option.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the option value should be added
option_id = 56 # int | Defines option id where the value has to be added
option_value = 'option_value_example' # str | Defines option value that has to be added
sort_order = 0 # int | Sort number in the list (optional) (default to 0)
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_option_value_add(product_id, option_id, option_value, sort_order=sort_order, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_value_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the option value should be added | 
 **option_id** | **int**| Defines option id where the value has to be added | 
 **option_value** | **str**| Defines option value that has to be added | 
 **sort_order** | **int**| Sort number in the list | [optional] [default to 0]
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_value_assign**
> InlineResponse20074 product_option_value_assign(product_option_id, option_value_id, clear_cache=clear_cache)



Assign product option item from product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_option_id = 56 # int | Defines product's option id where the value has to be assigned
option_value_id = 56 # int | Defines value id that has to be assigned
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_option_value_assign(product_option_id, option_value_id, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_value_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_option_id** | **int**| Defines product&#39;s option id where the value has to be assigned | 
 **option_value_id** | **int**| Defines value id that has to be assigned | 
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_option_value_update**
> InlineResponse20028 product_option_value_update(product_id, option_id, option_value_id, option_value, price=price, quantity=quantity, clear_cache=clear_cache)



Update product option item from option.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the option value should be updated
option_id = 56 # int | Defines option id where the value has to be updated
option_value_id = 56 # int | Defines value id that has to be assigned
option_value = 'option_value_example' # str | Defines option value that has to be added
price = 8.14 # float | Defines new product option price (optional)
quantity = 8.14 # float | Defines new products' options quantity (optional)
clear_cache = true # bool | Is cache clear required (optional) (default to true)

try:
    api_response = api_instance.product_option_value_update(product_id, option_id, option_value_id, option_value, price=price, quantity=quantity, clear_cache=clear_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_option_value_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the option value should be updated | 
 **option_id** | **int**| Defines option id where the value has to be updated | 
 **option_value_id** | **int**| Defines value id that has to be assigned | 
 **option_value** | **str**| Defines option value that has to be added | 
 **price** | **float**| Defines new product option price | [optional] 
 **quantity** | **float**| Defines new products&#39; options quantity | [optional] 
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_price_add**
> InlineResponse2007 product_price_add(body)



Add some prices to the product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductPriceAdd() # ProductPriceAdd | 

try:
    api_response = api_instance.product_price_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_price_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductPriceAdd**](ProductPriceAdd.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_price_delete**
> InlineResponse2004 product_price_delete(product_id, group_prices=group_prices)



Delete some prices of the product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines the product where the price has to be deleted
group_prices = 'group_prices_example' # str | Defines product's group prices (optional)

try:
    api_response = api_instance.product_price_delete(product_id, group_prices=group_prices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_price_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines the product where the price has to be deleted | 
 **group_prices** | **str**| Defines product&#39;s group prices | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_price_update**
> InlineResponse20028 product_price_update(body)



Update some prices of the product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductPriceUpdate() # ProductPriceUpdate | 

try:
    api_response = api_instance.product_price_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_price_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductPriceUpdate**](ProductPriceUpdate.md)|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_review_list**
> InlineResponse20075 product_review_list(product_id, start=start, count=count, ids=ids, store_id=store_id, status=status, params=params, exclude=exclude)



Get reviews of a specific product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Product id
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
ids = 'ids_example' # str | Retrieves reviews specified by ids (optional)
store_id = 'store_id_example' # str | Store Id (optional)
status = 'status_example' # str | Defines status (optional)
params = 'id,customer_id,email,message,status' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,customer_id,email,message,status)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.product_review_list(product_id, start=start, count=count, ids=ids, store_id=store_id, status=status, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_review_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product id | 
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **ids** | **str**| Retrieves reviews specified by ids | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **status** | **str**| Defines status | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,customer_id,email,message,status]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_store_assign**
> InlineResponse20028 product_store_assign(product_id, store_id)



Assign product to store

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines id of the product which should be assigned to a store
store_id = 'store_id_example' # str | Defines id of the store product should be assigned to

try:
    api_response = api_instance.product_store_assign(product_id, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_store_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines id of the product which should be assigned to a store | 
 **store_id** | **str**| Defines id of the store product should be assigned to | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_tax_add**
> InlineResponse20081 product_tax_add(body)



Add tax class and tax rate to store and assign to product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductTaxAdd() # ProductTaxAdd | 

try:
    api_response = api_instance.product_tax_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_tax_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductTaxAdd**](ProductTaxAdd.md)|  | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_update**
> InlineResponse20028 product_update(id, model=model, old_price=old_price, price=price, special_price=special_price, sprice_create=sprice_create, sprice_expire=sprice_expire, cost_price=cost_price, retail_price=retail_price, quantity=quantity, weight=weight, increase_quantity=increase_quantity, reduce_quantity=reduce_quantity, warehouse_id=warehouse_id, reserve_quantity=reserve_quantity, manage_stock=manage_stock, backorder_status=backorder_status, name=name, sku=sku, visible=visible, manufacturer=manufacturer, manufacturer_id=manufacturer_id, categories_ids=categories_ids, description=description, short_description=short_description, meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description, store_id=store_id, lang_id=lang_id, in_stock=in_stock, status=status, seo_url=seo_url, report_request_id=report_request_id, disable_report_cache=disable_report_cache, reindex=reindex, tags=tags, clear_cache=clear_cache, gtin=gtin, taxable=taxable, product_class=product_class)



Update price and quantity for a specific product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines product id that has to be updated
model = 'model_example' # str | Defines product model that has to be updated (optional)
old_price = 8.14 # float | Defines product's old price (optional)
price = 8.14 # float | Defines new product's price (optional)
special_price = 8.14 # float | Defines new product's special price (optional)
sprice_create = 'sprice_create_example' # str | Defines the date of special price creation (optional)
sprice_expire = 'sprice_expire_example' # str | Defines the term of special price offer duration (optional)
cost_price = 8.14 # float | Defines new product's cost price (optional)
retail_price = 8.14 # float | Defines new product's retail price (optional)
quantity = 8.14 # float | Defines new product's quantity (optional)
weight = 8.14 # float | Weight (optional)
increase_quantity = 8.14 # float | Defines the incremental changes in product quantity (optional)
reduce_quantity = 8.14 # float | Defines the decrement changes in product quantity (optional)
warehouse_id = 'warehouse_id_example' # str | This parameter is used for selecting a warehouse where you need to set/modify a product quantity. (optional)
reserve_quantity = 8.14 # float | This parameter allows to reserve/unreserve product quantity. (optional)
manage_stock = true # bool | Defines inventory tracking for product (optional)
backorder_status = 'backorder_status_example' # str | Set backorder status (optional)
name = 'name_example' # str | Defines product's name that has to be updated (optional)
sku = 'sku_example' # str | Defines new product's sku (optional)
visible = 'visible_example' # str | Set visibility status (optional)
manufacturer = 'manufacturer_example' # str | Defines product's manufacturer (optional)
manufacturer_id = 'manufacturer_id_example' # str | Defines product's manufacturer by manufacturer_id (optional)
categories_ids = 'categories_ids_example' # str | Defines product add that is specified by comma-separated categories id (optional)
description = 'description_example' # str | Defines new product's description (optional)
short_description = 'short_description_example' # str | Defines short description (optional)
meta_title = 'meta_title_example' # str | Defines unique meta title for each entity (optional)
meta_keywords = 'meta_keywords_example' # str | Defines unique meta keywords for each entity (optional)
meta_description = 'meta_description_example' # str | Defines unique meta description of a entity (optional)
store_id = 'store_id_example' # str | Defines store id where the product should be found (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
in_stock = true # bool | Set stock status (optional)
status = 'status_example' # str | Defines product's status (optional)
seo_url = 'seo_url_example' # str | Defines unique URL for SEO (optional)
report_request_id = 'report_request_id_example' # str | Report request id (optional)
disable_report_cache = false # bool | Disable report cache for current request (optional) (default to false)
reindex = true # bool | Is reindex required (optional) (default to true)
tags = 'tags_example' # str | Product tags (optional)
clear_cache = true # bool | Is cache clear required (optional) (default to true)
gtin = 'gtin_example' # str | Global Trade Item Number. An GTIN is an identifier for trade items. (optional)
taxable = true # bool | Specifies whether a tax is charged (optional) (default to true)
product_class = 'product_class_example' # str | A categorization for the product (optional)

try:
    api_response = api_instance.product_update(id, model=model, old_price=old_price, price=price, special_price=special_price, sprice_create=sprice_create, sprice_expire=sprice_expire, cost_price=cost_price, retail_price=retail_price, quantity=quantity, weight=weight, increase_quantity=increase_quantity, reduce_quantity=reduce_quantity, warehouse_id=warehouse_id, reserve_quantity=reserve_quantity, manage_stock=manage_stock, backorder_status=backorder_status, name=name, sku=sku, visible=visible, manufacturer=manufacturer, manufacturer_id=manufacturer_id, categories_ids=categories_ids, description=description, short_description=short_description, meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description, store_id=store_id, lang_id=lang_id, in_stock=in_stock, status=status, seo_url=seo_url, report_request_id=report_request_id, disable_report_cache=disable_report_cache, reindex=reindex, tags=tags, clear_cache=clear_cache, gtin=gtin, taxable=taxable, product_class=product_class)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines product id that has to be updated | 
 **model** | **str**| Defines product model that has to be updated | [optional] 
 **old_price** | **float**| Defines product&#39;s old price | [optional] 
 **price** | **float**| Defines new product&#39;s price | [optional] 
 **special_price** | **float**| Defines new product&#39;s special price | [optional] 
 **sprice_create** | **str**| Defines the date of special price creation | [optional] 
 **sprice_expire** | **str**| Defines the term of special price offer duration | [optional] 
 **cost_price** | **float**| Defines new product&#39;s cost price | [optional] 
 **retail_price** | **float**| Defines new product&#39;s retail price | [optional] 
 **quantity** | **float**| Defines new product&#39;s quantity | [optional] 
 **weight** | **float**| Weight | [optional] 
 **increase_quantity** | **float**| Defines the incremental changes in product quantity | [optional] 
 **reduce_quantity** | **float**| Defines the decrement changes in product quantity | [optional] 
 **warehouse_id** | **str**| This parameter is used for selecting a warehouse where you need to set/modify a product quantity. | [optional] 
 **reserve_quantity** | **float**| This parameter allows to reserve/unreserve product quantity. | [optional] 
 **manage_stock** | **bool**| Defines inventory tracking for product | [optional] 
 **backorder_status** | **str**| Set backorder status | [optional] 
 **name** | **str**| Defines product&#39;s name that has to be updated | [optional] 
 **sku** | **str**| Defines new product&#39;s sku | [optional] 
 **visible** | **str**| Set visibility status | [optional] 
 **manufacturer** | **str**| Defines product&#39;s manufacturer | [optional] 
 **manufacturer_id** | **str**| Defines product&#39;s manufacturer by manufacturer_id | [optional] 
 **categories_ids** | **str**| Defines product add that is specified by comma-separated categories id | [optional] 
 **description** | **str**| Defines new product&#39;s description | [optional] 
 **short_description** | **str**| Defines short description | [optional] 
 **meta_title** | **str**| Defines unique meta title for each entity | [optional] 
 **meta_keywords** | **str**| Defines unique meta keywords for each entity | [optional] 
 **meta_description** | **str**| Defines unique meta description of a entity | [optional] 
 **store_id** | **str**| Defines store id where the product should be found | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **in_stock** | **bool**| Set stock status | [optional] 
 **status** | **str**| Defines product&#39;s status | [optional] 
 **seo_url** | **str**| Defines unique URL for SEO | [optional] 
 **report_request_id** | **str**| Report request id | [optional] 
 **disable_report_cache** | **bool**| Disable report cache for current request | [optional] [default to false]
 **reindex** | **bool**| Is reindex required | [optional] [default to true]
 **tags** | **str**| Product tags | [optional] 
 **clear_cache** | **bool**| Is cache clear required | [optional] [default to true]
 **gtin** | **str**| Global Trade Item Number. An GTIN is an identifier for trade items. | [optional] 
 **taxable** | **bool**| Specifies whether a tax is charged | [optional] [default to true]
 **product_class** | **str**| A categorization for the product | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_add**
> InlineResponse20076 product_variant_add(body)



Add variant to product.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductVariantAdd() # ProductVariantAdd | 

try:
    api_response = api_instance.product_variant_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductVariantAdd**](ProductVariantAdd.md)|  | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_count**
> InlineResponse20080 product_variant_count(created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, category_id=category_id, product_id=product_id, store_id=store_id)



Get count variants.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
category_id = 'category_id_example' # str | Counts products’ variants specified by category id (optional)
product_id = 'product_id_example' # str | Retrieves products' variants specified by product id (optional)
store_id = 'store_id_example' # str | Retrieves variants specified by store id (optional)

try:
    api_response = api_instance.product_variant_count(created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, category_id=category_id, product_id=product_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **category_id** | **str**| Counts products’ variants specified by category id | [optional] 
 **product_id** | **str**| Retrieves products&#39; variants specified by product id | [optional] 
 **store_id** | **str**| Retrieves variants specified by store id | [optional] 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_delete**
> InlineResponse2004 product_variant_delete(id, product_id)



Delete variant.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines variant removal, specified by variant id
product_id = 'product_id_example' # str | Defines product's id where the variant has to be deleted

try:
    api_response = api_instance.product_variant_delete(id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines variant removal, specified by variant id | 
 **product_id** | **str**| Defines product&#39;s id where the variant has to be deleted | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_image_add**
> InlineResponse20037 product_variant_image_add(product_id, product_variant_id, image_name, type, url=url, content=content, label=label, mime=mime, position=position, store_id=store_id)



Add image to product

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines product id where the variant image has to be added
product_variant_id = 56 # int | Defines product's variants specified by variant id
image_name = 'image_name_example' # str | Defines image's name
type = 'base' # str | Defines image's types that are specified by comma-separated list (default to base)
url = 'url_example' # str | Defines URL of the image that has to be added (optional)
content = 'content_example' # str | Content(body) encoded in base64 of image file (optional)
label = 'label_example' # str | Defines alternative text that has to be attached to the picture (optional)
mime = 'mime_example' # str | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. (optional)
position = 0 # int | Defines image’s position in the list (optional) (default to 0)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.product_variant_image_add(product_id, product_variant_id, image_name, type, url=url, content=content, label=label, mime=mime, position=position, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_image_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines product id where the variant image has to be added | 
 **product_variant_id** | **int**| Defines product&#39;s variants specified by variant id | 
 **image_name** | **str**| Defines image&#39;s name | 
 **type** | **str**| Defines image&#39;s types that are specified by comma-separated list | [default to base]
 **url** | **str**| Defines URL of the image that has to be added | [optional] 
 **content** | **str**| Content(body) encoded in base64 of image file | [optional] 
 **label** | **str**| Defines alternative text that has to be attached to the picture | [optional] 
 **mime** | **str**| Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. | [optional] 
 **position** | **int**| Defines image’s position in the list | [optional] [default to 0]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_info**
> InlineResponse20033 product_variant_info(id, params=params, exclude=exclude, store_id=store_id)



Get variant info.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Retrieves variant's info specified by variant id
params = 'id,name,description,price' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description,price)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Retrieves variant info specified by store id (optional)

try:
    api_response = api_instance.product_variant_info(id, params=params, exclude=exclude, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Retrieves variant&#39;s info specified by variant id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Retrieves variant info specified by store id | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_list**
> InlineResponse20079 product_variant_list(start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, category_id=category_id, product_id=product_id, store_id=store_id)



Get list variants.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,name,description,price' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,description,price)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
created_from = 'created_from_example' # str | Retrieve entities from their creation date (optional)
created_to = 'created_to_example' # str | Retrieve entities to their creation date (optional)
modified_from = 'modified_from_example' # str | Retrieve entities from their modification date (optional)
modified_to = 'modified_to_example' # str | Retrieve entities to their modification date (optional)
category_id = 'category_id_example' # str | Retrieves products’ variants specified by category id (optional)
product_id = 'product_id_example' # str | Retrieves products' variants specified by product id (optional)
store_id = 'store_id_example' # str | Retrieves variants specified by store id (optional)

try:
    api_response = api_instance.product_variant_list(start=start, count=count, params=params, exclude=exclude, created_from=created_from, created_to=created_to, modified_from=modified_from, modified_to=modified_to, category_id=category_id, product_id=product_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **created_from** | **str**| Retrieve entities from their creation date | [optional] 
 **created_to** | **str**| Retrieve entities to their creation date | [optional] 
 **modified_from** | **str**| Retrieve entities from their modification date | [optional] 
 **modified_to** | **str**| Retrieve entities to their modification date | [optional] 
 **category_id** | **str**| Retrieves products’ variants specified by category id | [optional] 
 **product_id** | **str**| Retrieves products&#39; variants specified by product id | [optional] 
 **store_id** | **str**| Retrieves variants specified by store id | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_price_add**
> InlineResponse2007 product_variant_price_add(body)



Add some prices to the product variant.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductVariantPriceAdd() # ProductVariantPriceAdd | 

try:
    api_response = api_instance.product_variant_price_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_price_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductVariantPriceAdd**](ProductVariantPriceAdd.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_price_delete**
> InlineResponse2004 product_variant_price_delete(id, group_prices=group_prices)



Delete some prices of the product variant.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines the variant where the price has to be deleted
group_prices = 'group_prices_example' # str | Defines variants's group prices (optional)

try:
    api_response = api_instance.product_variant_price_delete(id, group_prices=group_prices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_price_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines the variant where the price has to be deleted | 
 **group_prices** | **str**| Defines variants&#39;s group prices | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_price_update**
> InlineResponse20028 product_variant_price_update(body)



Update some prices of the product variant.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductVariantPriceUpdate() # ProductVariantPriceUpdate | 

try:
    api_response = api_instance.product_variant_price_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_price_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductVariantPriceUpdate**](ProductVariantPriceUpdate.md)|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_variant_update**
> InlineResponse20028 product_variant_update(id, product_id, store_id=store_id, warehouse_id=warehouse_id, reserve_quantity=reserve_quantity, quantity=quantity, increase_quantity=increase_quantity, reduce_quantity=reduce_quantity, price=price, special_price=special_price, old_price=old_price, cost_price=cost_price, sprice_create=sprice_create, sprice_expire=sprice_expire, manage_stock=manage_stock, in_stock=in_stock, name=name, description=description, sku=sku, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, short_description=short_description, visible=visible, status=status, backorder_status=backorder_status, weight=weight, barcode=barcode, reindex=reindex, taxable=taxable, options=options)



Update variant.

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines variant update specified by variant id
product_id = 'product_id_example' # str | Defines product's id where the variant has to be updated
store_id = 'store_id_example' # str | Defines store id where the variant should be found (optional)
warehouse_id = 'warehouse_id_example' # str | This parameter is used for selecting a warehouse where you need to set/modify a product quantity. (optional)
reserve_quantity = 8.14 # float | This parameter allows to reserve/unreserve product variants quantity. (optional)
quantity = 8.14 # float | Defines new products' variants quantity (optional)
increase_quantity = 0 # float | Defines the incremental changes in product quantity (optional) (default to 0)
reduce_quantity = 0 # float | Defines the decrement changes in product quantity (optional) (default to 0)
price = 8.14 # float | Defines new product's variant price (optional)
special_price = 8.14 # float | Defines new product's variant special price (optional)
old_price = 8.14 # float | Defines product's old price (optional)
cost_price = 8.14 # float | Defines new product's cost price (optional)
sprice_create = 'sprice_create_example' # str | Defines the date of special price creation (optional)
sprice_expire = 'sprice_expire_example' # str | Defines the term of special price offer duration (optional)
manage_stock = true # bool | Defines inventory tracking for product variant (optional)
in_stock = true # bool | Set stock status (optional)
name = 'name_example' # str | Defines variant's name that has to be updated (optional)
description = 'description_example' # str | Specifies variant's description (optional)
sku = 'sku_example' # str | Defines new product's variant sku (optional)
meta_title = 'meta_title_example' # str | Defines unique meta title for each entity (optional)
meta_description = 'meta_description_example' # str | Defines unique meta description of a entity (optional)
meta_keywords = 'meta_keywords_example' # str | Defines unique meta keywords for each entity (optional)
short_description = 'short_description_example' # str | Defines short description (optional)
visible = 'visible_example' # str | Set visibility status (optional)
status = 'status_example' # str | Defines product variant's status (optional)
backorder_status = 'backorder_status_example' # str | Set backorder status (optional)
weight = 0 # float | Weight (optional) (default to 0)
barcode = 'barcode_example' # str | A barcode is a unique code composed of numbers used as a product identifier. (optional)
reindex = true # bool | Is reindex required (optional) (default to true)
taxable = true # bool | Specifies whether a tax is charged (optional) (default to true)
options = ['options_example'] # list[str] | Defines variant's options list (optional)

try:
    api_response = api_instance.product_variant_update(id, product_id, store_id=store_id, warehouse_id=warehouse_id, reserve_quantity=reserve_quantity, quantity=quantity, increase_quantity=increase_quantity, reduce_quantity=reduce_quantity, price=price, special_price=special_price, old_price=old_price, cost_price=cost_price, sprice_create=sprice_create, sprice_expire=sprice_expire, manage_stock=manage_stock, in_stock=in_stock, name=name, description=description, sku=sku, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, short_description=short_description, visible=visible, status=status, backorder_status=backorder_status, weight=weight, barcode=barcode, reindex=reindex, taxable=taxable, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_variant_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines variant update specified by variant id | 
 **product_id** | **str**| Defines product&#39;s id where the variant has to be updated | 
 **store_id** | **str**| Defines store id where the variant should be found | [optional] 
 **warehouse_id** | **str**| This parameter is used for selecting a warehouse where you need to set/modify a product quantity. | [optional] 
 **reserve_quantity** | **float**| This parameter allows to reserve/unreserve product variants quantity. | [optional] 
 **quantity** | **float**| Defines new products&#39; variants quantity | [optional] 
 **increase_quantity** | **float**| Defines the incremental changes in product quantity | [optional] [default to 0]
 **reduce_quantity** | **float**| Defines the decrement changes in product quantity | [optional] [default to 0]
 **price** | **float**| Defines new product&#39;s variant price | [optional] 
 **special_price** | **float**| Defines new product&#39;s variant special price | [optional] 
 **old_price** | **float**| Defines product&#39;s old price | [optional] 
 **cost_price** | **float**| Defines new product&#39;s cost price | [optional] 
 **sprice_create** | **str**| Defines the date of special price creation | [optional] 
 **sprice_expire** | **str**| Defines the term of special price offer duration | [optional] 
 **manage_stock** | **bool**| Defines inventory tracking for product variant | [optional] 
 **in_stock** | **bool**| Set stock status | [optional] 
 **name** | **str**| Defines variant&#39;s name that has to be updated | [optional] 
 **description** | **str**| Specifies variant&#39;s description | [optional] 
 **sku** | **str**| Defines new product&#39;s variant sku | [optional] 
 **meta_title** | **str**| Defines unique meta title for each entity | [optional] 
 **meta_description** | **str**| Defines unique meta description of a entity | [optional] 
 **meta_keywords** | **str**| Defines unique meta keywords for each entity | [optional] 
 **short_description** | **str**| Defines short description | [optional] 
 **visible** | **str**| Set visibility status | [optional] 
 **status** | **str**| Defines product variant&#39;s status | [optional] 
 **backorder_status** | **str**| Set backorder status | [optional] 
 **weight** | **float**| Weight | [optional] [default to 0]
 **barcode** | **str**| A barcode is a unique code composed of numbers used as a product identifier. | [optional] 
 **reindex** | **bool**| Is reindex required | [optional] [default to true]
 **taxable** | **bool**| Specifies whether a tax is charged | [optional] [default to true]
 **options** | [**list[str]**](str.md)| Defines variant&#39;s options list | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

