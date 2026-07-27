class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = dict()
        answer = list(list())

        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            if sortedWord in count:
                count[sortedWord].append(i)
            else:
                count[sortedWord] = [i]

        for words in count:
            subWord = []
            for word in count[words]:
                subWord.append(strs[word])
            answer.append(subWord)
            print(subWord)


        return answer
        