from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        queue = deque([beginWord])
        visited = set(beginWord)
        if endWord not in wordList:
            return 0
        count = 1

        for word in wordList:
            for x in range(len(word)):
                key = word[:x] + "*" + word[x+1:]
                graph[key].append(word)
        

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for x in range(len(word)):
                    key = word[:x] + "*" + word[x+1:]
                    for nei in graph[key]:
                        if nei == endWord:
                            return count+1
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            count+=1
        return 0