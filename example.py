from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

# Tenant ID for your Azure Subscription
TENANT_ID = ''

# Your Service Principal App ID
CLIENT = ''

# Your Service Principal Password
KEY = ''

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

subscription_id = '3b4d41fa-e91d-4bc7-bc11-13d221b3b77d'

compute_client = ComputeManagementClient(credentials, subscription_id)
def run_script():
<<<<<<< HEAD
	GROUP_NAME = 'shuicli'
=======
        GROUP_NAME = 'shuicli'
>>>>>>> c2bea2a50d10e0f2f451810447a7df1e6689f36f
    vmname = 'shui'
    ext_type_name = 'CustomScriptForLinux'
    ext_name = 'varun-script-test'
    params_create = {
        'location':'centralindia',
        'publisher': 'Microsoft.OSTCExtensions',
        'virtual_machine_extension_type': ext_type_name,
        'type_handler_version': '1.5',
        'auto_upgrade_minor_version': True,
        'settings':
        {
            'fileUris': ["https://s3.ap-south-1.amazonaws.com/mybucketprog/custom_script.sh"],
            'commandToExecute': "sh custom_script.sh"
        }
    }
    ext_poller = compute_client.virtual_machine_extensions.create_or_update( GROUP_NAME, vmname,ext_name,params_create )
run_script
