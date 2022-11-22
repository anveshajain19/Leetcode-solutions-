class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {} # Hash Table   
        ans = []   # every word's frequency 
        odd= 0     # store an odd number's frequency 
        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for times in count.values():
            ans.append(times)
            if times % 2 != 0:
                odd += 1      # calculate an odd number's frequency
        if odd != 0:
            return sum(ans) - odd + 1        
        elif odd == 0:
            return sum(ans) - odd