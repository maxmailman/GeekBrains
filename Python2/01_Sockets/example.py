# Сети ходят байты

# Строка
s = 'Hello'
print(s)
print(type(s))
print(s[1])

# Строки байт
sb = b'Hello'
print(sb)
print(type(sb))
print(sb[1])

# Кодирование строки
s = 'Hello'
sb = s.encode('utf-8')
print(sb)
