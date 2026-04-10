class Solution:
    from collections import defaultdict
    import string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            count = [0]*26
            for letter in string:
                count[ord(letter)-ord('a')]+=1
            result[tuple(count)].append(string)
        return list(result.values())

        