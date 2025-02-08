
import re
import itertools

p = re.compile('\d+')
if p.match('x334e'):
    print('ok')

for m in p.findall('x334e'):
    print(m)



counter = itertools.count(1) 

print(counter)
print(next(counter))

print(next(counter))
print(next(counter))