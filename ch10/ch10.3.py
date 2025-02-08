import math
import re
S= ['ab','b']
for(offset,item) in enumerate(S):
    print(item, 'appears at offset', offset)

sum = 0
for i in range(1,101):
    sum += i

print(sum)

for (idx, i) in enumerate(range(8,101)):
    print(idx, i)



I = iter(range(10))
print(next(I))
print(next(I))


I = map(lambda i : i**2, [1,-2,3])
print(list(I))
print(list(filter(lambda x : x >= 1, [1,-2,3])))

print(range.__doc__)

regEx = "(\\d+)"
pat = re.compile(regEx)
mat = pat.findall('123ff234gg24')
print(mat)


