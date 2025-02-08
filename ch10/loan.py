import re
with open('ch10/loan.txt', encoding='utf-8') as  file:
    sum = 0
    for line in file:
        if '还款' in line or '本息合' in line:
            sum += float(re.split(r'\s+', line)[4])
            print(re.split(r'\s+', line)[4])
    print()
    print(sum)