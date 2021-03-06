# swagger-client
API2Cart

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCartAdd() # AccountCartAdd | 

try:
    api_response = api_instance.account_cart_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_cart_add: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.api2cart.com/v1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_cart_add**](docs/AccountApi.md#account_cart_add) | **POST** /account.cart.add.json | 
*AccountApi* | [**account_cart_list**](docs/AccountApi.md#account_cart_list) | **GET** /account.cart.list.json | 
*AccountApi* | [**account_config_update**](docs/AccountApi.md#account_config_update) | **PUT** /account.config.update.json | 
*AccountApi* | [**account_failed_webhooks**](docs/AccountApi.md#account_failed_webhooks) | **GET** /account.failed_webhooks.json | 
*AccountApi* | [**account_supported_platforms**](docs/AccountApi.md#account_supported_platforms) | **GET** /account.supported_platforms.json | 
*AttributeApi* | [**attribute_add**](docs/AttributeApi.md#attribute_add) | **POST** /attribute.add.json | 
*AttributeApi* | [**attribute_assign_group**](docs/AttributeApi.md#attribute_assign_group) | **POST** /attribute.assign.group.json | 
*AttributeApi* | [**attribute_assign_set**](docs/AttributeApi.md#attribute_assign_set) | **POST** /attribute.assign.set.json | 
*AttributeApi* | [**attribute_attributeset_list**](docs/AttributeApi.md#attribute_attributeset_list) | **GET** /attribute.attributeset.list.json | 
*AttributeApi* | [**attribute_count**](docs/AttributeApi.md#attribute_count) | **GET** /attribute.count.json | 
*AttributeApi* | [**attribute_delete**](docs/AttributeApi.md#attribute_delete) | **DELETE** /attribute.delete.json | 
*AttributeApi* | [**attribute_group_list**](docs/AttributeApi.md#attribute_group_list) | **GET** /attribute.group.list.json | 
*AttributeApi* | [**attribute_info**](docs/AttributeApi.md#attribute_info) | **GET** /attribute.info.json | 
*AttributeApi* | [**attribute_list**](docs/AttributeApi.md#attribute_list) | **GET** /attribute.list.json | 
*AttributeApi* | [**attribute_type_list**](docs/AttributeApi.md#attribute_type_list) | **GET** /attribute.type.list.json | 
*AttributeApi* | [**attribute_unassign_group**](docs/AttributeApi.md#attribute_unassign_group) | **POST** /attribute.unassign.group.json | 
*AttributeApi* | [**attribute_unassign_set**](docs/AttributeApi.md#attribute_unassign_set) | **POST** /attribute.unassign.set.json | 
*AttributeApi* | [**attribute_update**](docs/AttributeApi.md#attribute_update) | **POST** /attribute.update.json | 
*BasketApi* | [**basket_info**](docs/BasketApi.md#basket_info) | **GET** /basket.info.json | 
*BasketApi* | [**basket_item_add**](docs/BasketApi.md#basket_item_add) | **POST** /basket.item.add.json | 
*BasketApi* | [**basket_live_shipping_service_create**](docs/BasketApi.md#basket_live_shipping_service_create) | **POST** /basket.live_shipping_service.create.json | 
*BasketApi* | [**basket_live_shipping_service_delete**](docs/BasketApi.md#basket_live_shipping_service_delete) | **DELETE** /basket.live_shipping_service.delete.json | 
*BasketApi* | [**basket_live_shipping_service_list**](docs/BasketApi.md#basket_live_shipping_service_list) | **GET** /basket.live_shipping_service.list.json | 
*BridgeApi* | [**bridge_delete**](docs/BridgeApi.md#bridge_delete) | **POST** /bridge.delete.json | 
*BridgeApi* | [**bridge_update**](docs/BridgeApi.md#bridge_update) | **POST** /bridge.update.json | 
*CartApi* | [**bridge_download**](docs/CartApi.md#bridge_download) | **GET** /bridge.download.file | 
*CartApi* | [**cart_bridge**](docs/CartApi.md#cart_bridge) | **GET** /cart.bridge.json | 
*CartApi* | [**cart_catalog_price_rules_count**](docs/CartApi.md#cart_catalog_price_rules_count) | **GET** /cart.catalog_price_rules.count.json | 
*CartApi* | [**cart_catalog_price_rules_list**](docs/CartApi.md#cart_catalog_price_rules_list) | **GET** /cart.catalog_price_rules.list.json | 
*CartApi* | [**cart_clear_cache**](docs/CartApi.md#cart_clear_cache) | **POST** /cart.clear_cache.json | 
*CartApi* | [**cart_config**](docs/CartApi.md#cart_config) | **GET** /cart.config.json | 
*CartApi* | [**cart_config_update**](docs/CartApi.md#cart_config_update) | **PUT** /cart.config.update.json | 
*CartApi* | [**cart_coupon_add**](docs/CartApi.md#cart_coupon_add) | **POST** /cart.coupon.add.json | 
*CartApi* | [**cart_coupon_condition_add**](docs/CartApi.md#cart_coupon_condition_add) | **POST** /cart.coupon.condition.add.json | 
*CartApi* | [**cart_coupon_count**](docs/CartApi.md#cart_coupon_count) | **GET** /cart.coupon.count.json | 
*CartApi* | [**cart_coupon_delete**](docs/CartApi.md#cart_coupon_delete) | **DELETE** /cart.coupon.delete.json | 
*CartApi* | [**cart_coupon_list**](docs/CartApi.md#cart_coupon_list) | **GET** /cart.coupon.list.json | 
*CartApi* | [**cart_create**](docs/CartApi.md#cart_create) | **POST** /cart.create.json | 
*CartApi* | [**cart_delete**](docs/CartApi.md#cart_delete) | **DELETE** /cart.delete.json | 
*CartApi* | [**cart_disconnect**](docs/CartApi.md#cart_disconnect) | **GET** /cart.disconnect.json | 
*CartApi* | [**cart_giftcard_add**](docs/CartApi.md#cart_giftcard_add) | **POST** /cart.giftcard.add.json | 
*CartApi* | [**cart_giftcard_count**](docs/CartApi.md#cart_giftcard_count) | **GET** /cart.giftcard.count.json | 
*CartApi* | [**cart_giftcard_list**](docs/CartApi.md#cart_giftcard_list) | **GET** /cart.giftcard.list.json | 
*CartApi* | [**cart_info**](docs/CartApi.md#cart_info) | **GET** /cart.info.json | 
*CartApi* | [**cart_list**](docs/CartApi.md#cart_list) | **GET** /cart.list.json | 
*CartApi* | [**cart_meta_data_list**](docs/CartApi.md#cart_meta_data_list) | **GET** /cart.meta_data.list.json | 
*CartApi* | [**cart_meta_data_set**](docs/CartApi.md#cart_meta_data_set) | **POST** /cart.meta_data.set.json | 
*CartApi* | [**cart_meta_data_unset**](docs/CartApi.md#cart_meta_data_unset) | **DELETE** /cart.meta_data.unset.json | 
*CartApi* | [**cart_methods**](docs/CartApi.md#cart_methods) | **GET** /cart.methods.json | 
*CartApi* | [**cart_plugin_list**](docs/CartApi.md#cart_plugin_list) | **GET** /cart.plugin.list.json | 
*CartApi* | [**cart_script_add**](docs/CartApi.md#cart_script_add) | **POST** /cart.script.add.json | 
*CartApi* | [**cart_script_delete**](docs/CartApi.md#cart_script_delete) | **DELETE** /cart.script.delete.json | 
*CartApi* | [**cart_script_list**](docs/CartApi.md#cart_script_list) | **GET** /cart.script.list.json | 
*CartApi* | [**cart_shipping_zones_list**](docs/CartApi.md#cart_shipping_zones_list) | **GET** /cart.shipping_zones.list.json | 
*CartApi* | [**cart_validate**](docs/CartApi.md#cart_validate) | **GET** /cart.validate.json | 
*CategoryApi* | [**category_add**](docs/CategoryApi.md#category_add) | **POST** /category.add.json | 
*CategoryApi* | [**category_assign**](docs/CategoryApi.md#category_assign) | **POST** /category.assign.json | 
*CategoryApi* | [**category_count**](docs/CategoryApi.md#category_count) | **GET** /category.count.json | 
*CategoryApi* | [**category_delete**](docs/CategoryApi.md#category_delete) | **DELETE** /category.delete.json | 
*CategoryApi* | [**category_find**](docs/CategoryApi.md#category_find) | **GET** /category.find.json | 
*CategoryApi* | [**category_image_add**](docs/CategoryApi.md#category_image_add) | **POST** /category.image.add.json | 
*CategoryApi* | [**category_image_delete**](docs/CategoryApi.md#category_image_delete) | **DELETE** /category.image.delete.json | 
*CategoryApi* | [**category_info**](docs/CategoryApi.md#category_info) | **GET** /category.info.json | 
*CategoryApi* | [**category_list**](docs/CategoryApi.md#category_list) | **GET** /category.list.json | 
*CategoryApi* | [**category_unassign**](docs/CategoryApi.md#category_unassign) | **POST** /category.unassign.json | 
*CategoryApi* | [**category_update**](docs/CategoryApi.md#category_update) | **PUT** /category.update.json | 
*CustomerApi* | [**customer_add**](docs/CustomerApi.md#customer_add) | **POST** /customer.add.json | 
*CustomerApi* | [**customer_attribute_list**](docs/CustomerApi.md#customer_attribute_list) | **GET** /customer.attribute.list.json | 
*CustomerApi* | [**customer_count**](docs/CustomerApi.md#customer_count) | **GET** /customer.count.json | 
*CustomerApi* | [**customer_find**](docs/CustomerApi.md#customer_find) | **GET** /customer.find.json | 
*CustomerApi* | [**customer_group_add**](docs/CustomerApi.md#customer_group_add) | **POST** /customer.group.add.json | 
*CustomerApi* | [**customer_group_list**](docs/CustomerApi.md#customer_group_list) | **GET** /customer.group.list.json | 
*CustomerApi* | [**customer_info**](docs/CustomerApi.md#customer_info) | **GET** /customer.info.json | 
*CustomerApi* | [**customer_list**](docs/CustomerApi.md#customer_list) | **GET** /customer.list.json | 
*CustomerApi* | [**customer_update**](docs/CustomerApi.md#customer_update) | **PUT** /customer.update.json | 
*OrderApi* | [**order_abandoned_list**](docs/OrderApi.md#order_abandoned_list) | **GET** /order.abandoned.list.json | 
*OrderApi* | [**order_add**](docs/OrderApi.md#order_add) | **POST** /order.add.json | 
*OrderApi* | [**order_count**](docs/OrderApi.md#order_count) | **GET** /order.count.json | 
*OrderApi* | [**order_financial_status_list**](docs/OrderApi.md#order_financial_status_list) | **GET** /order.financial_status.list.json | 
*OrderApi* | [**order_find**](docs/OrderApi.md#order_find) | **GET** /order.find.json | 
*OrderApi* | [**order_fulfillment_status_list**](docs/OrderApi.md#order_fulfillment_status_list) | **GET** /order.fulfillment_status.list.json | 
*OrderApi* | [**order_info**](docs/OrderApi.md#order_info) | **GET** /order.info.json | 
*OrderApi* | [**order_list**](docs/OrderApi.md#order_list) | **GET** /order.list.json | 
*OrderApi* | [**order_refund_add**](docs/OrderApi.md#order_refund_add) | **POST** /order.refund.add.json | 
*OrderApi* | [**order_shipment_add**](docs/OrderApi.md#order_shipment_add) | **POST** /order.shipment.add.json | 
*OrderApi* | [**order_shipment_delete**](docs/OrderApi.md#order_shipment_delete) | **DELETE** /order.shipment.delete.json | 
*OrderApi* | [**order_shipment_list**](docs/OrderApi.md#order_shipment_list) | **GET** /order.shipment.list.json | 
*OrderApi* | [**order_shipment_tracking_add**](docs/OrderApi.md#order_shipment_tracking_add) | **POST** /order.shipment.tracking.add.json | 
*OrderApi* | [**order_shipment_update**](docs/OrderApi.md#order_shipment_update) | **PUT** /order.shipment.update.json | 
*OrderApi* | [**order_status_list**](docs/OrderApi.md#order_status_list) | **GET** /order.status.list.json | 
*OrderApi* | [**order_update**](docs/OrderApi.md#order_update) | **PUT** /order.update.json | 
*ProductApi* | [**product_add**](docs/ProductApi.md#product_add) | **POST** /product.add.json | 
*ProductApi* | [**product_attribute_list**](docs/ProductApi.md#product_attribute_list) | **GET** /product.attribute.list.json | 
*ProductApi* | [**product_attribute_value_set**](docs/ProductApi.md#product_attribute_value_set) | **POST** /product.attribute.value.set.json | 
*ProductApi* | [**product_attribute_value_unset**](docs/ProductApi.md#product_attribute_value_unset) | **POST** /product.attribute.value.unset.json | 
*ProductApi* | [**product_brand_list**](docs/ProductApi.md#product_brand_list) | **GET** /product.brand.list.json | 
*ProductApi* | [**product_child_item_find**](docs/ProductApi.md#product_child_item_find) | **GET** /product.child_item.find.json | 
*ProductApi* | [**product_child_item_info**](docs/ProductApi.md#product_child_item_info) | **GET** /product.child_item.info.json | 
*ProductApi* | [**product_child_item_list**](docs/ProductApi.md#product_child_item_list) | **GET** /product.child_item.list.json | 
*ProductApi* | [**product_count**](docs/ProductApi.md#product_count) | **GET** /product.count.json | 
*ProductApi* | [**product_currency_add**](docs/ProductApi.md#product_currency_add) | **POST** /product.currency.add.json | 
*ProductApi* | [**product_currency_list**](docs/ProductApi.md#product_currency_list) | **GET** /product.currency.list.json | 
*ProductApi* | [**product_delete**](docs/ProductApi.md#product_delete) | **DELETE** /product.delete.json | 
*ProductApi* | [**product_fields**](docs/ProductApi.md#product_fields) | **GET** /product.fields.json | 
*ProductApi* | [**product_find**](docs/ProductApi.md#product_find) | **GET** /product.find.json | 
*ProductApi* | [**product_image_add**](docs/ProductApi.md#product_image_add) | **POST** /product.image.add.json | 
*ProductApi* | [**product_image_delete**](docs/ProductApi.md#product_image_delete) | **DELETE** /product.image.delete.json | 
*ProductApi* | [**product_image_update**](docs/ProductApi.md#product_image_update) | **PUT** /product.image.update.json | 
*ProductApi* | [**product_info**](docs/ProductApi.md#product_info) | **GET** /product.info.json | 
*ProductApi* | [**product_list**](docs/ProductApi.md#product_list) | **GET** /product.list.json | 
*ProductApi* | [**product_manufacturer_add**](docs/ProductApi.md#product_manufacturer_add) | **POST** /product.manufacturer.add.json | 
*ProductApi* | [**product_option_add**](docs/ProductApi.md#product_option_add) | **POST** /product.option.add.json | 
*ProductApi* | [**product_option_assign**](docs/ProductApi.md#product_option_assign) | **POST** /product.option.assign.json | 
*ProductApi* | [**product_option_list**](docs/ProductApi.md#product_option_list) | **GET** /product.option.list.json | 
*ProductApi* | [**product_option_value_add**](docs/ProductApi.md#product_option_value_add) | **POST** /product.option.value.add.json | 
*ProductApi* | [**product_option_value_assign**](docs/ProductApi.md#product_option_value_assign) | **POST** /product.option.value.assign.json | 
*ProductApi* | [**product_option_value_update**](docs/ProductApi.md#product_option_value_update) | **PUT** /product.option.value.update.json | 
*ProductApi* | [**product_price_add**](docs/ProductApi.md#product_price_add) | **POST** /product.price.add.json | 
*ProductApi* | [**product_price_delete**](docs/ProductApi.md#product_price_delete) | **DELETE** /product.price.delete.json | 
*ProductApi* | [**product_price_update**](docs/ProductApi.md#product_price_update) | **PUT** /product.price.update.json | 
*ProductApi* | [**product_review_list**](docs/ProductApi.md#product_review_list) | **GET** /product.review.list.json | 
*ProductApi* | [**product_store_assign**](docs/ProductApi.md#product_store_assign) | **POST** /product.store.assign.json | 
*ProductApi* | [**product_tax_add**](docs/ProductApi.md#product_tax_add) | **POST** /product.tax.add.json | 
*ProductApi* | [**product_update**](docs/ProductApi.md#product_update) | **PUT** /product.update.json | 
*ProductApi* | [**product_variant_add**](docs/ProductApi.md#product_variant_add) | **POST** /product.variant.add.json | 
*ProductApi* | [**product_variant_count**](docs/ProductApi.md#product_variant_count) | **GET** /product.variant.count.json | 
*ProductApi* | [**product_variant_delete**](docs/ProductApi.md#product_variant_delete) | **DELETE** /product.variant.delete.json | 
*ProductApi* | [**product_variant_image_add**](docs/ProductApi.md#product_variant_image_add) | **POST** /product.variant.image.add.json | 
*ProductApi* | [**product_variant_info**](docs/ProductApi.md#product_variant_info) | **GET** /product.variant.info.json | 
*ProductApi* | [**product_variant_list**](docs/ProductApi.md#product_variant_list) | **GET** /product.variant.list.json | 
*ProductApi* | [**product_variant_price_add**](docs/ProductApi.md#product_variant_price_add) | **POST** /product.variant.price.add.json | 
*ProductApi* | [**product_variant_price_delete**](docs/ProductApi.md#product_variant_price_delete) | **DELETE** /product.variant.price.delete.json | 
*ProductApi* | [**product_variant_price_update**](docs/ProductApi.md#product_variant_price_update) | **PUT** /product.variant.price.update.json | 
*ProductApi* | [**product_variant_update**](docs/ProductApi.md#product_variant_update) | **PUT** /product.variant.update.json | 
*SubscriberApi* | [**subscriber_list**](docs/SubscriberApi.md#subscriber_list) | **GET** /subscriber.list.json | 
*TaxApi* | [**tax_class_info**](docs/TaxApi.md#tax_class_info) | **GET** /tax.class.info.json | 
*WebhookApi* | [**webhook_count**](docs/WebhookApi.md#webhook_count) | **GET** /webhook.count.json | 
*WebhookApi* | [**webhook_create**](docs/WebhookApi.md#webhook_create) | **POST** /webhook.create.json | 
*WebhookApi* | [**webhook_delete**](docs/WebhookApi.md#webhook_delete) | **DELETE** /webhook.delete.json | 
*WebhookApi* | [**webhook_events**](docs/WebhookApi.md#webhook_events) | **GET** /webhook.events.json | 
*WebhookApi* | [**webhook_list**](docs/WebhookApi.md#webhook_list) | **GET** /webhook.list.json | 
*WebhookApi* | [**webhook_update**](docs/WebhookApi.md#webhook_update) | **PUT** /webhook.update.json | 


## Documentation For Models

 - [A2CDateTime](docs/A2CDateTime.md)
 - [AccountCartAdd](docs/AccountCartAdd.md)
 - [AccountCartAddHybrisWebsites](docs/AccountCartAddHybrisWebsites.md)
 - [BaseCustomer](docs/BaseCustomer.md)
 - [Basket](docs/Basket.md)
 - [BasketItem](docs/BasketItem.md)
 - [BasketItemOption](docs/BasketItemOption.md)
 - [BasketLiveShippingService](docs/BasketLiveShippingService.md)
 - [Brand](docs/Brand.md)
 - [Carrier](docs/Carrier.md)
 - [Cart](docs/Cart.md)
 - [CartChannel](docs/CartChannel.md)
 - [CartConfigUpdate](docs/CartConfigUpdate.md)
 - [CartCouponAdd](docs/CartCouponAdd.md)
 - [CartMetaData](docs/CartMetaData.md)
 - [CartShippingZone](docs/CartShippingZone.md)
 - [CartStoreInfo](docs/CartStoreInfo.md)
 - [CartWarehouse](docs/CartWarehouse.md)
 - [CatalogPriceRule](docs/CatalogPriceRule.md)
 - [CatalogPriceRuleAction](docs/CatalogPriceRuleAction.md)
 - [Category](docs/Category.md)
 - [Child](docs/Child.md)
 - [ChildCombination](docs/ChildCombination.md)
 - [Country](docs/Country.md)
 - [Coupon](docs/Coupon.md)
 - [CouponAction](docs/CouponAction.md)
 - [CouponCode](docs/CouponCode.md)
 - [CouponCondition](docs/CouponCondition.md)
 - [CouponHistory](docs/CouponHistory.md)
 - [Currency](docs/Currency.md)
 - [Customer](docs/Customer.md)
 - [CustomerAdd](docs/CustomerAdd.md)
 - [CustomerAddAddress](docs/CustomerAddAddress.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerAttribute](docs/CustomerAttribute.md)
 - [CustomerAttributeValue](docs/CustomerAttributeValue.md)
 - [CustomerGroup](docs/CustomerGroup.md)
 - [GiftCard](docs/GiftCard.md)
 - [Image](docs/Image.md)
 - [Info](docs/Info.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20010Result](docs/InlineResponse20010Result.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20011Result](docs/InlineResponse20011Result.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20012Result](docs/InlineResponse20012Result.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013Result](docs/InlineResponse20013Result.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20015Result](docs/InlineResponse20015Result.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20016Result](docs/InlineResponse20016Result.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20017Result](docs/InlineResponse20017Result.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20018Result](docs/InlineResponse20018Result.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse20019Result](docs/InlineResponse20019Result.md)
 - [InlineResponse2001Result](docs/InlineResponse2001Result.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20020Result](docs/InlineResponse20020Result.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20021Result](docs/InlineResponse20021Result.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20022Result](docs/InlineResponse20022Result.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20024Result](docs/InlineResponse20024Result.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20025Result](docs/InlineResponse20025Result.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20027Result](docs/InlineResponse20027Result.md)
 - [InlineResponse20027ResultCarts](docs/InlineResponse20027ResultCarts.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20028Result](docs/InlineResponse20028Result.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse20029Result](docs/InlineResponse20029Result.md)
 - [InlineResponse20029ResultWebhook](docs/InlineResponse20029ResultWebhook.md)
 - [InlineResponse2002Result](docs/InlineResponse2002Result.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse20030Result](docs/InlineResponse20030Result.md)
 - [InlineResponse20030ResultParams](docs/InlineResponse20030ResultParams.md)
 - [InlineResponse20030ResultParamsAdditional](docs/InlineResponse20030ResultParamsAdditional.md)
 - [InlineResponse20030ResultSupportedPlatforms](docs/InlineResponse20030ResultSupportedPlatforms.md)
 - [InlineResponse20031](docs/InlineResponse20031.md)
 - [InlineResponse20031Result](docs/InlineResponse20031Result.md)
 - [InlineResponse20032](docs/InlineResponse20032.md)
 - [InlineResponse20032Result](docs/InlineResponse20032Result.md)
 - [InlineResponse20033](docs/InlineResponse20033.md)
 - [InlineResponse20034](docs/InlineResponse20034.md)
 - [InlineResponse20034Result](docs/InlineResponse20034Result.md)
 - [InlineResponse20034ResultProduct](docs/InlineResponse20034ResultProduct.md)
 - [InlineResponse20035](docs/InlineResponse20035.md)
 - [InlineResponse20035Result](docs/InlineResponse20035Result.md)
 - [InlineResponse20036](docs/InlineResponse20036.md)
 - [InlineResponse20036Result](docs/InlineResponse20036Result.md)
 - [InlineResponse20037](docs/InlineResponse20037.md)
 - [InlineResponse20037Result](docs/InlineResponse20037Result.md)
 - [InlineResponse20038](docs/InlineResponse20038.md)
 - [InlineResponse20038Result](docs/InlineResponse20038Result.md)
 - [InlineResponse20039](docs/InlineResponse20039.md)
 - [InlineResponse2003Result](docs/InlineResponse2003Result.md)
 - [InlineResponse2003ResultEvents](docs/InlineResponse2003ResultEvents.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse20040](docs/InlineResponse20040.md)
 - [InlineResponse20040Result](docs/InlineResponse20040Result.md)
 - [InlineResponse20040ResultCategory](docs/InlineResponse20040ResultCategory.md)
 - [InlineResponse20041](docs/InlineResponse20041.md)
 - [InlineResponse20041Result](docs/InlineResponse20041Result.md)
 - [InlineResponse20042](docs/InlineResponse20042.md)
 - [InlineResponse20042Result](docs/InlineResponse20042Result.md)
 - [InlineResponse20043](docs/InlineResponse20043.md)
 - [InlineResponse20043Result](docs/InlineResponse20043Result.md)
 - [InlineResponse20044](docs/InlineResponse20044.md)
 - [InlineResponse20045](docs/InlineResponse20045.md)
 - [InlineResponse20045Result](docs/InlineResponse20045Result.md)
 - [InlineResponse20046](docs/InlineResponse20046.md)
 - [InlineResponse20046Result](docs/InlineResponse20046Result.md)
 - [InlineResponse20047](docs/InlineResponse20047.md)
 - [InlineResponse20047Result](docs/InlineResponse20047Result.md)
 - [InlineResponse20047ResultCartOrderStatuses](docs/InlineResponse20047ResultCartOrderStatuses.md)
 - [InlineResponse20048](docs/InlineResponse20048.md)
 - [InlineResponse20048Result](docs/InlineResponse20048Result.md)
 - [InlineResponse20049](docs/InlineResponse20049.md)
 - [InlineResponse20049Result](docs/InlineResponse20049Result.md)
 - [InlineResponse2004Result](docs/InlineResponse2004Result.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse20050](docs/InlineResponse20050.md)
 - [InlineResponse20050Result](docs/InlineResponse20050Result.md)
 - [InlineResponse20051](docs/InlineResponse20051.md)
 - [InlineResponse20051Result](docs/InlineResponse20051Result.md)
 - [InlineResponse20052](docs/InlineResponse20052.md)
 - [InlineResponse20052Result](docs/InlineResponse20052Result.md)
 - [InlineResponse20053](docs/InlineResponse20053.md)
 - [InlineResponse20053Result](docs/InlineResponse20053Result.md)
 - [InlineResponse20054](docs/InlineResponse20054.md)
 - [InlineResponse20054Result](docs/InlineResponse20054Result.md)
 - [InlineResponse20055](docs/InlineResponse20055.md)
 - [InlineResponse20056](docs/InlineResponse20056.md)
 - [InlineResponse20056Result](docs/InlineResponse20056Result.md)
 - [InlineResponse20057](docs/InlineResponse20057.md)
 - [InlineResponse20057Result](docs/InlineResponse20057Result.md)
 - [InlineResponse20058](docs/InlineResponse20058.md)
 - [InlineResponse20059](docs/InlineResponse20059.md)
 - [InlineResponse20059Result](docs/InlineResponse20059Result.md)
 - [InlineResponse2005Result](docs/InlineResponse2005Result.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse20060](docs/InlineResponse20060.md)
 - [InlineResponse20060Result](docs/InlineResponse20060Result.md)
 - [InlineResponse20061](docs/InlineResponse20061.md)
 - [InlineResponse20061Result](docs/InlineResponse20061Result.md)
 - [InlineResponse20062](docs/InlineResponse20062.md)
 - [InlineResponse20063](docs/InlineResponse20063.md)
 - [InlineResponse20063Result](docs/InlineResponse20063Result.md)
 - [InlineResponse20064](docs/InlineResponse20064.md)
 - [InlineResponse20064Result](docs/InlineResponse20064Result.md)
 - [InlineResponse20065](docs/InlineResponse20065.md)
 - [InlineResponse20065Result](docs/InlineResponse20065Result.md)
 - [InlineResponse20066](docs/InlineResponse20066.md)
 - [InlineResponse20066Result](docs/InlineResponse20066Result.md)
 - [InlineResponse20067](docs/InlineResponse20067.md)
 - [InlineResponse20068](docs/InlineResponse20068.md)
 - [InlineResponse20068Result](docs/InlineResponse20068Result.md)
 - [InlineResponse20069](docs/InlineResponse20069.md)
 - [InlineResponse20069Result](docs/InlineResponse20069Result.md)
 - [InlineResponse2006Result](docs/InlineResponse2006Result.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse20070](docs/InlineResponse20070.md)
 - [InlineResponse20070Result](docs/InlineResponse20070Result.md)
 - [InlineResponse20071](docs/InlineResponse20071.md)
 - [InlineResponse20071Result](docs/InlineResponse20071Result.md)
 - [InlineResponse20072](docs/InlineResponse20072.md)
 - [InlineResponse20072Result](docs/InlineResponse20072Result.md)
 - [InlineResponse20073](docs/InlineResponse20073.md)
 - [InlineResponse20073Result](docs/InlineResponse20073Result.md)
 - [InlineResponse20074](docs/InlineResponse20074.md)
 - [InlineResponse20074Result](docs/InlineResponse20074Result.md)
 - [InlineResponse20075](docs/InlineResponse20075.md)
 - [InlineResponse20075Result](docs/InlineResponse20075Result.md)
 - [InlineResponse20076](docs/InlineResponse20076.md)
 - [InlineResponse20076Result](docs/InlineResponse20076Result.md)
 - [InlineResponse20077](docs/InlineResponse20077.md)
 - [InlineResponse20078](docs/InlineResponse20078.md)
 - [InlineResponse20078Result](docs/InlineResponse20078Result.md)
 - [InlineResponse20079](docs/InlineResponse20079.md)
 - [InlineResponse20079Result](docs/InlineResponse20079Result.md)
 - [InlineResponse2007Result](docs/InlineResponse2007Result.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse20080](docs/InlineResponse20080.md)
 - [InlineResponse20080Result](docs/InlineResponse20080Result.md)
 - [InlineResponse20081](docs/InlineResponse20081.md)
 - [InlineResponse20081Result](docs/InlineResponse20081Result.md)
 - [InlineResponse20082](docs/InlineResponse20082.md)
 - [InlineResponse20082Result](docs/InlineResponse20082Result.md)
 - [InlineResponse20083](docs/InlineResponse20083.md)
 - [InlineResponse20083Result](docs/InlineResponse20083Result.md)
 - [InlineResponse20084](docs/InlineResponse20084.md)
 - [InlineResponse20084Result](docs/InlineResponse20084Result.md)
 - [InlineResponse20085](docs/InlineResponse20085.md)
 - [InlineResponse20085Result](docs/InlineResponse20085Result.md)
 - [InlineResponse20086](docs/InlineResponse20086.md)
 - [InlineResponse20087](docs/InlineResponse20087.md)
 - [InlineResponse20087Result](docs/InlineResponse20087Result.md)
 - [InlineResponse20088](docs/InlineResponse20088.md)
 - [InlineResponse20088Result](docs/InlineResponse20088Result.md)
 - [InlineResponse2008Result](docs/InlineResponse2008Result.md)
 - [InlineResponse2008ResultSupportedCarts](docs/InlineResponse2008ResultSupportedCarts.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009Result](docs/InlineResponse2009Result.md)
 - [InlineResponse200Result](docs/InlineResponse200Result.md)
 - [Language](docs/Language.md)
 - [ModelResponseCartCatalogPriceRulesList](docs/ModelResponseCartCatalogPriceRulesList.md)
 - [ModelResponseCartCouponList](docs/ModelResponseCartCouponList.md)
 - [ModelResponseCartGiftCardList](docs/ModelResponseCartGiftCardList.md)
 - [ModelResponseCartMetaDataList](docs/ModelResponseCartMetaDataList.md)
 - [ModelResponseCartScriptList](docs/ModelResponseCartScriptList.md)
 - [ModelResponseCategoryList](docs/ModelResponseCategoryList.md)
 - [ModelResponseCustomerAttributeList](docs/ModelResponseCustomerAttributeList.md)
 - [ModelResponseCustomerGroupList](docs/ModelResponseCustomerGroupList.md)
 - [ModelResponseCustomerList](docs/ModelResponseCustomerList.md)
 - [ModelResponseOrderAbandonedList](docs/ModelResponseOrderAbandonedList.md)
 - [ModelResponseOrderList](docs/ModelResponseOrderList.md)
 - [ModelResponseOrderShipmentList](docs/ModelResponseOrderShipmentList.md)
 - [ModelResponseProductAttributeList](docs/ModelResponseProductAttributeList.md)
 - [ModelResponseProductChildItemList](docs/ModelResponseProductChildItemList.md)
 - [ModelResponseProductList](docs/ModelResponseProductList.md)
 - [Order](docs/Order.md)
 - [OrderAbandoned](docs/OrderAbandoned.md)
 - [OrderAdd](docs/OrderAdd.md)
 - [OrderAddNoteAttributes](docs/OrderAddNoteAttributes.md)
 - [OrderAddOrderItem](docs/OrderAddOrderItem.md)
 - [OrderAddOrderItemOption](docs/OrderAddOrderItemOption.md)
 - [OrderAddOrderItemProperty](docs/OrderAddOrderItemProperty.md)
 - [OrderItem](docs/OrderItem.md)
 - [OrderItemOption](docs/OrderItemOption.md)
 - [OrderPaymentMethod](docs/OrderPaymentMethod.md)
 - [OrderRefund](docs/OrderRefund.md)
 - [OrderRefundAdd](docs/OrderRefundAdd.md)
 - [OrderRefundAddItems](docs/OrderRefundAddItems.md)
 - [OrderShipmentAdd](docs/OrderShipmentAdd.md)
 - [OrderShipmentAddItems](docs/OrderShipmentAddItems.md)
 - [OrderShipmentAddTrackingNumbers](docs/OrderShipmentAddTrackingNumbers.md)
 - [OrderShipmentTrackingAdd](docs/OrderShipmentTrackingAdd.md)
 - [OrderShipmentUpdate](docs/OrderShipmentUpdate.md)
 - [OrderShippingMethod](docs/OrderShippingMethod.md)
 - [OrderStatus](docs/OrderStatus.md)
 - [OrderStatusHistoryItem](docs/OrderStatusHistoryItem.md)
 - [OrderStatusRefund](docs/OrderStatusRefund.md)
 - [OrderStatusRefundItem](docs/OrderStatusRefundItem.md)
 - [OrderTotal](docs/OrderTotal.md)
 - [OrderTotals](docs/OrderTotals.md)
 - [OrderTotalsNewDiscount](docs/OrderTotalsNewDiscount.md)
 - [Pagination](docs/Pagination.md)
 - [Plugin](docs/Plugin.md)
 - [PluginList](docs/PluginList.md)
 - [Product](docs/Product.md)
 - [ProductAdd](docs/ProductAdd.md)
 - [ProductAddGroupPrices](docs/ProductAddGroupPrices.md)
 - [ProductAddSellerProfiles](docs/ProductAddSellerProfiles.md)
 - [ProductAddShippingDetails](docs/ProductAddShippingDetails.md)
 - [ProductAddTierPrices](docs/ProductAddTierPrices.md)
 - [ProductAdvancedPrice](docs/ProductAdvancedPrice.md)
 - [ProductAttribute](docs/ProductAttribute.md)
 - [ProductGroupPrice](docs/ProductGroupPrice.md)
 - [ProductInventory](docs/ProductInventory.md)
 - [ProductOption](docs/ProductOption.md)
 - [ProductOptionItem](docs/ProductOptionItem.md)
 - [ProductPriceAdd](docs/ProductPriceAdd.md)
 - [ProductPriceUpdate](docs/ProductPriceUpdate.md)
 - [ProductPriceUpdateGroupPrices](docs/ProductPriceUpdateGroupPrices.md)
 - [ProductReview](docs/ProductReview.md)
 - [ProductReviewRating](docs/ProductReviewRating.md)
 - [ProductTaxAdd](docs/ProductTaxAdd.md)
 - [ProductTaxAddTaxRates](docs/ProductTaxAddTaxRates.md)
 - [ProductTierPrice](docs/ProductTierPrice.md)
 - [ProductVariantAdd](docs/ProductVariantAdd.md)
 - [ProductVariantAddAttributes](docs/ProductVariantAddAttributes.md)
 - [ProductVariantPriceAdd](docs/ProductVariantPriceAdd.md)
 - [ProductVariantPriceUpdate](docs/ProductVariantPriceUpdate.md)
 - [ResponseCartCatalogPriceRulesListResult](docs/ResponseCartCatalogPriceRulesListResult.md)
 - [ResponseCartCouponListResult](docs/ResponseCartCouponListResult.md)
 - [ResponseCartGiftcardListResult](docs/ResponseCartGiftcardListResult.md)
 - [ResponseCartMetaDataListResult](docs/ResponseCartMetaDataListResult.md)
 - [ResponseCartScriptListResult](docs/ResponseCartScriptListResult.md)
 - [ResponseCategoryListResult](docs/ResponseCategoryListResult.md)
 - [ResponseCustomerAttributeListResult](docs/ResponseCustomerAttributeListResult.md)
 - [ResponseCustomerGroupListResult](docs/ResponseCustomerGroupListResult.md)
 - [ResponseCustomerListResult](docs/ResponseCustomerListResult.md)
 - [ResponseOrderAbandonedListResult](docs/ResponseOrderAbandonedListResult.md)
 - [ResponseOrderListResult](docs/ResponseOrderListResult.md)
 - [ResponseOrderShipmentListResult](docs/ResponseOrderShipmentListResult.md)
 - [ResponseProductAttributeListResult](docs/ResponseProductAttributeListResult.md)
 - [ResponseProductChildItemListResult](docs/ResponseProductChildItemListResult.md)
 - [ResponseProductListResult](docs/ResponseProductListResult.md)
 - [Script](docs/Script.md)
 - [Shipment](docs/Shipment.md)
 - [ShipmentItems](docs/ShipmentItems.md)
 - [ShipmentTrackingNumber](docs/ShipmentTrackingNumber.md)
 - [SpecialPrice](docs/SpecialPrice.md)
 - [State](docs/State.md)
 - [StoreAttribute](docs/StoreAttribute.md)
 - [StoreAttributeGroup](docs/StoreAttributeGroup.md)
 - [Subscriber](docs/Subscriber.md)
 - [TaxClass](docs/TaxClass.md)
 - [TaxClassRate](docs/TaxClassRate.md)
 - [Webhook](docs/Webhook.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

## store_key

- **Type**: API key
- **API key parameter name**: store_key
- **Location**: URL query string


## Author

contact@api2cart.com

