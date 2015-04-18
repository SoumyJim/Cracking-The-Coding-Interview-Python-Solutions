__author__ = 'Jithu Jim'

#Write a program to swap odd and even bits in an integer
# with as few instructions as possible (e.g., bit 0 and bit 1 are swapped,
# bit 2 and bit 3 are swapped, etc).

def swap_odd_even(x):
    mask1 = 0xaaaaaaaa
    mask2 = 0x55555555
    return bin(((x & mask1)>>1|( x & mask2)<<1))

print(swap_odd_even(0b111110010))