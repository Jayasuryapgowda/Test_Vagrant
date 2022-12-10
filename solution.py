target = int(input())
subs = ['TOI','HINDU','ET','BM','HT']
subs_amt = [26,20.5,34,10.5,18]
res = []
n = len(subs_amt)

def sol(target):
    for i in range(0,n-1):
        for j in range(i,n-1):
            if subs_amt[i] == subs_amt[j]:
                continue
            elif subs_amt[i]+subs_amt[j] <= target:
                res.append([subs[i],subs[j]])
                continue
    return res

print(sol(target))