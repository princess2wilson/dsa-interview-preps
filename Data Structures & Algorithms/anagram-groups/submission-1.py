class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            sorted_str = sorted(string)
            sorted_str = "".join(sorted_str) 
            hashmap[sorted_str].append(string)
            
        return list(hashmap.values())