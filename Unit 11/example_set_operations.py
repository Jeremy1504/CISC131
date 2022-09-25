A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
# alternatively, using | operator
print(A|B)

##########################
print()
print(A.intersection(B))
# alternatively, using & operator
print(A & B)

##########################
print()
print(A.difference(B))
# alternatively, using - operator
print(A - B)

##########################
print()
print(A.symmetric_difference(B))
# alternatively, using ^ operator
print(A ^ B)

##########################
print()
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))
# alternatively, using <= operator
print(A <= B)

##########################
print()
print(A.issuperset(B))
# alternatively, using >= operator
print(A >= B)