import json
import requests
print("This API call is a part of the response of the Satellite Imagery Search API. It is available only for NDVI and EVI indices.")
r = requests.get('https://samples.agromonitoring.com/stats/1.0/02359768a00/5ac22f004b1ae4000b5b97cf?appid=b1b15e88fa797225412429c1c50c122a1')
print(r.text)
data = r.json()
print(data)

print("------------------------------------------------------------")
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1


top_users = sorted(todos_by_user.items(),
                    key=lambda x: x[1], reverse=True)
max_complete=top_users[0][1]
users = []
for user,num_complete in top_users:
    if num_complete< max_complete:
        break
    users.append(str(user))
max_users = " and ".join(users)
