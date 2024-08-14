s1 = "RAHUL"

def rever(s1):
    if (len(s1) == 1):
        return s1
    print("--> ", rever(s1[1:]) + s1[0])
    return rever(s1[1:]) + s1[0]
    
print(rever(s1))
