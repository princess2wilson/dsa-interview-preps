from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for string in strs:
            sorted_string =''.join(sorted(string))
            hashmap[sorted_string].append(string)
            

        
        return list(hashmap.values())