# This is my first python program
from lecture1 import count

a = """
dsgdsgfdhfg
dsfghfdhgh
öfdskalhjgds
"""
print("Hello World!")
print(a)

a = 9
b = 6.5
c = 5 + 6j
d = True # True is a keyword
e = "My name is Nuri"

print(c)
print(f"the value of b: {b}")

#name = input("What is your name?")

#print(f"Hi, {name}. Nice to meet you!")

# print("enter two numbers")
# A = complex(input())
# B = complex(input())
# C = A + B
# print(C)

print(3*5+2)
print(3*(5+2))
print(2**3**2)
print(2**2**3)
print(int(True and False))
print(6<8)
print(10/3 == 3 + 1 / 3)
print(abs((10/3) - (3+1/3)) < 10**-6)
print(10/3)

print(13&10)
print(13|10)
print(13^10)
print(~13)

i = 5

i += 10

print(i)

# grade = int(input("Enter the grade:"))
#
# if grade>=85:
#     print("Excellent")
# elif 75 <= grade < 85:
#     print("Very good")
# elif 50 <= grade < 75:
#     print("pass")
# else:
#     print("Work harder next time!")
#
# print("pass") if grade>=50 else print("fail")
def adding_fun(a,b,d):
    c = a + b + d
    return c , b + d

a="1"
sm = adding_fun(a,"2","3")  #HW

print(sm)

count = 100

while count > 0:
    print(count)
    count -= 1

st = "Hi, I am a new student"
i = 0

while i < len(st):
    if st[i] == "a" or st[i] == "i" or st[i] == "e" or st[i] == "o" or st[i] == "u":
        i += 1
        continue
    print(st[i], end="")
    i += 1

print("")
for ch in st:
    if ch not in "aieouAIEOU":
        print(ch, end="")

print("")
A = [1,2,3,4,5,6,7]
B = [4,5,6]

for a, b in zip(A,B):
    print(a + b)

for i, ch in enumerate(st):
    print(f"{i}:{ch}")


for i in range(50,100,5):  # generator
    if i % 20 == 0:
        break
    print(i,end=" ")

def addlkjf():
    pass

print(A)
print(B)
#A.reverse()
print(A[:2])
print(A[2:])
print(A[2:5])
print(A[-2])
A.insert(3,15)
print(A)
A.pop()
print(A)

C = []

for i in range(0,100,5):
    C.append(i)

print(C)

D = [i//2 for i in range(0,100,5) if i%10 != 0]
print(D)

