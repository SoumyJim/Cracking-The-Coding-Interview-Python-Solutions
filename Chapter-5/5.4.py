__author__ = 'Jim'
#Explain what the following code does: ((n & (n-1)) == 0).
#n & n-1 ==0 means n and n-1 doesnt have any 1s in common places.

n = 0b10001000
n_1 = 0b01110111
print(n&n_1)
