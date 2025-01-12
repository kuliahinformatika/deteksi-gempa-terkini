users = {
    'id': 1,
    'name':'Leanne Graham',
    'username': 'Bret',
    'email':'Sincere@april.biz'
}

print(users)
print(users['id'])
print(users['name'])
print(type(users))

print("\nubah dictionary ke json")
import json
result = json.dumps(users)
print(result)
print(type(result))

with open('users.json', 'w') as file:
    json.dump(users, file)#dump tanpa s menghasilkan file