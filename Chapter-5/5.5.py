__author__ = 'Jithu Jim'
#Write a function to determine the number of bits required to convert integer A to integer B.

def count_bit_different(a,b):
    count = 0
    c = a^b
    c = bin(c)
    for e in c:
        if e == str(1):
            count += 1
    return (count)

print(count_bit_different(31,14))
print(count_bit_different(41,100))
print(count_bit_different(3,4))
print(count_bit_different(0,1))
print(count_bit_different(3341,1904))