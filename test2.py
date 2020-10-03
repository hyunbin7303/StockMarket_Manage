import http.client
import json

file_path_real= "./jong.json"

conn = http.client.HTTPConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "7c660e7db2msh6dba68fb0305bc6p1d982cjsn55312d329620"
    }

conn.request("GET", "/stock/v2/get-financials?region=US&symbol=AMRN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
A=data.decode("utf-8")

A3=A.replace("\"","\'")
B=json.loads(A)
print (B)
with open(file_path_real, 'w') as outfile1:
    json.dump(B,outfile1,indent=4)


