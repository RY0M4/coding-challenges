# Catching Car Mileage Numbers

def is_interesting(n, arr, c = 2):
    n = str(n)
    if len(n) <= 1 and len(n) + 2 < 10 or int(n) + 2 <= 99:
        return 0
    if int(n) in arr or is_sequence(n) == True or is_zero_sequence(n) == True or is_incremental_sequence(n) == True or is_decremental_sequence(n) == True or is_palindrome(n) == True:
        return 2
    if c != 0:
        n = int(n) + 1
        c -= 1
        if is_interesting(n, arr, c) == 2 or is_interesting(n, arr, c) == 1:
            return 1
        elif is_interesting(n, arr, c) == 0:
            return 0
    else:
        return 0
        
def is_sequence(n):
    if len(n) < 3:
        return False
    for i in range(len(n)):
        if i != len(n) - 1:
            if int(n[i + 1]) != int(n[i]):
                return False
    return True
    
def is_zero_sequence(n):
    if len(n) < 3:
        return False
    for i in range(len(n)):
        if i != len(n) - 1:
            if int(n[i + 1]) != 0:
                return False
    return True
    
def is_incremental_sequence(n):
    if len(n) < 3:
        return False
    for i in range(len(n)):
        if i != len(n) - 1:
            if int(n[i + 1]) != int(n[i]) + 1:
                if int(n[i]) != 9 or int(n[i + 1]) != 0: 
                    return False
    return True
    
def is_decremental_sequence(n):
    if len(n) < 3:
        return False
    for i in range(len(n)):
        if i != len(n) - 1:
            if int(n[i + 1]) != int(n[i]) - 1:
                return False
    return True
    
def is_palindrome(n):
    if len(n) < 3:
        return False
    i = 0
    while i != len(n):
        if n[i] != n[-1 - i]:
            return False
        else:
            i += 1
    return True

print(is_interesting(3, [1337, 256]))

print(is_interesting(1336, [1337, 256]))

print(is_interesting(1337, [1337, 256]))

print(is_interesting(11208, [1337, 256]))

print(is_interesting(11209, [1337, 256]))

print(is_interesting(11211, [1337, 256]))
