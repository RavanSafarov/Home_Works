#Task1

# for x in range(5):
#     for y in range(5):
#         if x == 1 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 3:
#             print(" ", end='')
#             continue
#         print("*", end='')
#     print()

#Task2

# for x in range(4):
#     for y in range(8):
#         if x == 1 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 4:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 5:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 6:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 4:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 5:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 6:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 3:
#             print(" ", end='')
#             continue
#         print("*", end='')
#     print()

#Task3

# for x in range(8):
#     for y in range(5):
#         if x == 1 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 1 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 2 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 3 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 4 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 5 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 5 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 5 and y == 3:
#             print(" ", end='')
#             continue
#         if x == 6 and y == 1:
#             print(" ", end='')
#             continue
#         if x == 6 and y == 2:
#             print(" ", end='')
#             continue
#         if x == 6 and y == 3:
#             print(" ", end='')
#             continue
#         print("*", end='')
#     print()

#Task4

# for x in range(6):
#     if x == 0:
#         print("* * * * * *")
#     elif x == 1:
#         print(" * * * * *")
#     elif x == 2:
#         print("  * * * *")
#     elif x == 3:
#         print("   * * *")
#     elif x == 4:
#         print("    * *")
#     elif x == 5:
#         print("     *")
#
# print()
#
# for x in range(1, 6):
#     if x == 1:
#         print("     *")
#         print("    * *")
#     elif x == 2:
#         print("   * * *")
#     elif x == 3:
#         print("  * * * *")
#     elif x == 4:
#         print(" * * * * *")
#     elif x == 5:
#         print("* * * * * *")
#print()

#Task5

# for x in range(6):
#     if x == 0:
#         print("* * * * * *")
#     elif x == 1:
#         print(" * * * * *")
#     elif x == 2:
#         print("  * * * *")
#     elif x == 3:
#         print("   * * *")
#     elif x == 4:
#         print("    * *")
#     elif x == 5:
#         print("     *")
#
# for x in range(6):
#     if x == 0:
#         print("    * *")
#     elif x == 1:
#         print("   * * *")
#     elif x == 2:
#         print("  * * * *")
#     elif x == 3:
#         print(" * * * * *")
#     elif x == 4:
#         print("* * * * * *")
#print()

#Task6

# oreal = 5
# star1 = 1
# star2 = 1
#
#
# for y in range(11):
#     for x in range(star1):
#         print("*", end=" ")
#     for h in range(oreal):
#         print(" ", end=" ")
#     for z in range(star2):
#         print("*", end=" ")
#
#     print()
#     if y < 5:
#         star1 += 1
#         star2 += 1
#         oreal -= 1
#     else:
#         star1 -= 1
#         star2 -= 1
#         oreal += 1
# print()

#Task7


# for i in range(4):
#     if i == 0:
#         print('*     *')
#     elif i == 1:
#         print(' *   *')
#     elif i == 2:
#         print('  * *')
#     elif i == 3:
#         print('   *')
#
#
# for i in range(3):
#     if i == 0:
#         print('  * *')
#     elif i == 1:
#         print(' *   *')
#     elif i == 2:
#         print('*     *')
