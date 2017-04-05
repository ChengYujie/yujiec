def store(i):                              # Store letters to their corresponding number
    let=[]
    if(i>=2 and i<=6):
        let = [chr(97+(i-2)*3),chr(98+(i-2)*3),chr(99+(i-2)*3)]
    if(i==7):
        let = ['p','q','r','s']
    if(i==8):
        let = ['t','u','v']
    if(i==9):
        let = ['w','x','y','z']
    return let

def list_():                              # Get Combination letters for every possibility
    num = input('Input: ')               # with a given input
    a = list(num)
    lis = []
    for dig in a:
        dig = int(dig)
        if store(dig):
            lis.append(store(dig))
    c = lis.pop(0)
    for i in lis:
        tes = []
        for j in c:
            for k in i:
                l = j + k
                tes.append(l)
        c = tes
    return c

def getdic():                                           # Open and read dictionary file
    with open('C:\WordsRTF.RTF', 'r') as f:         # In this case the dictionary is stored in C:\WordsRTF.RTF
        content = f.read().splitlines()
        new = []
        for i in content:
            i = i[:-1]
            new.append(i)
        while new[0] != 'a':
            new.pop(0)
        new.insert(0, 'A')
        return new

str = getdic()
new_str = []
a = list_()

for element in a:                               # Checking if the input is in the dictionary
    for word in str:
        if word == element:
            new_str.append(word)
print(new_str)

