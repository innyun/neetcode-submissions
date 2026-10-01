class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        l = len(beginWord)

        if endWord not in wordList:
            return 0

        seen = set()

        q = deque([(beginWord, 1)])
        while q:
            for _ in range(len(q)):
                word, step = q.popleft()
                # print(word, step)
                if word == endWord:
                    return step
                
                seen.add(word)

                for i in range(l):
                    for j in range(26):
                        new_word = list(word)
                        new_word[i] = chr(ord('a') + j)
                        new_word = ''.join(new_word)
                        if new_word != word and new_word in wordList and new_word not in seen:
                            q.append((new_word, step + 1))

        return 0