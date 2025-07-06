class BubbleSort:
    def sort(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return nums
        pass

sol = BubbleSort()

nums=[2,6,5,1,3,4]
 
print(sol.sort(nums))