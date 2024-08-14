s1 = "RAHULLUHAR"

# start = 0
# end = len(s1) - 1
# flag = False

# while (start < end):
#     if (s1[start] == s1[end]):
#         start = start + 1
#         end = end - 1
#         flag = True
#     else:
#         flag = False
#         break

# print(flag)

def reverse(s1, start, end, flag):
    if (start > end):
        return True
    
    if (s1[start] == s1[end]):
        flag = reverse(s1, start+1, end-1, flag)
    return flag


start = 0
end = len(s1) - 1
flag = False
ans = reverse(s1, start, end, flag)
print(ans)


# import time

# def time_taken_cal(func):
#     def wapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         total_time = end - start
#         return result, total_time
#     return wapper

# @time_taken_cal
# def reverse(str):
#     return str[::-1]

# str = "rahul"

# str_rev, time = reverse(str)
# print(str_rev)
# print(time)
