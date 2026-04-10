class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import Counter
        counter = Counter()
        max_counter = 0

        l = 0

        for r in range(0,len(fruits)):
            counter[fruits[r]] +=1
            
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l+=1
            max_counter = max(r-l+1,max_counter)
        return max_counter
            




