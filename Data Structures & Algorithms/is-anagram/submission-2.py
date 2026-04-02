class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashA = {}
        hashB = {}
        for i in s:
            if i in hashA:
                hashA[i] +=1
            else:
                hashA[i] = 1
        for index in t:
            if index in hashB:
                hashB[index] +=1
            else:
                hashB[index] = 1
        return hashA == hashB