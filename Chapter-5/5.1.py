__author__ = 'Jim'

#You are given two 32-bit numbers, N and M, and two bit positions, i and j.
#Write a method to set all bits between i and j in N equal to M (e.g., M becomes
#a substring of N located at i and starting at j).

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