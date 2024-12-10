#Task1

from random import randint

# nums = []
# i = 0
#
# while i < 10:
#     rnd = randint(-100, 100)
#     i += 1
#     nums.append(rnd)
# print(nums)
#
# i = 0
# sum = 0
# sum1 = 0
# while i < 10:
#     if nums[i] < 0:
#         sum += nums[i]
#     else:
#         sum1 += nums[i]
#     i += 1
# print("Negative numbers: ")
# print(sum)
# print("Positive numbers: ")
# print(sum1)
#
# i = 0
# sum2 = 0
# sum3 = 0
# sum4 = 1
# while i < 10:
#     if nums[i] % 2 == 0:
#         sum2 += nums[i]
#     if nums[i] % 3 == 0:
#         sum4 *= nums[i]
#     else:
#         sum3 += nums[i]
#     i += 1
# print("Even numbers: ")
# print(sum2)
# print("Numbers which can divided by 3: ")
# print(sum4)
# print("Odd numbers: ")
# print(sum3)

#Task2

# original =[]
# even = []
# odd = []
# negative = []
# positive = []
#
# i = 0
#
# while i < 10:
#     rnd = randint(-100, 100)
#     original.append(rnd)
#     i += 1
# print("Range: ")
# print(original)
#
# i = 0
#
# while i < len(original):
#     if original[i] % 2 == 0:
#         even.append(original[i])
#     if original[i] % 2 == 1:
#         odd.append(original[i])
#     if original[i] > 0:
#         positive.append(original[i])
#     if original[i] < 0:
#         negative.append(original[i])
#     i += 1
#
#
# print("Even numbers: ")
# print(even)
# print("Odd numbers: ")
# print(odd)
# print("Positive numbers: ")
# print(positive)
# print("Negative numbers: ")
# print(negative)