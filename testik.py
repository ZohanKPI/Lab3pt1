# file for test work in json
# scheme for json 
import json
with open('Task1.json') as f:
    data = json.load(f)
n = input("Enter your ticket number : ")
if n not in data['numbers']:
    print("No ticket available")
else:
    pass
info = data['ticket_number1']
print("Your number is: ", info)