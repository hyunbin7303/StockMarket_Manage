import json
# with open('data.json') as json_file: 
#     data = json.load(json_file) 
  
#     # Print the type of data variable 
#     print("Type:", type(data)) 
  
#     # Print the data of dictionary 
#     print("\nPeople1:", data['people1']) 
#     print("\nPeople2:", data['people2'])
    


with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile) # Reading the file
    print("Read successful")
    jsonfile.close()

print(data['username'])
print(data['tickers'][0]['symbol'])    

# https://www.datacamp.com/community/tutorials/reading-writing-files-python
# https://www.programiz.com/python-programming/generator