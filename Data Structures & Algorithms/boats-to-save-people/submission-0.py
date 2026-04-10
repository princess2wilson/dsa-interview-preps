class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #[1,2,4.5]

        r = len(people) - 1
        l = 0
        res = 0

        while l <= r:
            remaining = limit - people[r]
            r-=1
            res+=1
            if l<=r and remaining >=people[l]:
                l+=1
        return res


