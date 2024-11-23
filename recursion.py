import sys
import time


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


# sys.setrecursionlimit(100000)
print(factorial(-5))


def power_2(n):
    if n == 0:
        return 1
    elif n > 0:
        return 2 * power_2(n - 1)
    else:
        return power_2(n + 1) / 2


print(power_2(3))
print(power_2(-2))


def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        first_half_sum = sum_array(arr[:len(arr) // 2])
        second_half_sum = sum_array(arr[len(arr) // 2:])
        return first_half_sum + second_half_sum


def sum_array_index(arr, start_index, end_index):
    if start_index == end_index - 1:
        return arr[start_index]
    else:
        half_index = (start_index + end_index) // 2
        first_half_sum = sum_array_index(arr, start_index, half_index)
        second_half_sum = sum_array_index(arr, half_index, end_index)
        return first_half_sum + second_half_sum


print(sum_array([1, 2, 3, 4, 5]))
print(sum_array_index([1, 2, 3, 4, 5], 0, 5))


def fabonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pre = fabonaci(n - 1)
        before_pre = fabonaci(n - 2)
        return pre + before_pre


def fabonaci_hash(n, result_dic):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n - 1 in result_dic:
            f_1 = result_dic[n - 1]
        else:
            f_1 = fabonaci_hash(n - 1, result_dic)
            result_dic[n - 1] = f_1
        if n - 2 in result_dic:
            f_2 = result_dic[n - 2]
        else:
            f_2 = fabonaci_hash(n - 2, result_dic)
            result_dic[n - 2] = f_2
        return f_1 + f_2


n = 40
start_time = time.time()
print(fabonaci(n))
print(time.time() - start_time)
start_time = time.time()
print(fabonaci_hash(n, {}))
print(time.time() - start_time)
