# Source: https://usaco.guide/general/io
#coins = 1, 3, 6, 10, 15
 
a = input()
coins = [1, 3, 6, 10, 15]
a = int(a)
dp = [10**9] * 100
dp[0] = 0
# for i in range(100):
#     for c in coins:
#         if i - c >= 0:
#             dp[i] = min(dp[i], dp[i-c] + 1)
 
# print(dp)
#exceptions
# 23, 22, 46
# 68
for i in range(a):
    curr = input()
    curr = int(curr)
    count = 0
    
    if curr > 15:
        count += curr // 15
        curr -= count * 15
        
        if curr == 8:
            curr += 15
            count -= 1
        if curr == 5:
            curr += 15
            count -= 1
 
 
    while(curr > 0):
        if curr == 20:
            curr -= 20
            count += 2
        elif curr == 23:
            curr -= 23
            count += 3
        elif curr == 12:
            curr -= 12
            count += 2
        elif curr >= 15:
            curr -= 15
            count += 1
        elif curr >= 10:
            curr -= 10
            count += 1
        elif curr >= 6:
            curr -= 6
            count += 1
        elif curr >= 3:
            curr -= 3
            count += 1
        else:
            curr -= 1
            count += 1
        
    print(count)