import random
from statistics import mean,median
from collections import Counter
from numpy import std
from math import pow, sqrt

#генеруэмо тисячу чисел в діапазоні від 0 до 10
list_with_random_numbers = [random.randint(0,100) for i in range(1000)]

def list_min(list_n):
    min_n = list_n[0]
    for n in list_n:
        if min_n>n:
            min_n = n
    return min_n

def list_max(list_n):
    max_n  = list_n[0]
    for n in list_n:
        if max_n<n:
            max_n = n
    return max_n

def list_avg(list_n):
    sum_n=0
    for n in list_n:
        sum_n+=n
    return sum_n/len(list_n)

def list_mid(list_n):
    list_n.sort(reverse=False)
    len_l = len(list_n)
    if len_l%2 :
        return list_n[len_l//2]
    else:
        return list_avg(list_n[len_l//2-1:len_l//2+1])
    

def list_friq(list_n):
    di={key: list_n.count(key) for key in list_n}
    return dict(sorted(di.items(), key = lambda x:x[1],reverse=True))


def list_std (list_n):
    list_avg_n = list_avg(list_n)
    return sqrt((sum([pow((i-list_avg_n),2) for i in list_n])/len(list_n)))

#print(list_with_random_numbers)
print(f" мінімальне та максимальне значення - {list_min(list_with_random_numbers)} , {list_max(list_with_random_numbers)} ") 
print(f" мінімальне та максимальне значення(python) - {sorted(list_with_random_numbers)[0]}, {sorted(list_with_random_numbers, reverse=False)[-1]}")
print(f" середнє значення послідовності - {list_avg(list_with_random_numbers)} ")
print(f" середнє значення послідовності(python) - {mean(list_with_random_numbers)} ")
print(f" медіану послідовності - {list_mid(list_with_random_numbers)} ")
print(f" медіану послідовності(python) - {median(list_with_random_numbers)} ")
print(f" частоту кожної цифри в послідовності - {list_friq(list_with_random_numbers)} ")
print(f" частоту кожної цифри в послідовності(python) - {Counter(list_with_random_numbers)} ")
print(f" середнє квадратичне відхилення - {list_std(list_with_random_numbers)} ")
print(f" середнє квадратичне відхилення(python) - {std(list_with_random_numbers)} ")
