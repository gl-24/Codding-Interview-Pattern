'''
Given an array arr[] of size N and a given difference diff, the task is to count the number of partitions that we can perform such that the difference between the sum of the two subsets is equal to the given difference.
Note: A partition in the array means dividing an array into two parts say S1 and S2 such that the union of S1 and S2 is equal to the original array and each element is present in only of the subsets.

Examples:
Input: N = 4, arr[] = [5, 2, 6, 4], diff = 3
Output: 1
Explanation: We can only have a single partition which is shown below:
{5, 2} and {6, 4} such that S1 = 7 and S2 = 10 and thus the difference is 3

Input: N = 5, arr[] = [1, 2, 3, 1, 2], diff = 1
Output: 5
Explanation: We can have five partitions which is shown below
{1, 3, 1} and {2, 2}  S1 = 5, S2 = 4
{1, 2, 2} and {1, 3}  S1 = 5, S2 = 4
{3, 2} and {1, 1, 2}  S1 = 5, S2 = 4
{1, 2, 2} and {1, 3}  S1 = 5, S2 = 4
{3, 2} and {1, 1, 2}  S1 = 5, S2 = 4
'''
def count(arr,n,sm):
    t = [[0 for x in range(sm+1)] for x in range(n+1)]
    
    #initialization
    for i in range(n+1):
        t[i][0] = 0
    for j in range(sm+1):
        t[0][j] = 1 

    for i in range(n+1):
        for j in range(sm+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][sm]



def main():
    arr = [1,1,2,3]
    n = len(arr)
    diff = 1 
    sm = diff + sum(arr) // 2 
    ans = count(arr,n,sm)
    print(ans)

if __name__ == "__main__":
    main()