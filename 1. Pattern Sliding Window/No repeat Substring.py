'''
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

def non_repeat_substring(s:str):
    start = end = 0
    d = 0 
    mp = {}
    while end < len(s):
        ch = s[end] 
        mp[ch] = mp.get(ch,0) + 1 
        while mp[ch] > 1:
            mp[s[start]] -= 1
            start += 1
        d = max(d, end - start + 1)
        end += 1
    return d 

def main():
    s = "aabccbb"
    ans = non_repeat_substring(s)
    print(ans)

if __name__ == "__main__":
    main()

