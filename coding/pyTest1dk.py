c = 10101
rev_c = 0
dum_c = c

while dum_c != 0:          #reversing the number
    rev_c = rev_c * 10 + dum_c % 10
    dum_c //= 10       # double divide sign is for integer division

if rev_c == c:
    print("palindrm")
else:
    print("non palindrm")
