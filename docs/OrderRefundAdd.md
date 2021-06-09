# OrderRefundAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Defines the order for which the refund will be created. | [optional] 
**items** | [**list[OrderRefundAddItems]**](OrderRefundAddItems.md) | Defines items in the order that will be refunded | [optional] 
**total_price** | **float** | Defines order refund amount. | [optional] 
**shipping_price** | **float** | Defines refund shipping amount. | [optional] 
**fee_price** | **float** | Specifies refund&#39;s fee price | [optional] 
**message** | **str** | Refund reason, or some else message which assigned to refund. | [optional] 
**item_restock** | **bool** | Boolean, whether or not to add the line items back to the store inventory. | [optional] [default to False]
**send_notifications** | **bool** | Send notifications to customer after refund was created | [optional] [default to False]
**_date** | **str** | Specifies an order creation date in format Y-m-d H:i:s | [optional] 
**is_online** | **bool** | Indicates whether refund type is online | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


