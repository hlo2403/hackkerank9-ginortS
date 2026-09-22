s=input()
result="".join(sorted(s,key=lambda ch:(
    ch.isdigit(),
    ch.isdigit() and int(ch)%2==0,
    ch.isupper(),
    ch
    
)))
print(result)
