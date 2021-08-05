# Range Extraction

def solution(args):
    args.append(0)
    s = ""
    i = 0
    while i != len(args) - 1:
        if args[i] == args[i + 1] - 1:
            c = []
            while i < len(args) - 1 and args[i] == args[i + 1] - 1:
                c.append(args[i])
                i += 1
            c.append(args[i])
            i += 1
            if len(c) > 2:
                s += str(c[0]) + "-" + str(c[-1]) + ","
            else:
                for k in c:
                    s += str(k) + ","
        else:
            s += str(args[i]) + ","
            i += 1
    return s[0 : -1]
    
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

print((solution([-3,-2,-1,2,10,15,16,18,19,20])))
