def table(n,i):
    
    if i<=10:
        print(n*i)
        i=i+1
        return table(n,i)
    else:
        return 0

table(12,1)
