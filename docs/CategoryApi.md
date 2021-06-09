# swagger_client.CategoryApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**category_add**](CategoryApi.md#category_add) | **POST** /category.add.json | 
[**category_assign**](CategoryApi.md#category_assign) | **POST** /category.assign.json | 
[**category_count**](CategoryApi.md#category_count) | **GET** /category.count.json | 
[**category_delete**](CategoryApi.md#category_delete) | **DELETE** /category.delete.json | 
[**category_find**](CategoryApi.md#category_find) | **GET** /category.find.json | 
[**category_image_add**](CategoryApi.md#category_image_add) | **POST** /category.image.add.json | 
[**category_image_delete**](CategoryApi.md#category_image_delete) | **DELETE** /category.image.delete.json | 
[**category_info**](CategoryApi.md#category_info) | **GET** /category.info.json | 
[**category_list**](CategoryApi.md#category_list) | **GET** /category.list.json | 
[**category_unassign**](CategoryApi.md#category_unassign) | **POST** /category.unassign.json | 
[**category_update**](CategoryApi.md#category_update) | **PUT** /category.update.json | 


# **category_add**
> InlineResponse20041 category_add(name, parent_id=parent_id, stores_ids=stores_ids, store_id=store_id, lang_id=lang_id, avail=avail, sort_order=sort_order, created_time=created_time, modified_time=modified_time, description=description, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, seo_url=seo_url)



Add new category in store

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Defines category's name that has to be added
parent_id = 'parent_id_example' # str | Adds categories specified by parent id (optional)
stores_ids = '0' # str | Create category in the stores that is specified by comma-separated stores' id (optional) (default to 0)
store_id = 'store_id_example' # str | Store Id (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
avail = true # bool | Defines category's visibility status (optional) (default to true)
sort_order = 0 # int | Sort number in the list (optional) (default to 0)
created_time = 'created_time_example' # str | Entity's date creation (optional)
modified_time = 'modified_time_example' # str | Entity's date modification (optional)
description = 'description_example' # str | Defines category's description (optional)
meta_title = 'meta_title_example' # str | Defines unique meta title for each entity (optional)
meta_description = 'meta_description_example' # str | Defines unique meta description of a entity (optional)
meta_keywords = 'meta_keywords_example' # str | Defines unique meta keywords for each entity (optional)
seo_url = 'seo_url_example' # str | Defines unique category's URL for SEO (optional)

try:
    api_response = api_instance.category_add(name, parent_id=parent_id, stores_ids=stores_ids, store_id=store_id, lang_id=lang_id, avail=avail, sort_order=sort_order, created_time=created_time, modified_time=modified_time, description=description, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, seo_url=seo_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Defines category&#39;s name that has to be added | 
 **parent_id** | **str**| Adds categories specified by parent id | [optional] 
 **stores_ids** | **str**| Create category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to 0]
 **store_id** | **str**| Store Id | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **avail** | **bool**| Defines category&#39;s visibility status | [optional] [default to true]
 **sort_order** | **int**| Sort number in the list | [optional] [default to 0]
 **created_time** | **str**| Entity&#39;s date creation | [optional] 
 **modified_time** | **str**| Entity&#39;s date modification | [optional] 
 **description** | **str**| Defines category&#39;s description | [optional] 
 **meta_title** | **str**| Defines unique meta title for each entity | [optional] 
 **meta_description** | **str**| Defines unique meta description of a entity | [optional] 
 **meta_keywords** | **str**| Defines unique meta keywords for each entity | [optional] 
 **seo_url** | **str**| Defines unique category&#39;s URL for SEO | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_assign**
> InlineResponse20014 category_assign(product_id, category_id)



Assign category to product

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
product_id = 'product_id_example' # str | Defines category assign to the product, specified by product id
category_id = 'category_id_example' # str | Defines category assign, specified by category id

try:
    api_response = api_instance.category_assign(product_id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Defines category assign to the product, specified by product id | 
 **category_id** | **str**| Defines category assign, specified by category id | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_count**
> InlineResponse20038 category_count(parent_id=parent_id, store_id=store_id, lang_id=lang_id)



Count categories in store.

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
parent_id = 'parent_id_example' # str | Counts categories specified by parent id (optional)
store_id = 'store_id_example' # str | Counts category specified by store id (optional)
lang_id = 'lang_id_example' # str | Counts category specified by language id (optional)

try:
    api_response = api_instance.category_count(parent_id=parent_id, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| Counts categories specified by parent id | [optional] 
 **store_id** | **str**| Counts category specified by store id | [optional] 
 **lang_id** | **str**| Counts category specified by language id | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_delete**
> InlineResponse2004 category_delete(id)



Delete category in store

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines category removal, specified by category id

try:
    api_response = api_instance.category_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines category removal, specified by category id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_find**
> InlineResponse20040 category_find(find_value, find_where=find_where, find_params=find_params)



Search category in store. \"Laptop\" is specified here by default.

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
find_value = 'find_value_example' # str | Entity search that is specified by some value
find_where = 'name' # str | Entity search that is specified by the comma-separated unique fields (optional) (default to name)
find_params = 'whole_words' # str | Entity search that is specified by comma-separated parameters (optional) (default to whole_words)

try:
    api_response = api_instance.category_find(find_value, find_where=find_where, find_params=find_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_value** | **str**| Entity search that is specified by some value | 
 **find_where** | **str**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name]
 **find_params** | **str**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words]

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_image_add**
> InlineResponse20042 category_image_add(category_id, image_name, url, type, label=label, mime=mime, position=position, store_id=store_id)



Add image to category

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str | Defines category id where the image should be added
image_name = 'image_name_example' # str | Defines image's name
url = 'url_example' # str | Defines URL of the image that has to be added
type = 'type_example' # str | Defines image's types that are specified by comma-separated list
label = 'label_example' # str | Defines alternative text that has to be attached to the picture (optional)
mime = 'mime_example' # str | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. (optional)
position = 0 # int | Defines image’s position in the list (optional) (default to 0)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.category_image_add(category_id, image_name, url, type, label=label, mime=mime, position=position, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_image_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Defines category id where the image should be added | 
 **image_name** | **str**| Defines image&#39;s name | 
 **url** | **str**| Defines URL of the image that has to be added | 
 **type** | **str**| Defines image&#39;s types that are specified by comma-separated list | 
 **label** | **str**| Defines alternative text that has to be attached to the picture | [optional] 
 **mime** | **str**| Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. | [optional] 
 **position** | **int**| Defines image’s position in the list | [optional] [default to 0]
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_image_delete**
> InlineResponse2004 category_image_delete(category_id, image_id, store_id=store_id)



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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str | Defines category id where the image should be deleted
image_id = 'image_id_example' # str | Define image id
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.category_image_delete(category_id, image_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_image_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Defines category id where the image should be deleted | 
 **image_id** | **str**| Define image id | 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_info**
> InlineResponse20039 category_info(id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)



Get category info about category ID*** or specify other category ID.

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Retrieves category's info specified by category id
params = 'id,parent_id,name,description' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,parent_id,name,description)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Retrieves category info  specified by store id (optional)
lang_id = 'lang_id_example' # str | Retrieves category info  specified by language id (optional)

try:
    api_response = api_instance.category_info(id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Retrieves category&#39;s info specified by category id | 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,parent_id,name,description]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Retrieves category info  specified by store id | [optional] 
 **lang_id** | **str**| Retrieves category info  specified by language id | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_list**
> ModelResponseCategoryList category_list(start=start, count=count, page_cursor=page_cursor, parent_id=parent_id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)



Get list of categories from store.

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
page_cursor = 'page_cursor_example' # str | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter) (optional)
parent_id = 'parent_id_example' # str | Retrieves categories specified by parent id (optional)
params = 'id,parent_id,name,description' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,parent_id,name,description)
exclude = 'exclude_example' # str | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all (optional)
store_id = 'store_id_example' # str | Retrieves categories specified by store id (optional)
lang_id = 'lang_id_example' # str | Retrieves categorys specified by language id (optional)

try:
    api_response = api_instance.category_list(start=start, count=count, page_cursor=page_cursor, parent_id=parent_id, params=params, exclude=exclude, store_id=store_id, lang_id=lang_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **page_cursor** | **str**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **parent_id** | **str**| Retrieves categories specified by parent id | [optional] 
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,parent_id,name,description]
 **exclude** | **str**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **store_id** | **str**| Retrieves categories specified by store id | [optional] 
 **lang_id** | **str**| Retrieves categorys specified by language id | [optional] 

### Return type

[**ModelResponseCategoryList**](ModelResponseCategoryList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_unassign**
> InlineResponse20014 category_unassign(category_id, product_id)



Unassign category to product

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str | Defines category unassign, specified by category id
product_id = 'product_id_example' # str | Defines category unassign to the product, specified by product id

try:
    api_response = api_instance.category_unassign(category_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_unassign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| Defines category unassign, specified by category id | 
 **product_id** | **str**| Defines category unassign to the product, specified by product id | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_update**
> InlineResponse20028 category_update(id, name=name, parent_id=parent_id, stores_ids=stores_ids, avail=avail, sort_order=sort_order, modified_time=modified_time, description=description, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, seo_url=seo_url, lang_id=lang_id, store_id=store_id)



Update category in store

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Defines category update specified by category id
name = 'name_example' # str | Defines new category’s name (optional)
parent_id = 'parent_id_example' # str | Defines new parent category id (optional)
stores_ids = '0' # str | Update category in the stores that is specified by comma-separated stores' id (optional) (default to 0)
avail = true # bool | Defines category's visibility status (optional)
sort_order = 56 # int | Sort number in the list (optional)
modified_time = 'modified_time_example' # str | Entity's date modification (optional)
description = 'description_example' # str | Defines new category's description (optional)
meta_title = 'meta_title_example' # str | Defines unique meta title for each entity (optional)
meta_description = 'meta_description_example' # str | Defines unique meta description of a entity (optional)
meta_keywords = 'meta_keywords_example' # str | Defines unique meta keywords for each entity (optional)
seo_url = 'seo_url_example' # str | Defines unique category's URL for SEO (optional)
lang_id = 'lang_id_example' # str | Language id (optional)
store_id = 'store_id_example' # str | Store Id (optional)

try:
    api_response = api_instance.category_update(id, name=name, parent_id=parent_id, stores_ids=stores_ids, avail=avail, sort_order=sort_order, modified_time=modified_time, description=description, meta_title=meta_title, meta_description=meta_description, meta_keywords=meta_keywords, seo_url=seo_url, lang_id=lang_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Defines category update specified by category id | 
 **name** | **str**| Defines new category’s name | [optional] 
 **parent_id** | **str**| Defines new parent category id | [optional] 
 **stores_ids** | **str**| Update category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to 0]
 **avail** | **bool**| Defines category&#39;s visibility status | [optional] 
 **sort_order** | **int**| Sort number in the list | [optional] 
 **modified_time** | **str**| Entity&#39;s date modification | [optional] 
 **description** | **str**| Defines new category&#39;s description | [optional] 
 **meta_title** | **str**| Defines unique meta title for each entity | [optional] 
 **meta_description** | **str**| Defines unique meta description of a entity | [optional] 
 **meta_keywords** | **str**| Defines unique meta keywords for each entity | [optional] 
 **seo_url** | **str**| Defines unique category&#39;s URL for SEO | [optional] 
 **lang_id** | **str**| Language id | [optional] 
 **store_id** | **str**| Store Id | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

