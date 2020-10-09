
import abc
import requests
import json

response = requests.get("https://samples.agromonitoring.com/agro/1.0/image/search?polyid=5aaa8052cbbbb5000b73ff66&start=1500336000&end=1508976000&appid=b1b15e88fa797225412429c1c50c122a1")
JsonValues = response.json()
print(response.status_code)
print(type(response))
print(response.headers)
print(response.headers['content-type'])
print('-------------')

print("Agri API Testing 2 ")
response2 = requests.get("http://api.agromonitoring.com/agro/1.0/polygons?appid=cdfacf765daf39ecc17a56f5948c49d1")
JsonValues = response2.json()
print(JsonValues)

print("Agri API Testing 3 ")
response3 = requests.get("https://samples.agromonitoring.com/stats/1.0/02359768a00/5ac22f004b1ae4000b5b97cf?appid=b1b15e88fa797225412429c1c50c122a1")
JsonValues = response3.json()
print(JsonValues)


