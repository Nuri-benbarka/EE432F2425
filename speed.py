import time



def addA_500(n):
    for i in range(500):
        n += 100
    return n

def addB_500(n):
    for i in range(50000):
        n+=1
    return n

def addP_500(n):
    for i in range(500):
        n+=100
        print("loop")
    return n

def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def sum2_n(n):
    return n*(n+1)/2

def nest_sum(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i * j
    return sum

start_time1 = time.time()
print(addA_500(12))
end_time1 = time.time()

start_time2 = time.time()
print(addB_500(12))
end_time2 = time.time()

start_time3 = time.time()
print(addP_500(12))
end_time3 = time.time()

print(end_time1-start_time1)
print(end_time2-start_time2)
print(end_time3-start_time3)

start_time3 = time.time()
print(sum_n(200000000))
end_time3 = time.time()
print(end_time3-start_time3)

start_time3 = time.time()
print(sum2_n(200000001))
end_time3 = time.time()
print(end_time3-start_time3)