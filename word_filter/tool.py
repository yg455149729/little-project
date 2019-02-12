# -*- coding: utf-8 -*-
def create_dataset():
    data=[["my","school","is","fucked"],["my","girl","is","pretty"],
          ["his","book","bullshit"],["shit","his","mama"],["his","words","are",
          "disgusting"],["it","don't","worth","it"]]
    
    classes=[1,0,1,1,0,0]
    return data,classes

def create_directory(dataset):
    directory=set([])
    for i in dataset:
        temp=set(i)
        directory=directory|temp
    return list(directory)
def ratio_front(num,sum):
    return num*1.0/sum
def ratio_back(front_ratio,class_ratio,ratio):
    back_ratio=front_ratio*class_ratio*1.0/ratio
    return back_ratio
def Sum(c):
    sum=0
    for i in c:
        sum+=i
    return sum
def sumoflist(c1,c2):
    c3=[]
    for i in range(len(c1)):
        tmp=c1[i]+c2[i]
        c3.append(tmp)
    return c3
def practice():
    dataset,classes=create_dataset()
    directory=create_directory(dataset)
    length=len(directory)
    #c1,c2 represents the appearance of word in directory in both two class:1 or 2
    c1=[0]*length
    c2=[0]*length
    c1_num=0
    c2_num=0
    pc1=0.0
    pc2=0.0
    for i in range(len(dataset)):
        temp=[0]*length
        words=dataset[i]
        for j in words:
            temp[directory.index(j)]=1# make the word to vector
        
        if(classes[i]==1):
            c1=sumoflist(c1,temp)
            c1_num+=1;
        else:
            c2=sumoflist(c2,temp)
            c2_num+=1
    pc1=c1_num*1.0/(c1_num+c2_num)# the ratio of c1,c2 in whole dataset
    pc2=1.0-pc1
    c1_sum=Sum(c1)
    c2_sum=Sum(c2)
    sum=c1_sum+c2_sum
    pc1_back=[0.0]*len(directory)
    pc2_back=[0.0]*len(directory)
    print(c1)
    print(c2)
    print(len(directory))
    for i in range(len(directory)):
        front_ratio_1=c1[i]*1.0/c1_sum
        front_ratio_2=c2[i]*1.0/c2_sum
        ratio=(c1[i]+c2[i])*1.0/sum
        print(front_ratio_1,pc1,ratio)
        pc1_back[i]=ratio_back(front_ratio_1,pc1,ratio)
        pc2_back[i]=ratio_back(front_ratio_2,pc2,ratio)
    print(pc1_back,pc2_back)

practice()

















