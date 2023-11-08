class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        j=min(len(word1), len(word2))

        for i in range(j):
            res.append(word1[i]+word2[i])

        return ''.join(res) + word1[i+1:] + word2[i+1:]
        
        