'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''
def fruits_into_basket(arr):
    start = end = 0
    d = 0
    mp = dict()
    while end < len(arr):
        if arr[end] not in mp:
            mp[arr[end]] = 1
        else:
            mp[arr[end]] += 1
        
        while len(mp) > 2:
            mp[arr[start]] = mp.get(arr[start],0) - 1
            if mp[arr[start]] == 0:
                mp.pop(arr[start])
            start += 1 
        
        d = max(d, end - start + 1)
        end += 1
    return d 

def main():
    fruits = ['A','B','C','A','C']
    ans = fruits_into_basket(fruits)
    print(ans)

if __name__ == "__main__":
    main()

'''
Time Complexity : O(N)
Space Complexity : O(1)
'''    