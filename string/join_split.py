sequence = ['a', 'b', 'c', ' ', 'a', 'z', 'a']

## Empty Separator ##
aa = ''.join(sequence) # abc aza 
bb = ', '.join(sequence) # a, b, c,  , a, z, a

mixed_data = ["The answer is", 42, "!"]

## Handling Mixed Data Types ##
cc = " ".join(map(str, mixed_data)) # The answer is 42 !

print(cc)



print(aa)
print(type(aa))
print(bb)

bb = aa.split()

print(bb)
