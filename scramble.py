import math
from collections import Counter
import pandas as pd
import random

def logistic(x0,mu,M,N):
    x = x0
    for i in range(M):
        x = mu * x * (1-x)
    xm = x  

    map = []
    for i in range(N):
        x = mu * x * (1-x)
        map.append(x)  
    return map  

def cubic(x0,r,M,N):
    x = x0
    for i in range(M):
        x = r * x * (1 - pow(x,2))
    xm = x  

    map = []
    for i in range(N):
        x = r * x * (1 - pow(x,2))
        map.append(x) 
    return map

def sine(x0,a,M,N):
    x = x0
    for i in range(M):
        x = 4 / a * math.sin(math.pi * x)
    xm = x  

    map = []
    for i in range(N):
        x = 4 / a * math.sin(math.pi * x)
        map.append(x) 
    return map

class Element:
    def __init__(self,value,num):
        self.value = value
        self.num = num

def sequence(map):
    L = len(map)
    list = []
    for i in range(L):
        list.append(Element(map[i],i)) #初始化数组
    
    for i in range(1,L):
        j = i
        while j>0 and list[j].value < list[j-1].value:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
    return list #进行大小排序

def resequence(list):
    L = len(list)
    elements = []
    for i in range(L):
        elements.append(list[list[i].num])
    return elements #置乱

def map_print(arr):
    list = []
    for i in range(len(arr)):
        list.append(resequence(sequence(arr))[i].num)
    return list #置乱后数组

def LCM(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        a = a * arr[i] // math.gcd(a,arr[i])
    return a

def Times_Count(arr):
    size_count = Counter(arr)
    for num, count in size_count.items():
        print(f"循环 {num} 有 {count} 个")

def cir_count(arr):
    mark = []
    Count = []
    for i in range(len(arr)):
        mark.append(0) #初始化标记数组
    len_count = 0 #长度计数
    num_count = 0 #数量计数
    for i in range(len(arr)):
        len_count = 0
        if mark[i] == 0:
            while mark[i] == 0:
                mark[i] = 1
                i = arr[i]
                len_count += 1
            num_count += 1
            Count.append(len_count)
        else:
            continue
    return Count,num_count

def info(list):
    Count,num = cir_count(list)
    a = LCM(Count)
    print("循环数量",num)
    print("循环长度",Count)
    a = LCM(Count)
    print("阶",a)
    Times_Count(Count)

def Random(min,max):
    x = random.uniform(min,max)
    while x == min or x == max:
        x = random.uniform(min,max)
    return x
    

def Average_logistic():   
    all_data = []
    for n in range(10,200): #N[10,200)
        a = 0
        for j in range(50): #100times
            x0 = Random(0,1)
            mu = Random(3.57,4)
            map = logistic(x0,mu,1000,n)
            list = map_print(map)
            Count,num = cir_count(list)
            t = LCM(Count)
            a += t
        ave = a / 50
        all_data.append({'N':n,'Average':ave})
        
    df = pd.DataFrame(all_data)
    df.to_excel("logistic.xlsx",index=False)

def Average_cubic():   
    all_data = []
    for n in range(10,200): #N[10,200)
        a = 0
        for j in range(50): #100times
            x0 = Random(0,1)
            r = Random(2.5,3)
            map = cubic(x0,r,1000,n)
            list = map_print(map)
            Count,num = cir_count(list)
            t = LCM(Count)
            a += t
        ave = a / 50
        all_data.append({'N':n,'Average':ave})
        
    df = pd.DataFrame(all_data)
    df.to_excel("cubic.xlsx",index=False)

def Average_sine():   
    all_data = []
    for n in range(10,200): #N[10,200)
        a = 0
        for j in range(50): #100times
            x0 = Random(-1,1)
            mu = Random(0,4)
            map = sine(x0,mu,1000,n)
            list = map_print(map)
            Count,num = cir_count(list)
            t = LCM(Count)
            a += t
        ave = a / 50
        all_data.append({'N':n,'Average':ave})
        
    df = pd.DataFrame(all_data)
    df.to_excel("sine.xlsx",index=False)

print("Logistic")
map_logistic = logistic(0.66,3.66,1000,120)
list_logistic = map_print(map_logistic)
info(list_logistic)
#Average_logistic()


print("Cubic")
map_cubic = cubic(0.68,2.83,1000,40)
list_cubic = map_print(map_cubic)
info(list_cubic)
#Average_cubic()

print("Sine")
map_sine = sine(0.31,3.62,1000,40)
list_sine = map_print(map_sine)
info(list_sine)
#Average_sine() #平均阶-N
