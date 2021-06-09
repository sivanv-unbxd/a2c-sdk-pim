# swagger_client.AttributeApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_add**](AttributeApi.md#attribute_add) | **POST** /attribute.add.json | 
[**attribute_assign_group**](AttributeApi.md#attribute_assign_group) | **POST** /attribute.assign.group.json | 
[**attribute_assign_set**](AttributeApi.md#attribute_assign_set) | **POST** /attribute.assign.set.json | 
[**attribute_attributeset_list**](AttributeApi.md#attribute_attributeset_list) | **GET** /attribute.attributeset.list.json | 
[**attribute_count**](AttributeApi.md#attribute_count) | **GET** /attribute.count.json | 
[**attribute_delete**](AttributeApi.md#attribute_delete) | **DELETE** /attribute.delete.json | 
[**attribute_group_list**](AttributeApi.md#attribute_group_list) | **GET** /attribute.group.list.json | 
[**attribute_info**](AttributeApi.md#attribute_info) | **GET** /attribute.info.json | 
[**attribute_list**](AttributeApi.md#attribute_list) | **GET** /attribute.list.json | 
[**attribute_type_list**](AttributeApi.md#attribute_type_list) | **GET** /attribute.type.list.json | 
[**attribute_unassign_group**](AttributeApi.md#attribute_unassign_group) | **POST** /attribute.unassign.group.json | 
[**attribute_unassign_set**](AttributeApi.md#attribute_unassign_set) | **POST** /attribute.unassign.set.json | 
[**attribute_update**](AttributeApi.md#attribute_update) | **POST** /attribute.update.json | 


# **attribute_add**
> InlineResponse200 attribute_add(type, name, code=code, store_id=store_id, lang_id=lang_id, visible=visible, required=required, position=position, attribute_group_id=attribute_group_id, is_global=is_global, is_searchable=is_searchable, is_filterable=is_filterable, is_comparable=is_comparable, is_html_allowed_on_front=is_html_allowed_on_front, is_filterable_in_search=is_filterable_in_search, is_configurable=is_configurable, is_visible_in_advanced_search=is_visible_in_advanced_search, is_used_for_promo_rules=is_used_for_promo_rules, used_in_product_listing=used_in_product_listing, used_for_sort_by=used_for_sort_by, apply_to=apply_to)



Add new attribute

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Defines attribute's type
name = 'name_example' # str | Defines attributes's name
code = 'code_example' # str | Entity code (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
visible = false # bool | Set visibility status (optional) (default to false)
required = false # bool | Defines if the option is required (optional) (default to false)
position = 0 # int | Attribute`s position (optional) (default to 0)
attribute_group_id = 'attribute_group_id_example' # str | Filter by attribute_group_id (optional)
is_global = 'Store' # str | Attribute saving scope (optional) (default to Store)
is_searchable = false # bool | Use attribute in Quick Search (optional) (default to false)
is_filterable = 'No' # str | Use In Layered Navigation (optional) (default to No)
is_comparable = false # bool | Comparable on Front-end (optional) (default to false)
is_html_allowed_on_front = false # bool | Allow HTML Tags on Frontend (optional) (default to false)
is_filterable_in_search = false # bool | Use In Search Results Layered Navigation (optional) (default to false)
is_configurable = false # bool | Use To Create Configurable Product (optional) (default to false)
is_visible_in_advanced_search = false # bool | Use in Advanced Search (optional) (default to false)
is_used_for_promo_rules = false # bool | Use for Promo Rule Conditions (optional) (default to false)
used_in_product_listing = false # bool | Used in Product Listing (optional) (default to false)
used_for_sort_by = false # bool | Used for Sorting in Product Listing (optional) (default to false)
apply_to = 'all_types' # str | Types of products which can have this attribute (optional) (default to all_types)

try:
    api_response = api_instance.attribute_add(type, name, code=code, store_id=store_id, lang_id=lang_id, visible=visible, required=required, position=position, attribute_group_id=attribute_group_id, is_global=is_global, is_searchable=is_searchable, is_filterable=is_filterable, is_comparable=is_comparable, is_html_allowed_on_front=is_html_allowed_on_front, is_filterable_in_search=is_filterable_in_search, is_configurable=is_configurable, is_visible_in_advanced_search=is_visible_in_advanced_search, is_used_for_promo_rules=is_used_for_promo_rules, used_in_product_listing=used_in_product_listing, used_for_sort_by=used_for_sort_by, apply_to=apply_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Defines attribute&#39;s type | 
 **name** | **str**| Defines attributes&#39;s name | 
 **code** | **str**| Entity code | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **visible** | **bool**| Set visibility status | [optional] [default to false]
 **required** | **bool**| Defines if the option is required | [optional] [default to false]
 **position** | **int**| Attribute&#x60;s position | [optional] [default to 0]
 **attribute_group_id** | **str**| Filter by attribute_group_id | [optional] 
 **is_global** | **str**| Attribute saving scope | [optional] [default to Store]
 **is_searchable** | **bool**| Use attribute in Quick Search | [optional] [default to false]
 **is_filterable** | **str**| Use In Layered Navigation | [optional] [default to No]
 **is_comparable** | **bool**| Comparable on Front-end | [optional] [default to false]
 **is_html_allowed_on_front** | **bool**| Allow HTML Tags on Frontend | [optional] [default to false]
 **is_filterable_in_search** | **bool**| Use In Search Results Layered Navigation | [optional] [default to false]
 **is_configurable** | **bool**| Use To Create Configurable Product | [optional] [default to false]
 **is_visible_in_advanced_search** | **bool**| Use in Advanced Search | [optional] [default to false]
 **is_used_for_promo_rules** | **bool**| Use for Promo Rule Conditions | [optional] [default to false]
 **used_in_product_listing** | **bool**| Used in Product Listing | [optional] [default to false]
 **used_for_sort_by** | **bool**| Used for Sorting in Product Listing | [optional] [default to false]
 **apply_to** | **str**| Types of products which can have this attribute | [optional] [default to all_types]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_assign_group**
> InlineResponse20065 attribute_assign_group(id, group_id, attribute_set_id=attribute_set_id)



Assign attribute to the group

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
group_id = 'group_id_example' # str | Attribute group_id
attribute_set_id = 'attribute_set_id_example' # str | Attribute set id (optional)

try:
    api_response = api_instance.attribute_assign_group(id, group_id, attribute_set_id=attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_assign_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **group_id** | **str**| Attribute group_id | 
 **attribute_set_id** | **str**| Attribute set id | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_assign_set**
> InlineResponse20065 attribute_assign_set(id, attribute_set_id, group_id=group_id)



Assign attribute to the attribute set

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
attribute_set_id = 'attribute_set_id_example' # str | Attribute set id
group_id = 'group_id_example' # str | Attribute group_id (optional)

try:
    api_response = api_instance.attribute_assign_set(id, attribute_set_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_assign_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **attribute_set_id** | **str**| Attribute set id | 
 **group_id** | **str**| Attribute group_id | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_attributeset_list**
> InlineResponse20067 attribute_attributeset_list(start=start, count=count, params=params, exclude=exclude)



Get attribute_set list

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
params = 'id,name' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.attribute_attributeset_list(start=start, count=count, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_attributeset_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_count**
> InlineResponse20063 attribute_count(type=type, store_id=store_id, lang_id=lang_id, visible=visible, required=required, system=system)



Get attributes count

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Defines attribute's type (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
visible = true # bool | Filter items by visibility status (optional)
required = true # bool | Defines if the option is required (optional)
system = true # bool | True if attribute is system (optional)

try:
    api_response = api_instance.attribute_count(type=type, store_id=store_id, lang_id=lang_id, visible=visible, required=required, system=system)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Defines attribute&#39;s type | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **visible** | **bool**| Filter items by visibility status | [optional] 
 **required** | **bool**| Defines if the option is required | [optional] 
 **system** | **bool**| True if attribute is system | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_delete**
> InlineResponse2004 attribute_delete(id, store_id=store_id)



Delete attribute from store

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.attribute_delete(id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_delete: %s\n" % e)
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

# **attribute_group_list**
> InlineResponse20067 attribute_group_list(start=start, count=count, lang_id=lang_id, params=params, exclude=exclude, attribute_set_id=attribute_set_id)



Get attribute group list

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
lang_id = 'lang_id_example' # str | Language id (optional)
params = 'id,name' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
attribute_set_id = 'attribute_set_id_example' # str | Attribute set id (optional)

try:
    api_response = api_instance.attribute_group_list(start=start, count=count, lang_id=lang_id, params=params, exclude=exclude, attribute_set_id=attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **lang_id** | **str**| Language id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **attribute_set_id** | **str**| Attribute set id | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_info**
> InlineResponse20062 attribute_info(id, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude)



Get attribute info

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
params = 'force_all' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to force_all)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)

try:
    api_response = api_instance.attribute_info(id, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_list**
> InlineResponse20061 attribute_list(start=start, count=count, type=type, attribute_ids=attribute_ids, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude, visible=visible, required=required, system=system)



Get attributes list

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
type = 'type_example' # str | Defines attribute's type (optional)
attribute_ids = 'attribute_ids_example' # str | Filter attributes by ids (optional)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Retrieves attributes on specified language id (optional)
params = 'id,name,code,type' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,name,code,type)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
visible = true # bool | Filter items by visibility status (optional)
required = true # bool | Defines if the option is required (optional)
system = true # bool | True if attribute is system (optional)

try:
    api_response = api_instance.attribute_list(start=start, count=count, type=type, attribute_ids=attribute_ids, store_id=store_id, lang_id=lang_id, params=params, exclude=exclude, visible=visible, required=required, system=system)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **type** | **str**| Defines attribute&#39;s type | [optional] 
 **attribute_ids** | **str**| Filter attributes by ids | [optional] 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Retrieves attributes on specified language id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,code,type]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **visible** | **bool**| Filter items by visibility status | [optional] 
 **required** | **bool**| Defines if the option is required | [optional] 
 **system** | **bool**| True if attribute is system | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_type_list**
> InlineResponse20064 attribute_type_list()



Get list of supported attributes types

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.attribute_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_unassign_group**
> InlineResponse20066 attribute_unassign_group(id, group_id)



Unassign attribute from group

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
group_id = 'group_id_example' # str | Customer group_id

try:
    api_response = api_instance.attribute_unassign_group(id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_unassign_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **group_id** | **str**| Customer group_id | 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_unassign_set**
> InlineResponse20066 attribute_unassign_set(id, attribute_set_id)



Unassign attribute from attribute set

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
attribute_set_id = 'attribute_set_id_example' # str | Attribute set id

try:
    api_response = api_instance.attribute_unassign_set(id, attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_unassign_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **attribute_set_id** | **str**| Attribute set id | 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_update**
> InlineResponse20031 attribute_update(id, name, store_id=store_id, lang_id=lang_id)



Update attribute data

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
api_instance = swagger_client.AttributeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Entity id
name = 'name_example' # str | Defines new attributes's name
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)

try:
    api_response = api_instance.attribute_update(id, name, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity id | 
 **name** | **str**| Defines new attributes&#39;s name | 
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

