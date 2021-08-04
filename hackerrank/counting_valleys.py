# Counting Valleys

def countingValleys(steps, path):
    s, l, i = 0, 0, 0
    while i != steps - 1:
        if path[i] == "D" and l == 0:
            c = 0
            while path[i] == "D":
                l, i, c = l - 1, i + 1, c + 1
            if c >= 2:
                s += 1
        elif path[i] == "D":
            l, i = l - 1, i +1
        elif path[i] == "U":
            l, i = l + 1, i + 1
    return s
    
print(countingValleys(8, ["U", "D", "D", "D", "U", "D", "U", "U"]))

print(countingValleys(12, ["D", "D", "U", "U", "D", "D", "U", "D", "U", "U", "U", "D"]))
