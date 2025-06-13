class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        answer = [set(),set()]
        for num in nums1:
            if num not in s2 and num not in answer[0]:
                answer[0].add(num)
        for num in nums2:
            if num not in s1 and num not in answer[1]:
                answer[1].add(num)      
        answer[0] = list(answer[0])
        answer[1] = list(answer[1])       
        return answer