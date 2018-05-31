import json

message = {
    'action': 'auth',
    'login': 'my_login'
}

print(type(message))

# Словарь в json
jmessage = json.dumps(message)
print(type(jmessage))

# Строка в байты
bmessage = jmessage.encode('utf-8')
print(bmessage)
print(type(bmessage))

# Байты в словарь
# Байты в строку
jmessage = bmessage.decode('utf-8')
print(type(jmessage))
# Строка в словарь
message = json.loads(jmessage)
print(type(message))
