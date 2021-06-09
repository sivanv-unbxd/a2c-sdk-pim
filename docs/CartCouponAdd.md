# CartCouponAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Store Id | [optional] 
**code** | **str** | Coupon code | 
**name** | **str** | Coupon name | [optional] 
**codes** | **list[str]** | Entity codes | [optional] 
**action_type** | **str** | Coupon discount type | 
**action_apply_to** | **str** | Defines where discount should be applied | 
**action_scope** | **str** | Specify how discount should be applied. If scope&#x3D;matching_items, then discount will be applied to each of the items that match action conditions. Scope order means that discount will be applied once. | 
**action_amount** | **float** | Defines the discount amount value. | 
**date_start** | **str** | Defines when discount code will be available. | [optional] [default to 'now']
**date_end** | **str** | Defines when discount code will be expired. | [optional] 
**usage_limit** | **int** | Usage limit for coupon. | [optional] 
**usage_limit_per_customer** | **int** | Usage limit per customer. | [optional] 
**action_condition_entity** | **str** | Defines entity for action condition. | [optional] 
**action_condition_key** | **str** | Defines entity attribute code for action condition. | [optional] 
**action_condition_operator** | **str** | Defines condition operator. | [optional] 
**action_condition_value** | **str** | Defines condition attribute value/s. Can be comma separated string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


