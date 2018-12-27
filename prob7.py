str="radar"
def is_palindrome(str):
    x=list(str)
    y=[]
    for i in reversed(x):
        y.append(i)
    rev="".join(y)
    if(rev==str):
        return "True"
    else:
        return "False"
print(is_palindrome(str))