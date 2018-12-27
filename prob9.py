def overlapping(a,b):
    for i,val1 in enumerate(a):
        for j,val2 in enumerate(b):
            if(val1==val2):
                return "True"
    return "False"
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(overlapping(a,b))