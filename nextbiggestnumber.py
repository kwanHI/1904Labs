"""
@Author: Kwan Limpsangsri
@Date: 2021-02-28
@Script: NextBiggestNumber.py
"""
#!/usr/bin/python3

import sys

def main():
    nextbiggestnumber(sys.argv[1])


def nextbiggestnumber(numstr):
    """
    First Check if Number is Positive or Negative Integer
    """
    print('Input=',numstr)
    if isinstance(numstr,int):
        numstr = str(numstr)

    if numstr[0]=='-':
        print('Only take positive integer number.')
        return -1
    else:
        ret = checkNextMax(numstr)
        print('Next Biggest Number: ',ret)
        return ret
    return -1

class Box:
    def __init__(self):
        self.elements = []
    def push(self, token):
        self.elements.append(token)
        return self
    def pop(self):
        return self.elements.pop() 
    def popNth(self, i):
        return self.elements.pop(i)     
    def peek(self):
        return self.elements[-1]
    def cnt(self):
        return len(self.elements)
    def isEmpty(self):
        return (len(self.elements) == 0)
    def printOut(self):
        return ''.join(self.elements)
    def printLastOut(self):
        ret =''
        for t in range(len(self.elements)-1,-1,-1):
            ret += self.elements[t]   
        return ret
    def allBoxFromLast(self):
        b = Box()
        [b.push(t) for t in range(self.elements.cnt()-1,-1,-1)] 
        return b
 
def checkNextMax(oStr):
    if len(oStr)<2:
        return -1
    box = Box()
    for i in range(len(oStr)-1,0,-1):
        pre = oStr[i-1]
        post = box.push(oStr[i]).peek()
        if pre >= post:
            if i ==1:
                if box.cnt() ==1:
                    return -1
                else:
                    ret = pre+ box.printLastOut()
                    if oStr == ret:
                        return -1
                    else:
                        return int(ret)
            
        else:        
            ret =''
            while ~box.isEmpty(): 
                token = str(box.popNth(0))
                if pre >= token:
                    ret = ret+token
                else: # pre < token:  
                    ret = token + ret+ pre+box.printOut()
                    if i==1:
                        return int(ret)
                    else:
                        return int(oStr[:i-1]+ret)
            return int(ret+pre)

if __name__ == "__main__":
    main()
