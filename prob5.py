def multiply(x):
    product=1
    for i,val in enumerate(x):
        product=product*val
    return product
def add(x):
    sum=0
    for i,val in enumerate(x):
        sum+=val
    return sum
a=[1,2,3,4]
print("Product:",multiply(a))
print("Sum:",add(a))