def unbounded_knapsack(wt,val,n,W):
    t = [[0 for i in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                t[i][j] = max(val[i-1]+t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]
def main(): 
    wt = [4,5,1]
    val = [1,2,3]
    W = 4 
    n = len(wt)
    ans = unbounded_knapsack(wt,val,n,W) 
    print(ans)
if __name__ == "__main__":
    main()