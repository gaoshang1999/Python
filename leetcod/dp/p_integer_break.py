

def integerBreakDp(n, arr):
    
    dp = [0] * (n+1)
    dp[0] = 1    
    
    for i in range(1, n+1):
        for a in arr:
            if i-a >=0 :
                dp[i] += dp[i-a]
        print(dp)
    
    return dp

def construct(arr, dp, i, solution):
    if i == 0 :
        print(solution)
    
    for a in arr:
        if i - a >= 0 :
            solution.append(a)
            construct(arr, dp, i-a, solution)
            solution.pop()
    
    
def integerBreak(n, arr):
    
    def helper(n, arr,ret):  
        l = len(arr)  
        if n == 0 :
#             print(ret)
            return 1
        
        if n < 0:
            return 0
        
        c = 0        
        for i in range(l):
            a = arr[i]
            ret.append(a)
            c += helper(n-a, arr, ret)
            ret.pop()
        return c

    return helper(n, arr, [])

def integerBreak_noRepeat(n, arr):
    
    def helper(n, arr, j, ret):  
        l = len(arr)  
        if n == 0 :
            print(ret)
            return 1
        
        if n < 0 or j == l:
            return 0
        
        c = 0        
        for i in range(j, l):
            a = arr[i]
            ret.append(a)
            c += helper(n-a, arr, j+1, ret)
            ret.pop()
        return c

    return helper(n, arr, 0, [])

def integerBreak_noRepeat_Dp(n, arr):
    
    dp = [0] * (n+1)
    dp[0] = 1    
    
    for a in arr:
        for i in range(n, 0, -1):
            if i-a >=0 :
                dp[i] += dp[i-a]
        print(dp)        
    
    return dp[-1]    

n = 7
arr = [1, 3, 4]

print(integerBreak(n, arr))
dp = (integerBreakDp(n, arr))    

construct(arr, dp, len(dp)-1, [])
print()

print(integerBreak_noRepeat(n, arr))   
print(integerBreak_noRepeat_Dp(n, arr))    