# Courtnay McEwen
# Josh Wright
# Steven Willis
# Raymond Phillips
# Don Huey

# def oneTo255():
#     for in range(1, 256):
#         print(i)

# oneTo255()


# def intsAndSums():
#     sum = 0
#     for i in range(256):
#         print(i)
#         sum += i
#         print(sum)

# intsAndSums()

# def maxOfLst(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     print(max)

# maxOfLst([2,5,9,3,1])

# def oddLst():
#     newLst = []
#     for i in range(1, 256):
#         if i % 2 != 0:
#             newLst.append(i)
#     return newLst

# print(oddLst())


# def greaterThanY(lst, Y):
#     count = 0
#     for i in lst:
#         if i > Y:
#             count += 1
#     print(count)

# greaterThanY([2,4,6,8,15], 5)

# def maxMinAvg(lst):
#     max = lst[0]
#     min = lst[0]
#     sum = lst[0]
#     for i in lst[1:]:
#         if i > max:
#             max = i
#         elif i < min:
#             min = i
#         sum += i
#     avg = sum/len(lst)
#     print(f"Max: {max}, Min: {min}, Avg: {avg}")

# maxMinAvg([5,6,7,8,10])

# def swapNegVals(lst):
#     for idx in range(len(lst)):
#         if lst[idx] < 0:
#             lst[idx] = "Dojo"
#     return lst

# b = swapNegVals([-1, 3, -6, 8])
# print(b)


# def printOdds():
#     for i in range(1,256, 2):
#         print(i)

# printOdds()

# def lstVals(lst):
#     for i in lst:
#         print(i)

# lstVals()

# def lstAvg(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     avg = sum/len(lst)
#     print(avg)

# lstAvg([1,2,3,4,5])

# def squareLstVal(lst):
#     for idx in range(len(lst)):
#         lst[idx] = lst[idx] * lst[idx]
#     print(lst)

# squareLstVal([2,4,6,8])

# def zeroNegVals(lst):
#     for idx in range(len(lst)):
#         if lst[idx] < 0:
#             lst[idx] = 0
#     return lst

# b = zeroNegVals([3, -5, 6, 9])
# print(b)

# def shiftVals(lst):
#     for idx in range(len(lst) - 1):
#         lst[idx] = lst[idx + 1]
#     lst[-1] = 0
#     return lst

# b = shiftVals([2,3,4,5,6])
# print(b)

