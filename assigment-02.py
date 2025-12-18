word = "muhammad Arsalan khan"

def tadat(a, anyword):
    anyword = anyword.lower()
    a = a.lower()
    count = 0
    for i in anyword:
        if(i == a):
            count += 1
    
    print(count)

tadat("a", word)