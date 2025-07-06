def majorityElement(nums):
    count = {}
    ans = 0

    for i in range(len(nums)):
        count[nums[i]] = 1 + count.get(nums[i], 0)

    for key, value in count.items():
        print(count)
    pass

print(majorityElement([3,2,2,3,4,1]))