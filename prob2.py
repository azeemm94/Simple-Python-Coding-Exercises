x=1
y=3
z=2
def max_of_three(a,b,c):
    if(a>b and a>c):
        return a
    else:
        if(b>c):
            return b
        else:
            return c
print(max_of_three(x,y,z))