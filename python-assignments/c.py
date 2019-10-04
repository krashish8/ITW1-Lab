def gcd(x,y):
    if (x==0):
        return y
    return gcd(y%x,x)

t = int(input())
for ii in range(1, t+1):
    ans = []
    dic = {}
    idx = -1
    a,b = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans.append(-1)
    for i in range(0,b-1):
        if l[i]==l[i+1]:
            ans.append(-1)
        elif int(l[i]**0.5) != l[i]**0.5:
            ans.append(gcd(l[i], l[i+1]))
            if idx==-1:
                idx = i + 1
        else:
            ans.append(l[i]**0.5)
            ans.append(-1)
    f = 0
    for i in range(idx+1,len(ans)):
        if ans[i] == -1:
            ans[i] = l[i-1]//ans[i-1]
    
    for i in range(idx-1,-1,-1):
        if ans[i] == -1:
            ans[i] = l[i]//ans[i+1]
    
    anss = sorted(set(ans))
    c = 65
    for i in anss:
        dic[i] = chr(c)
        c += 1
    print("Case #"+str(ii)+": ",end="")
    for i in ans:
        print(dic[i],end="")
    print()
