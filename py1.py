from abc import ABCMeta, abstractmethod

l=['a','b','c']
print(l);
print(l[0])
l.append("d");
print(l)
l.pop();

print(l);





#commit
ll=[l[i] for i in [2,1,0] ]
#print(next(ll));


m={"a":"b"}
m['c']='d';
m['a']*=2;
print(m);
list=m.keys();

print(list);
for k in list:
  print(k+"---->"+m[k]);

#test exists
flag='d' not in m
print(flag)


meta=(1,2,3,4,5,5,7);



#define class
class User:
  def __init__(self, id, name):
    self.id=id;
    self.name=name;
  def getName(self):
    return self.name;









class Super(metaclass= ABCMeta):
  """抽象超类"""
  @abstractmethod
  def method(self):
    pass

class Sub1(Super):
  pass

class Sub(Super):
  def method(self):
     super().method()


#sub =  Sub1() 运行错误