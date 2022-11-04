def equal_sum_partition(arr,n,sum):
    t = [[None for x in range(sum + 1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    for i in range(n+1):
        for j in range(sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j] 
            else:
                t[i][j] = t[i-1][j]
    
    if t[n][sum]==None:
        return False
    return t[n][sum]

def main():
    arr = [1,5,11,5]
    n = len(arr)
    s = sum(arr) 
    ans = 0
    if s % 2 != 0:
        ans = False
    else:
        ans = equal_sum_partition(arr,n,s // 2)
    print(ans)

if __name__ == "__main__":
    main()