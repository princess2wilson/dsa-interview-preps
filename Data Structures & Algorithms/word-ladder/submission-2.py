class Solution:
    from collections import defaultdict,deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        count = 1
        visited = set()
        
        graph = defaultdict(list)
        for word in wordList:
            for i,x in enumerate(word):
                split = word[:i] + "*" + word[i+1:]
                graph[split].append(word)
            


        visited = set()
        queue = deque()
        queue.append((beginWord,count))

        while queue:
            word,count = queue.popleft()
            if word in visited:
                continue
            visited.add(word)
            for i,x in enumerate(word):
                split = word[:i] + "*" + word[i+1:]
                if split in graph: 
                    for words in graph[split]:
                        if words == endWord:
                            return count+1
                        queue.append((words,count+1))
        return 0



        