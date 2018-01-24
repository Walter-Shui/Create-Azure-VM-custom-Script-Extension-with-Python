from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

# Tenant ID for your Azure Subscription
TENANT_ID = ''

# Your Service Principal App ID
CLIENT = '5eea6528-b77b-4558-9425-33995e5b3dbd'

# Your Service Principal Password
KEY = ''

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

subscription_id = '3b4d41fa-e91d-4bc7-bc11-13d221b3b77d'


compute_client = ComputeManagementClient(credentials, subscription_id)

GROUP_NAME = 'shuicli'
name = 'shui'
ext_type_name = 'CustomScriptForLinux'
ext_name = 'shuitest'
params_create = {
    'location': 'eastus',
    'publisher': 'Microsoft.OSTCExtensions',
    'virtual_machine_extension_type': ext_type_name,
    'type_handler_version': '1.0',
    'auto_upgrade_minor_version': True,
    'settings': {
        'fileUris': ["https://shuilinuxdiag336.blob.core.windows.net/customscriptfiles/install_nginx_ubuntu.sh"],
        'commandToExecute': "sh install_nginx_ubuntu.sh"
    }, 
    'protected_settings' : {
        'storageAccountName': 'shuilinuxdiag336',
        'storageAccountKey': '6GenPqSkzXfQiuOBjRfoKnRCaTs+aXpp2mVqn/fXp351YJzjiPtRmeTX8x4YJ3MwG7pfS7PHsWCdmQdoC3tVog=='
	},
}
ext_poller = compute_client.virtual_machine_extensions.create_or_update(
    GROUP_NAME,
    name,
    ext_name,
    params_create,
)
ext = ext_poller.result()
