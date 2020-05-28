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

# Add
SCOPE = ["https://database.windows.net//.default"]

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session

SQL_SERVER = "<<Enter_logical_SQL_server_URL_here>>"
DATABASE = "<<Enter_SQL_database_name_here>>" # Database name