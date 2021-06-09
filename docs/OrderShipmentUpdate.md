# OrderShipmentUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Store Id | [optional] 
**shipment_id** | **str** | Shipment id indicates the number of delivery | 
**order_id** | **str** | Defines the order that will be updated | [optional] 
**tracking_numbers** | [**list[OrderShipmentAddTrackingNumbers]**](OrderShipmentAddTrackingNumbers.md) | Defines shipment&#39;s tracking numbers that have to be added&lt;/br&gt; How set tracking numbers to appropriate carrier:&lt;ul&gt;&lt;li&gt;tracking_numbers[]&#x3D;a2c.demo1,a2c.demo2 - set default carrier&lt;/li&gt;&lt;li&gt;tracking_numbers[&lt;b&gt;carrier_id&lt;/b&gt;]&#x3D;a2c.demo - set appropriate carrier&lt;/li&gt;&lt;/ul&gt;To get the list of carriers IDs that are available in your store, use the &lt;a href &#x3D; \&quot;http://docs.api2cart.com/cart-info\&quot;&gt;cart.info&lt;/a &gt; method | [optional] 
**replace** | **bool** | Allows rewrite tracking numbers | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


