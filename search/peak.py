num = [1, 2, 3, 4, 5, 6]

target = 4

start = 0
end = len(num) - 1

while(start <= end):
    mid = (start + end) // 2

    if num[mid] == target:
        print(mid)
        break
    elif num[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
else:
    print("target not found")

num2 = [0, 2, 3, 4, 5, 4, 3, 2, 1, 0]

start = 0
end = len(num2) - 1

for num in num2:
    mid = (start + end) // 2

    if (num2[mid] < num2[mid+1]):
        mid = start + 1
    elif (num2[mid-1] > num2[mid]):
        end = mid
    else:
        print(num2[mid])
        break
