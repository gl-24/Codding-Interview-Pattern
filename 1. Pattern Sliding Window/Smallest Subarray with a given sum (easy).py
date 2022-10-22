'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''
def smallest_subarray_with_given_sum(k, arr):
    start = end = 0 
    d = len(arr) + 1 
    add = 0 
    while end < len(arr):
        add += arr[end]
        while add >= k
            d = min(d,end - start + 1)
            add -= arr[start]
            start += 1
        end += 1
    return d 

def main():
    arr = [2,1,5,2,3,2]
    k = 7 
    ans = smallest_subarray_with_given_sum(k,arr) 
    print(ans)

if __name__ == "__main__":
    main()
'''
Time Complexity : O(N)
Space Complexity : O(1)
'''