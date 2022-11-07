'''
Introduction 
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. 
The goal is to get the maximum profit out of the items in the knapsack. 
Each item can only be selected once, as we don’t have multiple quantities of any item.
Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. 
    Here are the weights and profits of the fruits:
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:
Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit
This shows that Banana + Melon is the best combination as it gives us the maximum profit and the total weight does not exceed the capacity.
'''
# Choice diagram 
def knapsack(wt,val,W,n)-> int:
    if n == 0 or W == 0:
        return  0 
    
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt,val,W - wt[n-1], n - 1), knapsack(wt,val,W,n-1))
    
    else:
        return knapsack(wt, val, W, n - 1)

# Memoization 
# t = [[-1] * 101] * 1001
def knapsack(wt,val,W,n)->int:
    t = [[0 for x in range(W+1)] for x in range(n+1)]    
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt,val,W - wt[n-1], n - 1), knapsack(wt,val,W,n-1))
    else:
        t[n][W] = knapsack(wt,val,W,n-1)
    
    if t[n][W] != -1:
        return t[n][W]

#Top Down Approach 
# t[n+1][w+1]
def knapsack(wt,val,W,n):
    t = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0

            if wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j - wt[i-1]], t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][W]        
    
    
def main():
    wt = [2,3,1,4]
    val = [4,5,3,7]
    W = 5 
    n = len(wt)
    ans = knapsack(wt,val,W,n) 
    print(ans)
if __name__ == "__main__":
    main()