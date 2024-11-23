

def count_freq(str):
    freq = {}
    for ch in str:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq

str = input("enter a sentence")
print(count_freq(str))


def common_ele(lst1,lst2):
    l1 = set()
    for ele in lst1:
        l1.add(ele)
    result = []
    for ele in lst2:
        if ele in l1:
            result.append(ele)
    return result

print(common_ele([1,2,3,4,5],[2,4,6]))

# remove duplicates
print(list(set([1,1,1,1,1,1,12,2,2,2,1,1])))