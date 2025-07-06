class SelectionSort:
    def sort(self, nums):
        minIndex = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[minIndex]:
                minIndex = i
                nums[minIndex] = nums[i]
        
        return nums
        pass

sol = SelectionSort()

nums=[4,2,6,5,1,3]
 
print(sol.sort(nums))