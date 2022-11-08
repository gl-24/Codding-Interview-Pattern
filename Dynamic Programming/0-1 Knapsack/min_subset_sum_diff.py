'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11  
'''
def min_subset_sum_diff(arr:list,n:int,rang:int):
    t = [[None for x in range(rang+1)] for x in range(n+1)]
    
    #Initialization 
    for i in range(n+1):
        for j in range(rang+1):
            if i == 0:
                t[i][j] = False

            if j == 0:
                t[i][j] = True 
    
    for i in range(1,n+1):
        for j in range(1,rang+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
        
    possible_sums = []
    for j in range((rang+1 )// 2):
        if t[n][j] == True:
            possible_sums.append(j)
        
    
    mn = rang
    for sums in possible_sums:
        mn = min(mn,rang - 2*sums)
    
    return mn


def main():
    arr = [1,6,11,5]
    n = len(arr)
    rang = sum(arr)
    ans = min_subset_sum_diff(arr,n,rang)
    print(ans)
if __name__ == "__main__":
    main()