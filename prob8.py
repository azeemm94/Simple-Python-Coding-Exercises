def is_member(a,x):
    n=len(a)
    for i in range(0,n-1):
        if(i==x):
            return "True"
    return "False"
a=[1,2,3,4,5]
x=2
print(is_member(a,x))