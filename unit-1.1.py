bicycles = ['trek','cannondale','redline','specialized']
print(len(bicycles))

print(bicycles[2])

bicycles.append('abc')
bicycles.insert(0, 'f')
del bicycles[1]
print(bicycles)


cars = ["byd","changcheng","xiaopeng","jili"]


print(sum(list(range(2,6))))

print("max:"+min(cars))

print(sorted(cars))
print(cars)

cars.sort()

print(cars)

cars.sort(reverse=True)

print(cars)

for (car) in cars:
  print("this is my car:" + car)
  print("ssdf")


squares = [value for value in range(1,11)]
print(squares)

print(cars[1:3])

if "byd" in cars:
  print(True)


s = "abce"

i = 0
while(i<len(s)):
  if(i%2 == 0):
    print(s[i].upper())
  else:
    print(s[i])
  i = i+1

for i in range(0, len(s)):
  print(s[i])


employmentStatus = {id:23, 'name':'active'}
employee = {'employeeName' : "tony", 'id': 123, 'employmentStatusList': []}
employee['employmentStatusList'].insert(0, employmentStatus)
print(employee)

2**8


