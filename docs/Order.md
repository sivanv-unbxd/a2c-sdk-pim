# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**basket_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**customer** | [**BaseCustomer**](BaseCustomer.md) |  | [optional] 
**create_at** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**shipping_address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**billing_address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**payment_method** | [**OrderPaymentMethod**](OrderPaymentMethod.md) |  | [optional] 
**shipping_method** | [**OrderShippingMethod**](OrderShippingMethod.md) |  | [optional] 
**shipping_methods** | [**list[OrderShippingMethod]**](OrderShippingMethod.md) |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**totals** | [**OrderTotals**](OrderTotals.md) |  | [optional] 
**total** | [**OrderTotal**](OrderTotal.md) |  | [optional] 
**discounts** | [**list[OrderTotalsNewDiscount]**](OrderTotalsNewDiscount.md) |  | [optional] 
**order_products** | [**list[OrderItem]**](OrderItem.md) |  | [optional] 
**bundles** | [**list[OrderItem]**](OrderItem.md) |  | [optional] 
**modified_at** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**finished_time** | [**A2CDateTime**](A2CDateTime.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**store_id** | **str** |  | [optional] 
**warehouses_ids** | **list[str]** |  | [optional] 
**refunds** | [**list[OrderRefund]**](OrderRefund.md) |  | [optional] 
**gift_message** | **str** |  | [optional] 
**additional_fields** | **object** |  | [optional] 
**custom_fields** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


