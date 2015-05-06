__author__ = 'Jithu Jim'

#find missing bit
B = []
def cal_missing_bit(A):
    count_0 = 0
    count_1 = 0
    missing_bit = '0b'

    for e in A:
        one_digit = bin(e)[::-1][:-2]
        if one_digit[0] == str(0):
            count_0 +=1
        else:
            count_1 += 1

    if (A[-1] + 1) % 2 == 0:
        count_0_sup = (A[-1] + 1)/2
        count_1_sup = (A[-1] + 1)/2
    else:
        count_1_sup = (A[-1] + 1)/2
        count_0_sup = count_1_sup + 1

    if count_0 != count_0_sup:
        missing_bit = missing_bit + str(0)
        for e in A:
            if bin(e)[::-1][:-2][0] == str(0):
                x = len(bin(e)[::-1][:-2])
                y = len(bin(A[-1] + 1)[::-1][:-2])
                for e in range(y-x):
                    diff = '0'
                B.append(str('0b')+diff+bin(e)[::-1][:-2])


    if count_1 != count_1_sup:
        missing_bit = missing_bit + str(1)
        for e in A:
            if bin(e)[::-1][:-2][0] == str(1):
                x = len(bin(e)[::-1][:-2])
                y = len(bin(A[-1] + 1)[::-1][:-2])
                for e in range(y-x):
                    diff = '0'
                B.append(str('0b')+diff+bin(e)[::-1][:-2])

    print(missing_bit)

A = [0,1,2,3,4,6]
cal_missing_bit(A)
