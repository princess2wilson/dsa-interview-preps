class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = [-1]
        res = []

        for index,num in enumerate(nums1):
            hashmap[num] = index

        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>stack[-1]:
                stack.pop()
            if not stack:
                hashmap[nums2[i]] = -1
            else:
                hashmap[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        for num in nums1:
            res.append(hashmap[num])
        return res

            



        



        

