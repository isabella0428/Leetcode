from collections import defaultdict, deque


class Solution:
    # bfs
    def ladderLength(self, beginWord, endWord, wordList):
        def constructDict(wordlist):
            d = defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    d[s].append(word)
            return d

        def bfs(beginWord, endWord, wordList):
            queue,visited = deque([[beginWord, 1]]), set()
            dict = constructDict(wordList)
            while queue:
                word, num = queue.popleft()
                if word == endWord:
                    return num
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i+1:]
                    for neighbour in dict[s]:
                        if neighbour in visited:
                            continue
                        else:
                            visited.add(neighbour)
                            queue.append([neighbour,num + 1])
            return 0
        return bfs(beginWord, endWord,wordList)


if __name__ == "__main__":
    a = Solution()
    print(a.ladderLength("a", "c", ['a','b','c']))