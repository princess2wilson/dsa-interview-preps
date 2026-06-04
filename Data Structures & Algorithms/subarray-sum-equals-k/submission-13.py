class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        1. check if totals target number has already been seen before
        2. if it has , update our count because we have another valid subarray
        3. update our map with prefix:+=1

        """
        hashmap = defaultdict(int)
        hashmap[0] =1
        count = 0
        total = 0
        for num in nums:
            total+=num
            if total-k in hashmap:
                count+=hashmap[total-k]
            hashmap[total]+=1

        return count
