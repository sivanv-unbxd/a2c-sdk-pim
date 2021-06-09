# AccountCartAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** | Store’s identifier which you can get from cart_list method | 
**store_url** | **str** | A web address of a store that you would like to connect to API2Cart | 
**bridge_url** | **str** | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] 
**store_root** | **str** | Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] 
**store_key** | **str** | Set this parameter if bridge is already uploaded to store | [optional] 
**validate_version** | **bool** | Specify if api2cart should validate cart version | [optional] [default to False]
**verify** | **bool** | Enables or disables cart&#39;s verification | [optional] [default to True]
**db_tables_prefix** | **str** | DB tables prefix | [optional] 
**ftp_host** | **str** | FTP connection host | [optional] 
**ftp_user** | **str** | FTP User | [optional] 
**ftp_password** | **str** | FTP Password | [optional] 
**ftp_port** | **int** | FTP Port | [optional] 
**ftp_store_dir** | **str** | FTP Store dir | [optional] 
**_3dcartapi_api_key** | **str** | 3DCart API Key | [optional] 
**amazon_sp_client_id** | **str** | Amazon SP API app client id | 
**amazon_sp_client_secret** | **str** | Amazon SP API app client secret | 
**amazon_sp_aws_user_key_id** | **str** | Amazon AWS user access key ID | 
**amazon_sp_aws_user_secret** | **str** | Amazon AWS user secret access key | 
**amazon_sp_aws_region** | **str** | Amazon AWS Region | 
**amazon_sp_aws_role_arn** | **str** | Amazon AWS Role ARN | 
**amazon_sp_refresh_token** | **str** | Amazon SP API OAuth refresh token | 
**amazon_sp_api_environment** | **str** | Amazon SP API environment | [optional] [default to 'production']
**amazon_access_token** | **str** | MWS Auth Token. Access token authorizing the app to access resources on behalf of a user | [optional] 
**amazon_seller_id** | **str** | Amazon Seller ID (Merchant token) | [optional] 
**amazon_marketplaces_ids** | **str** | Amazon Marketplace IDs comma separated string | [optional] 
**amazon_secret_key** | **str** | Amazon Secret Key | [optional] 
**amazon_access_key_id** | **str** | Amazon Secret Key Id | [optional] 
**aspdotnetstorefront_api_user** | **str** | It&#39;s a AspDotNetStorefront account for which API is available | [optional] 
**aspdotnetstorefront_api_pass** | **str** | AspDotNetStorefront API Password | [optional] 
**bigcommerceapi_admin_account** | **str** | It&#39;s a BigCommerce account for which API is enabled | [optional] 
**bigcommerceapi_api_path** | **str** | BigCommerce API URL | [optional] 
**bigcommerceapi_api_key** | **str** | Bigcommerce API Key | [optional] 
**bigcommerceapi_client_id** | **str** | Client ID of the requesting app | [optional] 
**bigcommerceapi_access_token** | **str** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**bigcommerceapi_context** | **str** | API Path section unique to the store | [optional] 
**demandware_client_id** | **str** | Demandware client id | [optional] 
**demandware_api_password** | **str** | Demandware api password | [optional] 
**demandware_user_name** | **str** | Demandware user name | [optional] 
**demandware_user_password** | **str** | Demandware user password | [optional] 
**demandware_env_type** | **str** | Demandware environment | [optional] [default to 'production']
**ebay_client_id** | **str** | Application ID (AppID). | [optional] 
**ebay_client_secret** | **str** | Shared Secret from eBay application | [optional] 
**ebay_runame** | **str** | The RuName value that eBay assigns to your application. | [optional] 
**ebay_access_token** | **str** | Used to authenticate API requests. | [optional] 
**ebay_refresh_token** | **str** | Used to renew the access token. | [optional] 
**ebay_environment** | **str** | eBay environment | [optional] [default to 'production']
**ebay_site_id** | **int** | eBay global ID | [optional] 
**walmart_client_id** | **str** | Walmart client ID | [optional] 
**walmart_client_secret** | **str** | Walmart client secret | [optional] 
**walmart_environment** | **str** | Walmart environment | [optional] [default to 'production']
**walmart_channel_type** | **str** | Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] 
**ecwid_acess_token** | **str** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**ecwid_store_id** | **str** | Store Id | [optional] 
**lightspeed_api_key** | **str** | LightSpeed api key | [optional] 
**lightspeed_api_secret** | **str** | LightSpeed api secret | [optional] 
**etsy_keystring** | **str** | Etsy keystring | [optional] 
**etsy_shared_secret** | **str** | Etsy shared secret | [optional] 
**etsy_access_token** | **str** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**etsy_token_secret** | **str** | Secret token authorizing the app to access resources on behalf of a user | [optional] 
**neto_api_key** | **str** | Neto API Key | [optional] 
**neto_api_username** | **str** | Neto User Name | [optional] 
**shopify_api_key** | **str** | Shopify API Key | [optional] 
**shopify_api_password** | **str** | Shopify API Password | [optional] 
**shopify_shared_secret** | **str** | Shared secret | [optional] 
**shopify_access_token** | **str** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**shopware_api_key** | **str** | Shopware api key | [optional] 
**shopware_api_secret** | **str** | Shopware client secret access key | [optional] 
**volusion_login** | **str** | It&#39;s a Volusion account for which API is enabled | [optional] 
**volusion_password** | **str** | Volusion API Password | [optional] 
**hybris_client_id** | **str** | Omni Commerce Connector Client ID | [optional] 
**hybris_client_secret** | **str** | Omni Commerce Connector Client Secret | [optional] 
**hybris_username** | **str** | User Name | [optional] 
**hybris_password** | **str** | User password | [optional] 
**hybris_websites** | [**list[AccountCartAddHybrisWebsites]**](AccountCartAddHybrisWebsites.md) | Websites to stores mapping data | [optional] 
**squarespace_api_key** | **str** | Squarespace API Key | [optional] 
**commercehq_api_key** | **str** | CommerceHQ api key | [optional] 
**commercehq_api_password** | **str** | CommerceHQ api password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


