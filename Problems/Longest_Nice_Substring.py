"""A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.



Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings. """


#Solution

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        windowSize = len(s) - 1

        niceString = ""

        while len(niceString) < 1 and windowSize > 0:
            for i in range(len(s) - windowSize):
                #print(s[i:windowSize+i+1])
                if len(niceString) > 0 :
                    break
                stringToCheck = s[i:windowSize+i+1]
                #print(self.isNice(stringToCheck),stringToCheck)
                if self.isNice(stringToCheck):
                    niceString = stringToCheck

            windowSize-=1

        return niceString


    def isNice(self,s: str)-> bool:

        allCaps = set()

        for character in s:
            if ord(character)<=90:
                allCaps.add(character)

        for character in s:
            if ord(character) >=97:
                if chr(ord(character)-32) not in allCaps:
                    return False

        allSmall = set()

        for character in s:
            if ord(character) >= 97:
                allCaps.add(character)

        for character in s:
            if ord(character) <= 90:
                if chr(ord(character)+32) not in allCaps:
                    return False

        return True

# Link : https://leetcode.com/problems/longest-nice-substring/
