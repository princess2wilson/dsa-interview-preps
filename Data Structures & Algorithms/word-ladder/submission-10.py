from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        queue = deque()
        count = 1
        visited = set()
        visited.add(beginWord)
        
        if endWord not in wordList:
            return 0

        for word in wordList:
            for i,x in enumerate(word):
                word_ = word[:i]+ "*" + word[i+1:]
                graph[word_].append(word)
        

        queue.append(beginWord)
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if endWord == word:
                    return count
                
                for i,x in enumerate(word):
                    word_ = word[:i]+ "*" + word[i+1:]
                    if word_ in graph:
                        for words in graph[word_]:
                            if words not in visited:
                                visited.add(words)
                                queue.append(words)
            count+=1
        return 0
            
        

        
        
            


"""
1. maker a graph with *at, 
c*t and ca* as the keys and add all the words in worlist that have 
those to the neighbours.
Then traverse the graph until you get to sad in 
the list of the key youre checking.
needs to be bfs and not dfs
"""