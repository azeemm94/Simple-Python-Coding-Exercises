str="I am testing out this reversing code"
def reverse(str):
    x=list(str)
    y=[]
    for i in reversed(x):
        y.append(i)
    rev="".join(y)
    return rev
print(reverse(str))