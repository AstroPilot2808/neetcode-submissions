class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        masterCount = dict()
        answer = list(list())

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            if tuple(count) in masterCount:
                masterCount[tuple(count)].append(s)
            else:
                masterCount[tuple(count)] = [s]
        print(masterCount.values())
        for wordList in masterCount.values():
            answer.append(wordList)

        return answer
        