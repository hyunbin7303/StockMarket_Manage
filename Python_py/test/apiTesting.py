import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7c660e7db2msh6dba68fb0305bc6p1d982cjsn55312d329620",
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/income-statement", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))