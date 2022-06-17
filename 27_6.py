
file = open("27.txt")
n,m = map(int,file.readline())
a = [int(i) for i in file.readlines()]

s = [a[i]*min(i,len(a)-i) for i in range(len(a))]
s_p = sum(a[:n//2])
s_m = sum(a[n//2+n%2:])

min_s = s
ans = 0
for i in range(0,n):
    s_p += a[i]-a[n//2+i+n%2]   
    s_m += a[n//2+i]-a[i]
    s += s_p-s_m
    if s < min_s:
        ans = i+1
        min_s=s





