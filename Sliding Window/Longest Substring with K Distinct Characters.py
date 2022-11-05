'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''
# def longest_substring_with_distinct_characters(s,k):
#     start = end = 0
#     d = 0
#     mp = dict()
#     while end < len(s):
#         if s[end] not in mp:
#             mp[s[end]] = 1 
#         else:
#             mp[s[end]] += 1
        
#         while len(mp) > k :
#             mp[s[start]] = mp.get(s[start],0) - 1
#             if mp[s[start]] == 0:
#                 mp.pop(s[start])
#             start += 1
#         d = max(d,end - start + 1)
#         end += 1
#     return d


def longest_substring_with_distinct_characters(s,k):
    start = end = 0
    d = 0
    counter = 0
    mp = dict()
    while end < len(s):
        if mp.get(s[end], 0) == 0:
            counter += 1
            mp[s[end]] = 1 

        while counter > k :
            if mp.get(s[start] ,0 ) == 1:
                mp[s[start]] -= 1 
                counter -= 1 
                start += 1
        d = max(d,end-start + 1)
        end += 1
    return d


def main():
    s = "cbbebi"
    k = 3
    ans = longest_substring_with_distinct_characters(s,k)
    print(ans)

if __name__ == "__main__":
    main()
'''
Time Complexity : O(N)
Space Complexity : O(1)
'''