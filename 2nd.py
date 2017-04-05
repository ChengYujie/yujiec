def lett(i):
    if (ord(i) >= 65 and ord(i) <= 90):  # ASCII code for A-Z
        j = ord(i) - 64
    if (ord(i) >= 97 and ord(i) <= 122):  # ASCII code for a-z
        j = ord(i) - 96  # assign a value to each letter, a is 1, b is 2, etc.
    return j

stri=input("Input: ")
a=list(stri)
b =''                                         # Empty string to store output
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
    b=b+val
print (b)
