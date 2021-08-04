# Jumping on the Clouds

def jumpingOnClouds(c):
    i = 0
    j = 0
    while i != len(c) - 1:
        if i + 2 <= len(c) - 1 and c[i + 2] != 1:
                i, j = i + 2, j + 1
        else:
            i, j = i + 1, j + 1
    return j
    
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
