## Python web application using Azure AD to authenticate against backend

Python web app using delegated permissions from signed-in user or application permissions to authenticate to backend. Backend can be Azure Function or SQLDB. Detailed documentation can be found in my blogs:

- In case you want to authenticate against a SQLDB as backend, see https://towardsdatascience.com/how-to-secure-python-flask-web-apis-with-azure-ad-14b46b8abf22
- In case you want to authenticate against an Azure Function as backend, see https://towardsdatascience.com/how-to-use-the-microsoft-identity-platform-in-your-azure-web-app-fcb3839a44e5

This sample is derived from https://github.com/Azure-Samples/ms-identity-python-webapp, in which user data is retrieved from Microsoft Graph.
