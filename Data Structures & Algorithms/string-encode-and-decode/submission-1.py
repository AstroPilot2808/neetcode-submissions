class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""

        for word in strs:
            answer = answer + word + "..."

        return answer

    def decode(self, s: str) -> List[str]:
        answer = s.split("...")

        answer.pop(-1)

        return answer
