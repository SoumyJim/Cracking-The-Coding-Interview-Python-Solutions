__author__ = 'Jim'

def complement(n):
    size = len(format(n, 'b'))
    comp = n ^ ((1 << size) - 1)
    return '0b{0:0{1}b}'.format(comp, size)

def update_bit(n,m,i,j):
    largest = complement(1<<31)
    left = int(largest,2) - int(bin((1<<j)-1),2)
    right = int(bin((1<<i)-1),2)
    mask = left | right
    first = int(n,2) & mask
    second = int(m,2) << i
    result = first | second
    return(bin(result))


print(update_bit(b'10000000000',b'10101',2,6))