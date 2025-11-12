class Solution:
    def longestPalindromeSubstring(self, s: str) -> str:
        output = ""
        maxLength = 0

        for i in range(len(s)):
            # Odd length scenario
            l, r = i, i
            while l >= 0 and r < len(s)and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    output = s[l:r + 1]
                    maxLength = r - l + 1
                
                l -= 1
                r += 1
            
            # Even length scenario
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    output = s[l:r + 1]
                    maxLength = r - l + 1
                
                l -= 1
                r += 1
        
        return output

if __name__ == "__main__":
    s = Solution()
    a = input()
    print("Longest palindrome substring in ", a, " is: ", s.longestPalindromeSubstring(a))

