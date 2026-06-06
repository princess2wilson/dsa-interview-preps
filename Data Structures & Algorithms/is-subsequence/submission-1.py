from collections import defaultdict
import bisect
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev = -1
        hashmap = defaultdict(list)

        for i, x in enumerate(t):
            hashmap[x].append(i)
        
        for index,char in enumerate(s):
            if char not in hashmap:
                return False

            idx = bisect.bisect_right(hashmap[char],prev)
            if idx ==len(hashmap[char]):
                return False
            prev = hashmap[char][idx]
        return True
            



