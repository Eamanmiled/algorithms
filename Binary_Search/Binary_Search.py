nums = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
target = 8

high, low = len(nums) - 1, 0
mid = (low + high) // 2


while low <= high:
    if target < nums[mid]:
        high = mid - 1
        mid = (low + high) // 2
    elif target > nums[mid]:
        low = mid + 1
        mid = (low + high) // 2
    elif target == nums[mid]:
        print("target is index", mid)
        break
    else:
        print("target is not in list")
        break

