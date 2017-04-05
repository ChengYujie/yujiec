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

num = input('Input: ')
a = list(num)
lis = []
for dig in a:
    dig = int(dig)                            # Change character to integer
    if store(dig):
       lis.append(store(dig))                 # Create array to store letters for each input number

c = lis.pop(0)
for i in lis:                                # Combining letters for every possibility
    tes = []
    for j in c:
        for k in i:
            l = j + k
            tes.append(l)
    c = tes
print(c)