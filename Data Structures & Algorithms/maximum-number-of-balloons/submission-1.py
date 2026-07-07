class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        count=0
        for char in text:
            freq[char] = freq.get(char,0)+1
        
        while (
            freq.get("b", 0) >= 1 and
            freq.get("a", 0) >= 1 and
            freq.get("l", 0) >= 2 and
            freq.get("o", 0) >= 2 and
            freq.get("n", 0) >= 1
        ):
            count += 1
            freq["b"] -= 1
            freq["a"] -= 1
            freq["l"] -= 2
            freq["o"] -= 2
            freq["n"] -= 1
        
        return count

