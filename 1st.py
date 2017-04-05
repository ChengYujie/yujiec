def lett(i):
    if (ord(i) >= 65 and ord(i) <= 90):  # ASCII code for A-Z
        j = ord(i) - 64
    if (ord(i) >= 97 and ord(i) <= 122):  # ASCII code for a-z
        j = ord(i) - 96  # assign a value to each letter, a is 1, b is 2, etc.
    return j

str=input("Input: ")
a=list(str)                                  #split input string into character list
num=0
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
print(num)

