__author__ = 'Jim'
#Given a (decimal - e.g. 3.72)
# number that is passed in as a string, print the binary representation.
# If the number can not be represented accurately in binary, print “ERROR”

def decimal_to_binary(d):
    int_part ,dec_part = str(d).split('.')
    int_result = ''
    dec_result = ''
    if int(int_part) == '' or int(int_part) == 0:
        int_result += str(0)
    if int(dec_part) == '' or int(dec_part) == 0:
        dec_result += str(0)

    int_part = int(int_part)
    dec_part = float('.'+dec_part)

    #handling the int part
    while(int_part>0):
        int_r = int_part % 2
        int_result += str(int_r)
        int_part = int_part//2

    while(len(dec_result)<33 and dec_part >0):
        dec_part = dec_part * 2
        if dec_part >=1:
            dec_result += str(1)
        else:
            dec_result += str(0)
        extra,dec_part = str(dec_part).split('.')
        dec_part = float('.'+dec_part)

    if len(dec_result) >= 32:
        return 'ERROR'
    else:
        return int_result[::-1]+'.'+dec_result


print(decimal_to_binary(3.75))
print(decimal_to_binary(19023.75))
print(decimal_to_binary(3.78901))
print(decimal_to_binary(0.0))
print(decimal_to_binary(000.09))
print(decimal_to_binary(1.))
print(decimal_to_binary(.0))
