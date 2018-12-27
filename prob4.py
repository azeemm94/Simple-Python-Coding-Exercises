ch="a"
def vowel_find(ch):
    ch=ch.lower()
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        return "True"
    else:
        return "False"
print(vowel_find(ch))