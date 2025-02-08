hexcase = False
b64pad = '='
chrsz = 8


def cleanb64str(str):
    str = '' if str == None else str
    length = len(str)
    if len <1:
        return str
    
    trailchar = str[len - 1]
    trailstr = ''
    i = len -1
    while i >= 0 and str[i] == trailchar:
        trailstr = trailstr+str[i]
        i +=1
    return str[0:str.index(trailstr)]

def concat(oldbin:list, newbin:list):
    retval = [0]*(len(oldbin)+len(newbin))
    for i in range(len(oldbin)+len(newbin)):
        if i <len(oldbin):
            retval[i]= oldbin[i]
        else:
            retval[i] = newbin[i - len(oldbin)]
    return retval

def rol(num: int, cnt:int):
    return (num<<cnt) | (num>>(32-cnt))

def safe_add(x: int, y: int):
    lsw = int(x & 0xffff) + int(y & 0xffff)
    msw = (x >> 16) + (y >> 16) + (lsw >> 16)
    return (msw << 16) | (lsw & 0xffff)

def sha1_ft(t:int , b:int , c:int , d:int ):
    if (t < 20):
        return (b & c) | ((~b) & d)
    if (t < 40):
        return b ^ c ^ d
    if (t < 60):
        return (b & c) | (b & d) | (c & d)
    return b ^ c ^ d



print(6 & 4<<4)