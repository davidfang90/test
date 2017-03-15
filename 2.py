import os

class HMM(object):
    def __init__(self):
        b = 3
        self.a = 1
    def train(self, x): 
        return x+self.a


def main():
    x = HMM()
    print(x.a)


    y = x.train(6)
    print(y)

def main1():
    list1=[1,2,3,4,5,6,7,8]
    list2=[]

    del(list1[0])


    print(list1)
    dic1={"a":1,"b":4}
    print(dic1)

    for x in list1:
        y=x+1
        


    for i in range(len(list1)):
        y=list1[i]+1
        list2.append(y)

    print(list2)
        
    
#hello
if __name__ == "__main__":
    main()
