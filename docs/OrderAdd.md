# OrderAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Defines order&#39;s id | [optional] 
**order_id** | **str** | Defines the order id if it is supported by the cart | [optional] 
**store_id** | **str** | Defines store id where the order should be assigned | [optional] 
**channel_id** | **str** | Channel ID | [optional] 
**order_status** | **str** | Defines order status. | 
**send_notifications** | **bool** | Send notifications to customer after order was created | [optional] [default to False]
**send_admin_notifications** | **bool** | Notify admin when new order was created. | [optional] [default to False]
**customer_email** | **str** | Defines the customer specified by email for whom order has to be created | 
**bill_first_name** | **str** | Specifies billing first name | 
**bill_last_name** | **str** | Specifies billing last name | 
**bill_address_1** | **str** | Specifies first billing address | 
**bill_city** | **str** | Specifies billing city | 
**bill_postcode** | **str** | Specifies billing postcode | 
**bill_state** | **str** | Specifies billing state code | 
**bill_country** | **str** | Specifies billing country code | 
**shipp_first_name** | **str** | Specifies shipping first name | [optional] 
**shipp_last_name** | **str** | Specifies shipping last name | [optional] 
**shipp_address_1** | **str** | Specifies first shipping address | [optional] 
**shipp_city** | **str** | Specifies shipping city | [optional] 
**shipp_postcode** | **str** | Specifies shipping postcode | [optional] 
**shipp_state** | **str** | Specifies shipping state code | [optional] 
**shipp_country** | **str** | Specifies shipping country code | [optional] 
**total_price** | **float** | Defines order&#39;s total price | [optional] 
**_date** | **str** | Specifies an order creation date in format Y-m-d H:i:s | [optional] 
**order_payment_method** | **str** | Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39; | [optional] 
**transaction_id** | **str** | Payment transaction id | [optional] 
**order_shipping_method** | **str** | Defines order shipping method | [optional] 
**currency** | **str** | Currency code of order | [optional] 
**bill_address_2** | **str** | Specifies second billing address | [optional] 
**bill_company** | **str** | Specifies billing company | [optional] 
**bill_phone** | **str** | Specifies billing phone | [optional] 
**bill_fax** | **str** | Specifies billing fax | [optional] 
**comment** | **str** | Specifies order comment | [optional] 
**admin_comment** | **str** | Specifies admin&#39;s order comment | [optional] 
**admin_private_comment** | **str** | Specifies private admin&#39;s order comment | [optional] 
**customer_first_name** | **str** | Specifies customer&#39;s first name | [optional] 
**customer_last_name** | **str** | Specifies customer’s last name | [optional] 
**customer_birthday** | **str** | Specifies customer’s birthday | [optional] 
**customer_fax** | **str** | Specifies customer’s fax | [optional] 
**customer_phone** | **str** | Specifies customer’s phone | [optional] 
**shipp_address_2** | **str** | Specifies second address line of a shipping street address | [optional] 
**shipp_company** | **str** | Specifies shipping company | [optional] 
**shipp_phone** | **str** | Specifies shipping phone | [optional] 
**shipp_fax** | **str** | Specifies shipping fax | [optional] 
**date_modified** | **str** | Specifies order&#39;s  modification date | [optional] 
**date_finished** | **str** | Specifies order&#39;s  finished date | [optional] 
**subtotal_price** | **float** | Total price of all ordered products multiplied by their number, excluding tax, shipping price and discounts | [optional] 
**tax_price** | **float** | The value of tax cost for order | [optional] 
**shipping_price** | **float** | Specifies order&#39;s shipping price | [optional] 
**shipping_tax** | **float** | Specifies order&#39;s shipping price tax | [optional] 
**discount** | **float** | Specifies order&#39;s discount | [optional] 
**coupon_discount** | **float** | Specifies order&#39;s coupon discount | [optional] 
**gift_certificate_discount** | **float** | Discounts for order with gift certificates | [optional] 
**fulfillment_status** | **str** | Create order with fulfillment status | [optional] 
**financial_status** | **str** | Create order with financial status | [optional] 
**total_paid** | **float** | Defines total paid amount for the order | [optional] 
**external_source** | **str** | Identifying the system used to generate the order | [optional] 
**tags** | **str** | Order tags | [optional] 
**inventory_behaviour** | **str** | The behaviour to use when updating inventory.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Values description:&lt;div style&#x3D;\&quot;margin-left: 2%; padding-top: 2%\&quot;&gt;&lt;div style&#x3D;\&quot;font-size:85%\&quot;&gt;&lt;b&gt;bypass&lt;/b&gt; &#x3D; Do not claim inventory &lt;/br&gt;&lt;/br&gt;&lt;b&gt;decrement_ignoring_policy&lt;/b&gt; &#x3D; Ignore the product&#39;s &lt;/br&gt; inventory policy and claim amounts&lt;/br&gt;&lt;/br&gt;&lt;b&gt;decrement_obeying_policy&lt;/b&gt; &#x3D;  Obey the product&#39;s &lt;/br&gt; inventory policy.&lt;/br&gt;&lt;/br&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt; | [optional] [default to 'bypass']
**create_invoice** | **bool** | Defines whether the invoice is created automatically along with the order | [optional] [default to False]
**note_attributes** | [**list[OrderAddNoteAttributes]**](OrderAddNoteAttributes.md) | Defines note attributes | [optional] 
**total_weight** | **int** | Defines the sum of all line item weights in grams for the order | [optional] 
**clear_cache** | **bool** | Is cache clear required | [optional] [default to True]
**order_item** | [**list[OrderAddOrderItem]**](OrderAddOrderItem.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


