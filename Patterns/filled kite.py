h=9
y=1
for x in range(h//2,0,-1):
    print(' '*x,'*'*y)
    y+=2

a=h+2
y=h
for x in range(0,h//2+1,1):
    print(' '*x,'*'*y)
    y-=2
