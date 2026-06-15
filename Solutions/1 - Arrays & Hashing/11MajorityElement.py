def majorityElement(nums):
    # res, count = 0,0

    # for n in nums:
    #     if count == 0:
    #         res = n
    #     count += (1 if n == res else -1)
    
    # return res

    count = {}
    res, maxCount = 0, 0

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > maxCount else res
        maxCount = max(maxCount, count[n])
    
    return res

print(majorityElement([2,2,1,1,1,2,2]))