def find_longest_word(a):
    longest=0
    for i,val in enumerate(a):
        if(len(val)>longest):
            longest=len(val)
    return longest
a=["finding","the","length","of","longest","word","in","this","sentence"]
print(find_longest_word(a))