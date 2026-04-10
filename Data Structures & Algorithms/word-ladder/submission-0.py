class Solution:
    from collections import defaultdict,deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0

        graph = defaultdict(list)

        #lets all possible words of word to graph: bat:[*at,b*t,ba*]
        #graph: {*at:[bat],b*t:[bat]}
        for word in wordList:
            for i in range(len(word)):
                transform = word[:i]+"*"+word[i+1:]
                graph[transform].append(word)


        queue = deque([(beginWord, 1)])
        
        while queue:
            word,distance = queue.popleft()
            if word == endWord:
                return distance
            
            visited.add(word)

            for i in range(len(word)):
                transformed = word[:i]+"*"+word[i+1:]
                potential_words = graph.get(transformed,None)
                if potential_words:
                    for x in potential_words:
                        if x not in visited:
                            queue.append((x,distance+1))
        return 0
