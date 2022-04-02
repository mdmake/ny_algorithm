"""
https://leetcode.com/problems/valid-palindrome-ii
"""


class Solution:
    def palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i] == s[j - 1]:
                    rez1 = self.palindrome(s[i:j])
                    if rez1:
                        return True

                if s[i + 1] == s[j]:
                    i += 1
                    rez2 = self.palindrome(s[i:j + 1])
                    if rez2:
                        return True

                return False

        return True


def main():
    sol = Solution()
    # sol.validPalindrome('abc')
    # print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("udud"))
    print(sol.validPalindrome("uddud"))
    print(sol.validPalindrome("duddu"))
    # print(sol.validPalindrome('aaaaaaaavaaaaaaaa'))
    # print(sol.validPalindrome('aaaaaaaavlaaaadaaaa'))
    # print(sol.validPalindrome("eeccccbebaeeabebccceea"))
    # print(sol.validPalindrome(
    #    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
    # print(sol.validPalindrome(
    #    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))


if __name__ == '__main__':
    main()
