import logging

import azure.functions as func
from jose import jwt

import pyodbc
import struct

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')

    auth = str(req.headers.get("Authorization", None))
    parts = auth.split()
    payload = parts[1]
    unverified_header = jwt.get_unverified_claims(payload)

    output = "appid: " + str(unverified_header.get("appid")) + ", "
    output += "roles in backend: " + str(unverified_header.get("roles")) + ", "
    output += "name: " + str(unverified_header.get("name")) + ", "
    output += "scp: " + str(unverified_header.get("scp")) + ", "
    output += "all: " + str(unverified_header)

    output.replace("\\u0027","")
    output.replace("'","")
    
    return func.HttpResponse(f"Table {name}, Token properties: {output}. ")

    #accessToken = bytes(payload, 'utf-8')
    #exptoken = b""
    #for i in accessToken:
    #    exptoken += bytes({i})
    #    exptoken += bytes(1)
    #tokenstruct = struct.pack("=i", len(exptoken)) + exptoken

    #server = "test-sqldbauth-sql.database.windows.net"
    #database = "test-sqldbauth-db"
    #connstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database
    #tokenstruct = struct.pack("=i", len(exptoken)) + exptoken
    #conn = pyodbc.connect(connstr, attrs_before = { 1256:tokenstruct })
    
    #cursor = conn.cursor()
    #cursor.execute("SELECT top 10 * FROM SalesLT.Customer")
    #row = cursor.fetchall()
    #return row