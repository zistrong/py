import time
print(time.process_time())
M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]
          

N=[[2,2,2],[3,3,3],[4,4,4]]

print([M[col][col] for col in range(3)])
print([M[col][col] for col in range(2,-1,-1)])
print([M[1][col] for col in range(3)])
print([M[col][1] for col in range(3)])
print([[M[1][col] ,M[col][1], M[1][col] + M[col][1]] for col in range(3)])




def sequeue(n):
    for i in range(n):
        print('生成器'+str(i))
        yield i**2

a = sequeue(4)

gen = list(M[col][1] for col in range(3)) #生成器
print(gen)


print(all(a))

