class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])
        print(left)

        right = [1]
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[len(nums) - 1 - i] * nums[i])
        print(right)
        
        answer = []
        for i in range(len(nums)):
            answer.append(left[i] * right[len(nums) - 1 - i])
        return answer