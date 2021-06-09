# ProductVariantAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Defines product&#39;s id where the variant has to be added | [optional] 
**name** | **str** | Defines variant&#39;s name that has to be added | [optional] 
**model** | **str** | Specifies variant&#39;s model that has to be added | 
**sku** | **str** | Defines variant&#39;s sku that has to be added | [optional] 
**barcode** | **str** | A barcode is a unique code composed of numbers used as a product identifier. | [optional] 
**price** | **float** | Defines new product&#39;s variant price | [optional] 
**cost_price** | **float** | Defines new product&#39;s cost price | [optional] 
**attributes** | [**list[ProductVariantAddAttributes]**](ProductVariantAddAttributes.md) | Defines variant&#39;s attributes list | [optional] 
**description** | **str** | Specifies variant&#39;s description | [optional] 
**special_price** | **float** | Specifies variant&#39;s model that has to be added | [optional] 
**sprice_create** | **str** | Defines the date of special price creation | [optional] 
**sprice_modified** | **str** | Defines the date of special price modification | [optional] 
**sprice_expire** | **str** | Defines the term of special price offer duration | [optional] 
**available_for_view** | **bool** | Specifies the set of visible/invisible product&#39;s variants for users | [optional] [default to True]
**available_for_sale** | **bool** | Specifies the set of visible/invisible product&#39;s variants for sale | [optional] [default to True]
**weight** | **float** | Weight | [optional] 
**weight_unit** | **str** | Weight Unit | [optional] 
**short_description** | **str** | Defines short description | [optional] 
**warehouse_id** | **str** | This parameter is used for selecting a warehouse where you need to set/modify a product quantity. | [optional] 
**quantity** | **float** | Defines product variant&#39;s quantity that has to be added | [optional] 
**created_at** | **str** | Defines the date of entity creation | [optional] 
**manufacturer** | **str** | Specifies the product variant&#39;s manufacturer | [optional] 
**tax_class_id** | **int** | Defines tax classes where entity has to be added | [optional] 
**meta_title** | **str** | Defines unique meta title for each entity | [optional] 
**meta_keywords** | **str** | Defines unique meta keywords for each entity | [optional] 
**meta_description** | **str** | Defines unique meta description of a entity | [optional] 
**url** | **str** | Defines unique product variant&#39;s URL | [optional] 
**store_id** | **str** | Add variants specified by store id | [optional] 
**lang_id** | **str** | Language id | [optional] 
**clear_cache** | **bool** | Is cache clear required | [optional] [default to True]
**taxable** | **bool** | Specifies whether a tax is charged | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


