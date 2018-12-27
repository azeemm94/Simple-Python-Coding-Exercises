def filter_long_words(a,n):
    x=[]
    for i,val in enumerate(a):
        if(len(val)>n):
            x.append(val)
    return x
a=["this","is","the","list","to","filter"]
n=3
print(filter_long_words(a,n))