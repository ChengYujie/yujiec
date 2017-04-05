def lett(i):
    if (ord(i) >= 65 and ord(i) <= 90):  # ASCII code for A-Z
        j = ord(i) - 64
    if (ord(i) >= 97 and ord(i) <= 122):  # ASCII code for a-z
        j = ord(i) - 96  # assign a value to each letter, a is 1, b is 2, etc.
    return j

def store(i):                     # Store letters to their corresponding number
    let = []
    if(i>=2 and i<=6 ):
        let = [chr(97+(i-2)*3),chr(98+(i-2)*3),chr(99+(i-2)*3)]
    if(i==7):
        let = ['p','q','r','s']
    if(i==8):
        let = ['t','u','v']
    if(i==9):
        let = ['w','x','y','z']
    return let

def list_(a):                              # Get Combination letters for every possibility
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

def number_of_click(a):
    num = 0
    for let in a:
        i = lett(let)
        if(i<=15):                               # Letters in 2-6
            val=i%3
        if(i>15 and i<20):                      # Letters in 7
            val=i-15
        if(i>19 and i<23):                      # Letters in 8
            val=i-19
        if(i>22):                               # Letters in 9
            val=i-22
        if (val == 1):                          # Calculation of number of clicks
            num = num + 1
        if (val == 2):
            num = num + 2
        if (val == 0 or val == 3):
            num = num + 3
        if(val ==4):
            num = num + 4
    print("Number of clicks: " , num)




def number_input(a):
    b = ''
    for let in a:
        i = lett(let)
        if(i<=15):                                # Assign letter for 2-6
            j=i-1
            val=j//3
            val=val+2
        if(i>15 and i<20):                       # Assign letter for 7
            val=7
        if(i>19 and i<23):                       # Assign letter for 8
            val=8
        if(i>22):                                # Assign letter for 9
            val=9
        val=str(val)
        b = b + val
    print("Input digits: " , b)

def getdic():                                           # Open and read dictionary file
    with open('C:\WordsRTF.RTF', 'r') as f:         # In this case the dictionary is stired in C:\WordsRTF.RTF
        content = f.read().splitlines()
        new = []
        for i in content:
            i = i[:-1]
            new.append(i)
        while new[0] != 'a':
            new.pop(0)
        new.insert(0, 'A')
        return new

def check_dic(a):
    new_str = []
    str = getdic()
    for element in a:  # Checking if the input is in the dictionary
        for word in str:
            if word == element:
                new_str.append(word)
    print(new_str)

strr=input("Input: ")
a = list(strr)
for i in a:
    if i.isalpha():
        option1 = 1
    else:
        option1 = 0
        break
for i in a:
    if i.isdigit():
        option2 = 1
    else:
        option2 = 0
        break
if option1:
    number_of_click(a)
    number_input(a)
if option2:
    print(list_(a))
    check_dic(list_(a))