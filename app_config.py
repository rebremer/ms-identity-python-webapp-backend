import os

CLIENT_SECRET = "<<Enter_the_Client_Secret_Here>>" # Our Quickstart uses this placeholder
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

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session

#
# New settings compared to original ms-identity-python-webapp to access the database
#
# 1. DATABASE_AUTHENTICATION
#
# Option 1a. AAD_USER_PASSTHROUGH
#
# In case DATABASE_AUTHENTICATION = "AAD_USER_PASSTHROUGH", the user bearer token is used to authenticate to the database.
# SCOPE https://database.windows.net//.default is required, see below. Caution: this scope likely requirems admin consent
DATABASE_AUTHENTICATION = "AAD_USER_PASSTHROUGH"
SCOPE = ["https://database.windows.net//.default"]
#
# Option 1b. AAD_APPLICATION_MI
#
# In case DATABASE_AUTHENTICATION = "AAD_APPLICATION_MI", the MI of the application is used to create bearer token and to authenticate to the database.
# SCOPE can be empty, no admin consent requirement
#DATABASE_AUTHENTICATION = "AAD_APPLICATION_MI"
#SCOPE = []

#
# 2. AAD_ROLE_CHECK
#
# In case AAD Role check is true, the user claimes in the id token are used to verify if user is allowed to retrieve data
# Notice that user shall also be added to the database as externa user and be granted the correct roles to retrieve data from tables
AAD_ROLE_CHECK = False
# Do no change settings below, also when role check is set false
ROLES_CONFIG = {"customer": {"role": "read_customer", "query": "SELECT top 10 * FROM SalesLT.Customer"}, "product": {"role": "read_product", "query": "SELECT top 10 * FROM SalesLT.Product"}}

#
# 3. DATABASE SETTINGS
#
SQL_SERVER = "<<Enter_logical_SQL_server_URL_here>>" # Logical DB server name
DATABASE = "<<Enter_SQL_database_name_here>>"