def consecutive(arr, a, b):
    for x in range(1,len(arr)):
        if arr[x-1] == a and arr[x] == b:
            return True
        elif arr[x-1] == b and arr[x] == a:
            return True
    return False

#    for x in arr:
#         if arr[x] == a or b:
#             if arr[x+1] == a or b:
#                 return True
#         else:
#             return False


lists = [1, 6, 9, -3, 4, -78, 0]

print(consecutive(lists, -3, 5))
