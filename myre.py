
import re


p = re.compile('\d+')
if p.match('x334e'):
    print('ok')

for m in p.findall('x334e'):
    print(m)