import Queue

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(endWord)
        visited=Queue.Queue()
        
        self.addNextWords(beginWord, wordList, visited)
        dist=2
        while not visited.empty():
            num=len(visited)
            for i in range(len(num)):
                word=visited.peek    #front 
                visited.pop()
                if word == endWord: 
                    return dist
                addNextWords(word, wordList, visited)
            dist+=1
        
    def addNextWords(self, word, wordList, visited):
        wordList.remove(word)
        
        for w in range(len(word)):
            letter=word[w]
            for k in range(26): 
                word[w]='a'+k
                if word in wordList and word!=wordList[-1]:  #last element
                    visited.put(word)
                    wordList.remove(word)
            word[w]=letter 
        
#BFS