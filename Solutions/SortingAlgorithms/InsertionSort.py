class InsertionSort:
    def sort(self, nums):
        for i in range(1, len(nums)):
            j = i - 1

            while nums[i] < nums[j] and j > -1:
                nums[j+1], nums[j] = nums[j], nums[i]
                j = j - 1
            
        return nums
        pass

sol = InsertionSort()

nums=[4,2,6,5,1,3]
 
print(sol.sort(nums))