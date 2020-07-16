import os

#CLIENT_SECRET = "3.9oi75AD4K-8Z~1qfE_mnd86VzaeYJC5I" # tenant: bremerov
CLIENT_SECRET = "j..5XAKzfx_V38-m.bDM4l0-a5M46.T_X1" # tenant: MS
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

#AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/e34e55f2-fe0c-43d2-8523-3d6bb35d514c" # tenant: bremerov
#AUTHORITY = "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47" # tenant: MS

#CLIENT_ID = "5ab0e01f-7c18-4713-b3eb-914e7fd120ff" # tenant: bremerov
CLIENT_ID = "b9915f61-1a89-46c3-a31a-cfe1c619e1c5" # tenant: MS

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
# Option 2a. Azure Function 
BACKEND_SETTINGS = {"Type": "AzureFunction", "Connection":{"URL": "https://blog-rolescope-backendapp.azurewebsites.net/api/HttpBackend?code=peMICFGMdwrjuKJM03NA9DmLn2FGmdjn2xYIZhH/AnKfUwa31/SAKw=="}}
# Option 2b. Database 
#BACKEND_SETTINGS = {"Type": "Database", "Connection":{"SQL_SERVER": "test-sqldbauth-sql.database.windows.net", "DATABASE": "test-sqldbauth-db"}}

#
# 3. Permissions:
# 
# Choose how to authenticate to resources. Only one delegated user scope can be defined
# https://docs.microsoft.com/en-us/azure/active-directory/develop/developer-glossary#permissions
#
# Option 3a. Delegated user is used to authenticate to Graph API, MI is then used to authenticate to backend
DELEGATED_PERMISSONS = ["User.Read"]
if BACKEND_SETTINGS.get("Type") == "AzureFunction":
    APPLICATION_PERMISSIONS = [BACKEND_SETTINGS.get("Connection").get("URL").split('.net/')[0] + ".net/.default"]
else:
    APPLICATION_PERMISSIONS = ["https://database.windows.net//.default"]

# Option 3b. Delegated user is used to authenticate to backend, graph API disabled
if BACKEND_SETTINGS.get("Type") == "AzureFunction":
    DELEGATED_PERMISSONS = [BACKEND_SETTINGS.get("Connection").get("URL").split('.net/')[0] + ".net/user_impersonation"]
else:
    DELEGATED_PERMISSONS = ["https://sql.azuresynapse-dogfood.net/user_impersonation"]
APPLICATION_PERMISSIONS = ["disabled"]

#
# 4. AAD_ROLE_CHECK
#
# In case AAD Role check is true, the user claimes in the id token are used to verify if user is allowed to retrieve data
# Notice that user shall also be added to the database as externa user and be granted the correct roles to retrieve data from tables
AAD_ROLE_CHECK = False