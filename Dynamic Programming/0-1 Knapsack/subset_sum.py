'''Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
'''

def subset_sum(arr,sum):
    n = len(arr)
    t = [[False for x in range(sum+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                t[i][j] = False 
            if j == 0:
                t[i][j] = True 

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]

def main():
    arr = [2,3,7,8,10]
    sum = 16 
    ans = subset_sum(arr,sum)
    print(ans)

if __name__ == "__main__":
    main()