# swagger_client.WebhookApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_count**](WebhookApi.md#webhook_count) | **GET** /webhook.count.json | 
[**webhook_create**](WebhookApi.md#webhook_create) | **POST** /webhook.create.json | 
[**webhook_delete**](WebhookApi.md#webhook_delete) | **DELETE** /webhook.delete.json | 
[**webhook_events**](WebhookApi.md#webhook_events) | **GET** /webhook.events.json | 
[**webhook_list**](WebhookApi.md#webhook_list) | **GET** /webhook.list.json | 
[**webhook_update**](WebhookApi.md#webhook_update) | **PUT** /webhook.update.json | 


# **webhook_count**
> InlineResponse2002 webhook_count(entity=entity, action=action, active=active)



Count registered webhooks on the store.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The entity you want to filter webhooks by (e.g. order or product) (optional)
action = 'action_example' # str | The action you want to filter webhooks by (e.g. order or product) (optional)
active = true # bool | The webhook status you want to filter webhooks by (optional)

try:
    api_response = api_instance.webhook_count(entity=entity, action=action, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The entity you want to filter webhooks by (e.g. order or product) | [optional] 
 **action** | **str**| The action you want to filter webhooks by (e.g. order or product) | [optional] 
 **active** | **bool**| The webhook status you want to filter webhooks by | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_create**
> InlineResponse200 webhook_create(entity, action, param_callback, label=label, fields=fields, active=active, store_id=store_id)



Create webhook on the store and subscribe to it.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | Specify the entity that you want to enable webhooks for (e.g product, order, customer, category)
action = 'action_example' # str | Specify what action (event) will trigger the webhook (e.g add, delete, or update)
param_callback = 'param_callback_example' # str | Callback where the webhook should send the POST request when the event occurs
label = 'label_example' # str | The name you give to the webhook (optional)
fields = 'id' # str | Fields the webhook should send (optional) (default to id)
active = true # bool | Webhook status (optional) (default to true)
store_id = 'store_id_example' # str | Defines store id where the webhook should be assigned (optional)

try:
    api_response = api_instance.webhook_create(entity, action, param_callback, label=label, fields=fields, active=active, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| Specify the entity that you want to enable webhooks for (e.g product, order, customer, category) | 
 **action** | **str**| Specify what action (event) will trigger the webhook (e.g add, delete, or update) | 
 **param_callback** | **str**| Callback where the webhook should send the POST request when the event occurs | 
 **label** | **str**| The name you give to the webhook | [optional] 
 **fields** | **str**| Fields the webhook should send | [optional] [default to id]
 **active** | **bool**| Webhook status | [optional] [default to true]
 **store_id** | **str**| Defines store id where the webhook should be assigned | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_delete**
> InlineResponse2004 webhook_delete(id)



Delete registered webhook on the store.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Webhook id

try:
    api_response = api_instance.webhook_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_events**
> InlineResponse2003 webhook_events()



List all Webhooks that are available on this store.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.webhook_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_list**
> InlineResponse2001 webhook_list(params=params, start=start, count=count, entity=entity, action=action, active=active, ids=ids)



List registered webhook on the store.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
params = 'id,entity,action,callback' # str | Set this parameter in order to choose which entity fields you want to retrieve (optional) (default to id,entity,action,callback)
start = 0 # int | This parameter sets the number from which you want to get entities (optional) (default to 0)
count = 10 # int | This parameter sets the entity amount that has to be retrieved. Max allowed count=250 (optional) (default to 10)
entity = 'entity_example' # str | The entity you want to filter webhooks by (e.g. order or product) (optional)
action = 'action_example' # str | The action you want to filter webhooks by (e.g. add, update, or delete) (optional)
active = true # bool | The webhook status you want to filter webhooks by (optional)
ids = 'ids_example' # str | List of сomma-separated webhook ids (optional)

try:
    api_response = api_instance.webhook_list(params=params, start=start, count=count, entity=entity, action=action, active=active, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **str**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,entity,action,callback]
 **start** | **int**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **int**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **entity** | **str**| The entity you want to filter webhooks by (e.g. order or product) | [optional] 
 **action** | **str**| The action you want to filter webhooks by (e.g. add, update, or delete) | [optional] 
 **active** | **bool**| The webhook status you want to filter webhooks by | [optional] 
 **ids** | **str**| List of сomma-separated webhook ids | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_update**
> InlineResponse2005 webhook_update(id, param_callback=param_callback, label=label, fields=fields, active=active)



Update Webhooks parameters.

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Webhook id
param_callback = 'param_callback_example' # str | Callback where the webhook should send the POST request when the event occurs (optional)
label = 'label_example' # str | The name you give to the webhook (optional)
fields = 'fields_example' # str | Fields the webhook should send (optional)
active = true # bool | Webhook status (optional)

try:
    api_response = api_instance.webhook_update(id, param_callback=param_callback, label=label, fields=fields, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook id | 
 **param_callback** | **str**| Callback where the webhook should send the POST request when the event occurs | [optional] 
 **label** | **str**| The name you give to the webhook | [optional] 
 **fields** | **str**| Fields the webhook should send | [optional] 
 **active** | **bool**| Webhook status | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

