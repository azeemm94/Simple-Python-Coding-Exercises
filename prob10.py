def generate_n_chars(x,n):
    a=[]
    for i in range(0,n):
        a.append(x)
    return "".join(a)
x="d"
n=3
print(generate_n_chars(x,n))