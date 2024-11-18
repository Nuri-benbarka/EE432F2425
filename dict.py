dic = {}

dic["Nuri"] = 34
dic["moh"] = 22
dic["aya"] = 21

print(dic)

# del dic["Nuri"]

print(dic)
print(dic["moh"])

for k, v in dic.items():
    if v < 30:
        print(k)

a = [[i,i**2] for i in range(10)]
print(a)

for i , j in enumerate(a):
    print(f"{i,j}")