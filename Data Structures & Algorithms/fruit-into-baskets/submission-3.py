class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_map = {}
        max_fruits = 0
        l = 0

        for r in range(len(fruits)):
            fruit_map[fruits[r]] = 1+fruit_map.get(fruits[r],0)
            
            while len(fruit_map) > 2:
                fruit_map[fruits[l]]-=1
                if fruit_map[fruits[l]] ==0:
                    fruit_map.pop(fruits[l])
                l+=1
            max_fruits = max(max_fruits, (r-l+1))

        return max_fruits
        
            


