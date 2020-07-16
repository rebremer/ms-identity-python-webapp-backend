import os

CLIENT_SECRET = "<<Enter_the_Client_Secret_Here>>"
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

#AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/<<Enter_the_Tenant_ID_Here>>"


CLIENT_ID = "<<Enter_the_Application_Id_here>>"

REDIRECT_PATH = "/getAToken"  # It will be used to form an absolute URL
# And that absolute URL must match your app's redirect_uri set in AAD

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session

GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0/me'  # This resource requires no admin consent

#
# New settings compared to original ms-identity-python-webapp to access the database
#
# 1. Usage of deamon or user
#
DAEMON_ENABLED = False
#

# 2. Type of BACKEND
#
# Option 2a. Database 
BACKEND_SETTINGS = {"Type": "Database", "Connection":{"SQL_SERVER": "<<Enter_logical_SQL_server_URL_here>>.database.windows.net", "DATABASE": "<<Enter_SQL_database_name_here>>"}}
# Option 2b. Azure Function 
#BACKEND_SETTINGS = {"Type": "AzureFunction", "Connection":{"URL": "https://<<your Azure Function>>.azurewebsites.net/api/HttpBackend?code=<<your secret>>"}}

#
# 3. Permissions:
# 
# Choose how to authenticate to resources. Only one delegated user scope can be defined
# https://docs.microsoft.com/en-us/azure/active-directory/develop/developer-glossary#permissions
#
# Option 3a. Delegated user is used to authenticate to Graph API, MI is then used to authenticate to backend
# Backend can either be database (2a) or Azure Function (2b)
DELEGATED_PERMISSONS = ["User.Read"]
if BACKEND_SETTINGS.get("Type") == "AzureFunction":
    APPLICATION_PERMISSIONS = [BACKEND_SETTINGS.get("Connection").get("URL").split('.net/')[0] + ".net/.default"]
else:
    APPLICATION_PERMISSIONS = ["https://database.windows.net//.default"]

# Option 3b. Delegated user is used to authenticate to backend, graph API disabled
# Backend can either be database (2a) or Azure Function (2b)
#if BACKEND_SETTINGS.get("Type") == "AzureFunction":
#    DELEGATED_PERMISSONS = [BACKEND_SETTINGS.get("Connection").get("URL").split('.net/')[0] + ".net/user_impersonation"]
#else:
#    DELEGATED_PERMISSONS = ["https://sql.azuresynapse-dogfood.net/user_impersonation"]
#APPLICATION_PERMISSIONS = ["disabled"]

#
# 4. AAD_ROLE_CHECK
#
# In case AAD Role check is true, the user claimes in the id token are used to verify if user is allowed to retrieve data
# Notice that user shall also be added to the database as externa user and be granted the correct roles to retrieve data from tables
AAD_ROLE_CHECK = False