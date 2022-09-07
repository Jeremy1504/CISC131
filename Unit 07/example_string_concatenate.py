s1 = 'Hello'
s2 = 'World'
s3 = s1 + s2 + s1

print(s1 + s2)
print(s1 + ' ' + s2)
print(s3)

print()

s1 = 'Hello'
s2 = 'World'
for i in range(5):
    s1 += s2
print(s1)
