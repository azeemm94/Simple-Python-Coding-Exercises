def char_freq(str):
    a=list(str)
    x=dict()
    for i,val in enumerate(a):
        if val in x:
            x[val]+=1
        else:
            x[val]=1
    return x
str="abcda"
print(char_freq(str))