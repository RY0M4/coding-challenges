# Sales By Match

def sockMerchant(n, ar):
    s = 0
    k = set(ar)
    for i in k:
        c = 0
        for j in ar:
            if j == i:
                c += 1
            if c == 2:
                s += 1
                c = 0  
    return s  
    
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
