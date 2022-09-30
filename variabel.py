x = input().lower()
y = 'a','i','u','e','o'

for i in x:
    if i in y:
        x = x.replace(i,'')

print(x)