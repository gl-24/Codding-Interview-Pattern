'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''
def remove_duplicates(arr):
    i = 1
    length = 1
    while i < len(arr):
        if arr[i-1] != arr[i]:
            length+=1
        i+=1
    return length

def main():
    arr = [2,3,3,3,6,9,9]
    print(remove_duplicates(arr))
if __name__ == "__main__":
    main()