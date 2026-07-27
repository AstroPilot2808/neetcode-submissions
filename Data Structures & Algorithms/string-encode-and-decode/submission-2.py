class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer = answer + str(len(word)) + "#" + word

        print(answer)
        return answer

    def decode(self, s: str) -> List[str]:
        
        answer = list()

        i = 0
        while(i < len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            answer.append(s[i:i+length])
            i = i+length
        

        return answer

