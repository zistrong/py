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

data=open('D:\\workspace-ln\\lm\\target\\classes\com\\sinovatech\\unicom\\web\\TWlmLoginController.class','rb');
data

#define class
class User:
  def __init__(self, id, name):
    self.id=id;
    self.name=name;
  def getName(self):
    return self.name;





