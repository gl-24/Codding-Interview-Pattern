def count_of_subsets(arr,n,sum):
    t = [[0 for x in range(sum+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                t[i][j] = 0
            
            if j == 0:
                t[i][j] = 1 
    
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j - arr[i - 1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][sum] 

def main():
    arr = [2,3,5,6,8,10]
    arr = [3,3,3,3]
    n = len(arr)
    s = 6
    ans = count_of_subsets(arr,n,s)
    print(ans)
if __name__ == "__main__":
    main()