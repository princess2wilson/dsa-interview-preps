class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recurse(temp,target,ind):
            if target == 0:
                result.append(temp[:])
                return
            if ind>=len(candidates) or target < 0:
                return

            temp.append(candidates[ind])
            recurse(temp,target-candidates[ind],ind+1)
            temp.pop()
            
            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind += 1
            recurse(temp,target,ind+1)
        recurse([],target,0)
        return result

            