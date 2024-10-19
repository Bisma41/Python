num=5
i=1
while i<=num:
    j=1
    count=0
    while j<=num:
        if i%j==0:
            count=count+1
        j=j+1
    if count<=2: 
        print(i)
    i=i+1
