# Hash Tables - Ransom Note
    
def checkMagazine(magazine, note):
    magazine = dict(zip([i for i in range(len([i for i in magazine.split()]))], [i for i in magazine.split()]))
    note = dict(zip([i for i in range(len([i for i in note.split()]))], [i for i in note.split()]))
    for i in note.values():
        if i in magazine.values():
            for j in magazine:
                if magazine[j] == i:
                    magazine[j] = ""
        else:
            return "No"
    return "Yes"
    
print(checkMagazine("give me one grand today night", "give one grand today"))

print(checkMagazine("two times three is not four", "two times two is four"))

print(checkMagazine("ive got a lovely bunch of coconuts", "ive got some coconuts"))
