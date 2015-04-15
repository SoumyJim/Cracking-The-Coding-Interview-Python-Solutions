__author__ = 'Jim'

def image_rotatat(m):
    n = len(m)

    for i in range(0,n/2):
        for j in range(n):
            m[i][j], m[n-1-i][j] = m[n-1-i][j],m[i][j]

    for i in range(n):
        for j in range(i):
            m[i][j],m[j][i] = m[j][i],m[i][j]

    return m

print(image_rotatat([[3,4,2,3],[5,6,7,3],[9,12,9,10],[7,1,2,5]]))